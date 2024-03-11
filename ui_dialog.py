# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.dict_name = QComboBox(Dialog)
        self.dict_name.setObjectName(u"dict_name")

        self.gridLayout.addWidget(self.dict_name, 0, 0, 1, 1)

        self.dict_key = QComboBox(Dialog)
        self.dict_key.setObjectName(u"dict_key")

        self.gridLayout.addWidget(self.dict_key, 0, 1, 1, 1)

        self.new_dict_key = QLineEdit(Dialog)
        self.new_dict_key.setObjectName(u"new_dict_key")

        self.gridLayout.addWidget(self.new_dict_key, 1, 1, 1, 1)

        self.del_dict_key_value = QPushButton(Dialog)
        self.del_dict_key_value.setObjectName(u"del_dict_key_value")

        self.gridLayout.addWidget(self.del_dict_key_value, 2, 1, 1, 1)

        self.dict_value = QLineEdit(Dialog)
        self.dict_value.setObjectName(u"dict_value")

        self.gridLayout.addWidget(self.dict_value, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Abort|QDialogButtonBox.Save)

        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.del_dict_key_value.setText(QCoreApplication.translate("Dialog", u"Delete Key Value", None))
    # retranslateUi

