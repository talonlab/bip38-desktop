#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from cx_Freeze import setup, Executable

import platform

from src.info import __version__ as version, __author__ as author, __description__ as description


app_name  = "BIP38"

# Get platform info
platform_name = platform.system().lower()
machine_arch = platform.machine()
app_version = version.lstrip("v")

if platform.system() == "Windows":
    icon_path = "src/ui/images/icon/icon.ico"
else:
    icon_path = "src/ui/images/svg/logo.svg"

msi_shortcut_table = [
    (
        "DesktopShortcut",             # Shortcut
        "DesktopFolder",               # Directory_
        app_name,                      # Name that will be show on the link
        "TARGETDIR",                   # Component_
        f"[TARGETDIR]{app_name}.exe",  # Target exe to exexute
        None,                          # Arguments
        None,                          # Description
        None,                          # Hotkey
        None,                          # Icon
        None,                          # IconIndex
        None,                          # ShowCmd
        'TARGETDIR'                    # WkDir
    )
]

bdist_mac_opt = {
    "iconfile": "data/MyIcon.icns",
    "bundle_name": app_name,
    "include_resources": [("src/ui/images", "Resources")],
    "codesign_identity": "Developer ID Application: Talon Lab"
}

bdist_dmg_options = {
    "volume_label": f"{app_name}-{app_version}-{platform_name}-{machine_arch}",
    "applications_shortcut": True,
    "background": icon_path
}

msi_directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("BIP38Menu", "ProgramMenuFolder", "BIP38~1|BIP38")
]

msi_data = {
    "Shortcut": msi_shortcut_table,
    "Directory": msi_directory_table
}

bdist_msi_opt = {
    "add_to_path": False,
    "data": msi_data,
    "initial_target_dir": f"[ProgramFiles64Folder]\\{app_name}",
    "install_icon": icon_path,
    "upgrade_code": "{E4A369F6-FC76-3013-A420-3BB9B370711C}",
    "license_file": "data/TERMS_AND_CONDITIONS.rtf"
}

build_exe_opt = {
    "packages": ["_scrypt"],
    "excludes": ["tkinter", "PySide6.QtNetwork", "PySide6.translations"],
    "bin_excludes": [
        "Qt6Network.dll", "Qt6OpenGL.dll", "Qt6Pdf.dll", "Qt6Qml.dll", "Qt6QmlMeta.dll",
        "Qt6QmlModels.dll", "Qt6QmlWorkerScript.dll", "Qt6Quick.dll", "Qt6VirtualKeyboard.dll",
        "qgif.dll", "qicns.dll", "qjpeg.dll", "qpdf.dll", "qtga.dll", "qtiff.dll", "qwbmp.dll", "qwebp.dll",
        "qtvirtualkeyboardplugin.dll", "qtuiotouchplugin.dll", "qdirect2d.dll", "qoffscreen.dll", "qminimal.dll"
    ],
    "include_msvcr": True,
    "include_files":[
            ("data/MyIcon.icns", "MyApp.app/Contents/Resources/icon.icns"),
        ]
}

executables = [
    Executable(
        "launch.py",
        base="gui",
        icon=icon_path,
        target_name=app_name,
        shortcut_name=app_name,
        shortcut_dir="BIP38Menu",
        copyright=f"Copyright (C) 2024 {app_name}"
    )
]

setup(
    name=app_name,
    author=author,
    version=version,
    description=description,
    executables=executables,
    options={
        "build_exe": build_exe_opt,
        "bdist_msi": bdist_msi_opt,
        "bdist_mac": bdist_mac_opt,
        "bdist_dmg": bdist_dmg_options
    }
)