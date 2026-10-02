# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['lucky_dangle.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('charms', 'charms'),
        ('bell_sound.wav', '.'),
        ('assets', 'assets')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LuckyDangle',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False, # Critical: Hides the background terminal window on Mac
    disable_windowed_traceback=False,
    argv_emulation=True, # Enables macOS features like drag-and-drop
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
    name='LuckyDangle',
)
app = BUNDLE(
    coll,
    name='LuckyDangle.app',
    icon='assets/icon.icns',
    bundle_identifier='com.shyleshpatil.luckydangle',
)