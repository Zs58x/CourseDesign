# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['E:\\courseDesign\\yolov5-1229final\\GUI.py', 'E:\\courseDesign\\yolov5-1229final\\detect.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('E:\\courseDesign\\yolov5-1229final\\weights\\*', 'weights'),
        ('E:\\courseDesign\\yolov5-1229final\\models\\*', 'models'),
        ('E:\\courseDesign\\yolov5-1229final\\utils\\*', 'utils'),
        ('E:\\courseDesign\\yolov5-1229final\\data\\*', 'data'),
        ('E:\\courseDesign\\yolov5-1229final\\image\\*', 'image'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='GUI',
)