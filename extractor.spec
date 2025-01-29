# extractor.spec
# PyInstaller spec file for Position Log Extractor

# Import required PyInstaller modules
from PyInstaller.utils.hooks import collect_submodules
import os

# Define the script path manually
script_path = "main.py"

# Collecting dependencies
hidden_imports = collect_submodules('pdfplumber')

# Define the PyInstaller build settings
a = Analysis(
    [script_path],
    pathex=[os.getcwd()],  # Use current working directory
    binaries=[],
    datas=[],
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Position Log Extractor",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want a console window
    icon=['icon.ico']
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="PositionLogExtractor",
)
