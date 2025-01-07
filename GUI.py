# GUIdemo2.py
# Demo2 of GUI by PqYt5
# Copyright 2021 Youcans, XUPT
# Crated：2021-10-06
import argparse
import datetime
import os
import random
import time
import cv2
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
import sys
import torch
import detect

from models.common import DetectMultiBackend
from ui.mainwindow_ui import Ui_MainWindow
from utils.general import check_img_size


class UI_Logic_Window(QMainWindow):
    def __init__(self,parent=None):
        super(UI_Logic_Window,self).__init__(parent)
        #初始化UI
        self.initUI()
        #预加载模型
        self.LoadModel()

    #初始化界面
    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.output_folder = 'output/'
        self.cap = cv2.VideoCapture()
        self.vid_writer = None
        self.camera_detect = False
        self.num_stop = 1  # 暂停与播放辅助信号，note：通过奇偶来控制暂停与播放
        self.openfile_name_model = None        # 权重初始文件名
        self.count = 0
        self.start_time = time.time()        # 打开线程
        self.stop_going = 0
        self.half = False

        #视频与摄像头的刷新计时器
        self.timer_video = QtCore.QTimer(self)

        #时间显示
        self.lcd_time = QTimer(self)
        self.lcd_time.setInterval(1000)
        self.lcd_time.timeout.connect(self.refresh)
        self.lcd_time.start()

        #信号与槽函数的连接
        self.init_slots()

    #时间刷新
    def refresh(self):
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.lcdNumber.display(now_time)

    #初始化槽函数
    def init_slots(self):
        self.ui.btn_loadimg.clicked.connect(self.button_image_Open)
        self.ui.btn_loadvideo.clicked.connect(self.button_video_Open)
        self.ui.btn_opencamera.clicked.connect(self.button_camera_Open)
        self.ui.btn_initweight.clicked.connect(self.button_camera_detect)
        self.ui.btn_closecamera.clicked.connect(self.button_camera_close)
        self.ui.btn_clear.clicked.connect(self.button_clear)
        self.ui.btn_going.clicked.connect(self.button_going)
        self.ui.btn_stop.clicked.connect(self.button_stop)
        self.timer_video.timeout.connect(self.show_video_frame)

    #加载模型
    def LoadModel(self):
        self.opt = detect.parse_opt()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        weights = self.opt.weights
        imgsz = self.opt.imgsz
        self.model = DetectMultiBackend(weights, device=self.device)
        stride = self.model.stride
        self.imgsz = check_img_size(imgsz, s=stride)  # check image size
        if self.half:
            self.model.half()

        # Get names and colors
        self.names = self.model.names
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in self.names]
        self.ui.textBrowser_print.append("模型加载完成")

    #选择图片并进行预测
    def button_image_Open(self):
        name_list = []
        img_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", "fire/images", "*.jpg;;*.png;;All Files(*)")

        if img_name:
            self.ui.textBrowser_print.append("打开图片成功")
            img = cv2.imread(img_name)
            self.origin = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
            #调整图像大小
            self.origin = cv2.resize(self.origin,(640,480), interpolation=cv2.INTER_AREA)
            #OpenCV to QtGUI
            self.QtImg_origin = QtGui.QImage(self.origin.data, self.origin.shape[1], self.origin.shape[0], QtGui.QImage.Format_RGB32)
            #显示原始图像
            self.ui.label_origin.setPixmap(QtGui.QPixmap.fromImage(self.QtImg_origin))
            self.ui.label_origin.setScaledContents(True) #自适应大小

            #预测
            info_show = ""
            img_out,info_show = detect.run3(model=self.model,img=img)

            # 检测信息显示在界面
            self.ui.textBrowser_detect.append(info_show)

            # 检测结果显示在界面
            self.result = cv2.cvtColor(img_out, cv2.COLOR_BGR2BGRA)
            self.result = cv2.resize(self.result, (640, 480), interpolation=cv2.INTER_AREA)
            QtImg = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],QtGui.QImage.Format_RGB32)
            self.ui.label_detect.setPixmap(QtGui.QPixmap.fromImage(QtImg))
            self.ui.label_detect.setScaledContents(True)  # 设置图像自适应界面大小



    def button_video_Open(self):
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "打开视频", "fire/video/", "*.mp4;;*.avi;;All Files(*)")
        flag = self.cap.open(video_name)

        # 判断摄像头是否打开
        if not flag:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开视频失败", buttons=QtWidgets.QMessageBox.Ok,defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            # -------------------------写入视频----------------------------------#
            self.ui.textBrowser_print.append("打开视频检测")
            fps, w, h, save_path = self.set_video_name_and_path()
            self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

            self.timer_video.start(30)  # 以30ms为间隔，启动或重启定时器
            # 进行视频识别时，关闭其他按键点击功能
            self.ui.btn_loadvideo.setDisabled(True)
            self.ui.btn_loadimg.setDisabled(True)
            self.ui.btn_opencamera.setDisabled(True)

    def set_video_name_and_path(self):
        # 获取当前系统时间，作为img和video的文件名
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # if vid_cap:  # video
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 视频检测结果存储位置
        save_path = self.output_folder + 'video_output/' + now + '.mp4'
        return fps, w, h, save_path

    #对视频抽帧得到的图片进行识别
    def show_video_frame(self):
        name_list = []
        flag, img = self.cap.read()

        if img is not None:
            # 原始数据的显示
            self.origin = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
            self.origin = cv2.resize(self.origin, (640, 480), interpolation=cv2.INTER_AREA)
            self.QtImg_origin = QtGui.QImage(self.origin.data, self.origin.shape[1], self.origin.shape[0],
                                             QtGui.QImage.Format_RGB32)
            self.ui.label_origin.setPixmap(QtGui.QPixmap.fromImage(self.QtImg_origin))
            self.ui.label_origin.setScaledContents(True)  # 设置图像自适应界面大小

            # 检测数据的显示
            # info_show = self.detect(name_list, img)  # 检测结果写入到原始img上
            info_show = ""
            img,info_show = detect.run3(model=self.model, img=img)

            self.vid_writer.write(img)  # 检测结果写入视频
            # 检测信息显示在界面
            self.ui.textBrowser_detect.append(info_show)
            show = cv2.resize(img, (640, 480),interpolation=cv2.INTER_AREA)  # 直接将原始img上的检测结果进行显示
            self.result = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                     QtGui.QImage.Format_RGB888)
            self.ui.label_detect.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.ui.label_detect.setScaledContents(True)  # 设置图像自适应界面大小
        else:
            self.timer_video.stop()
            # 读写结束，释放资源
            self.cap.release() # 释放video_capture资源
            self.vid_writer.release() # 释放video_writer资源
            self.ui.label_origin.clear()
            self.ui.label_detect.clear()
            self.ui.textBrowser_print.append("视频播放完毕")
            # 视频帧显示期间，禁用其他检测按键功能
            self.ui.btn_loadvideo.setDisabled(True)
            self.ui.btn_loadimg.setDisabled(True)
            self.ui.btn_opencamera.setDisabled(True)

    def button_camera_Open(self):
        self.camera_detect = True
        self.ui.textBrowser_print.append("打开摄像头")
        # 设置使用的摄像头序号，系统自带为0
        camera_num = 0
        # 打开摄像头
        self.cap = cv2.VideoCapture(camera_num)
        # 判断摄像头是否处于打开状态
        bool_open = self.cap.isOpened()
        if not bool_open:
            QtWidgets.QMessageBox.warning(self, u"Warning", u"打开摄像头失败", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u"Warning", u"打开摄像头成功", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            self.ui.btn_loadvideo.setDisabled(True)
            self.ui.btn_loadimg.setDisabled(True)

    def button_camera_detect(self):
        self.ui.textBrowser_print.append("启动摄像头检测")
        fps, w, h, save_path = self.set_video_name_and_path()
        fps = 5  # 控制摄像头检测下的fps，Note：保存的视频，播放速度有点快，我只是粗暴的调整了FPS
        self.vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
        self.timer_video.start(30)
        self.ui.btn_loadvideo.setDisabled(True)
        self.ui.btn_loadimg.setDisabled(True)
        self.ui.btn_opencamera.setDisabled(True)

    def button_camera_close(self):
        self.ui.textBrowser_print.append("关闭摄像头")
        self.timer_video.stop()  # 停止读取
        self.cap.release()  # 释放摄像头
        self.ui.label_origin.clear()  # 清空label画布
        self.ui.label_detect.clear()  # 清空label画布
        # self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 摄像头

        self.ui.btn_loadvideo.setDisabled(False)
        self.ui.btn_loadimg.setDisabled(False)
        self.ui.btn_opencamera.setDisabled(False)

    def button_clear(self):
        self.ui.textBrowser_print.append("清除显示区域")
        self.ui.textBrowser_print.clear()
        self.ui.textBrowser_detect.clear()

    def button_going(self):
        self.timer_video.blockSignals(False)
        # 暂停检测
        # 若QTimer已经触发，且激活
        if self.timer_video.isActive() == True and self.num_stop % 2 == 1:
            self.ui.btn_going.setText('继续')
            self.ui.textBrowser_print.append("视频暂停播放")
            self.num_stop = self.num_stop + 1  # 调整标记信号为偶数
            self.timer_video.blockSignals(True)
            # 继续检测
        else:
            self.num_stop = self.num_stop + 1
            self.ui.btn_going.setText('暂停')
            self.ui.textBrowser_print.append("视频继续播放")

    def button_stop(self):
        self.ui.textBrowser_print.append("视频结束播放")
        self.cap.release()  # 释放video_capture资源
        self.timer_video.stop()  # 停止读取
        if self.vid_writer != None:
            self.vid_writer.release()  # 释放video_writer资源

        self.ui.label_origin.clear()  # 清空label画布
        self.ui.label_detect.clear()  # 清空label画布
        # 启动其他检测按键功能
        self.ui.btn_loadvideo.setDisabled(False)
        self.ui.btn_loadimg.setDisabled(False)
        self.ui.btn_opencamera.setDisabled(False)

        # 结束检测时，查看暂停功能是否复位，将暂停功能恢复至初始状态
        # Note:点击暂停之后，num_stop为偶数状态
        if self.num_stop % 2 == 0:
            print("Reset stop/begin!")
            self.ui.btn_going.setText(u'暂停')
            self.num_stop = self.num_stop + 1
            self.timer_video.blockSignals(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    MainWindow = QMainWindow()  # 创建主窗口
    ui = UI_Logic_Window()
    ui.show()
    sys.exit(app.exec_())  # 在主线程中退出
