#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

import sys

from desktop.main import BIP38Application


def main() -> None:
    qapp: QApplication = QApplication(sys.argv)

    palette = QPalette()
    palette.setColor(QPalette.Active, QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Disabled, QPalette.Text, QColor(170, 170, 170))
    qapp.setPalette(palette)

    main_application: BIP38Application = BIP38Application()
    main_application.app.show()
    sys.exit(qapp.exec())


if __name__ == '__main__':
    main()
