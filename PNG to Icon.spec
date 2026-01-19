# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/星泓 原D槽/星泓 檔案/星泓 電腦/程式/Python/Tools/PNG to Icon/PNG to Icon.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/星泓 原D槽/星泓 檔案/星泓 電腦/程式/Python/Tools/PNG to Icon/icon.ico', 'icon.ico')],
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
    a.binaries,
    a.datas,
    [],
    name='PNG to Icon',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\星泓 原D槽\\星泓 檔案\\星泓 電腦\\程式\\Python\\Tools\\PNG to Icon\\icon.ico'],
)
