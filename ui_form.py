# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_name = QLineEdit(self.centralwidget)
        self.list_name.setObjectName(u"list_name")

        self.gridLayout.addWidget(self.list_name, 6, 2, 1, 1)

        self.csv_btn = QPushButton(self.centralwidget)
        self.csv_btn.setObjectName(u"csv_btn")

        self.gridLayout.addWidget(self.csv_btn, 4, 0, 1, 1)

        self.csv_file_name = QLineEdit(self.centralwidget)
        self.csv_file_name.setObjectName(u"csv_file_name")

        self.gridLayout.addWidget(self.csv_file_name, 6, 0, 1, 1)

        self.json_list = QTextEdit(self.centralwidget)
        self.json_list.setObjectName(u"json_list")
        self.json_list.setReadOnly(True)

        self.gridLayout.addWidget(self.json_list, 7, 1, 1, 1)

        self.edit_list = QPushButton(self.centralwidget)
        self.edit_list.setObjectName(u"edit_list")

        self.gridLayout.addWidget(self.edit_list, 4, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 256, 366))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 7, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.customer_review = QCheckBox(self.groupBox)
        self.customer_review.setObjectName(u"customer_review")

        self.gridLayout_2.addWidget(self.customer_review, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 7, 1, 1)

        self.visible = QCheckBox(self.groupBox)
        self.visible.setObjectName(u"visible")

        self.gridLayout_2.addWidget(self.visible, 1, 6, 1, 1)

        self.product_id = QLineEdit(self.groupBox)
        self.product_id.setObjectName(u"product_id")

        self.gridLayout_2.addWidget(self.product_id, 1, 2, 1, 1)

        self.in_stock = QCheckBox(self.groupBox)
        self.in_stock.setObjectName(u"in_stock")
        self.in_stock.setText(u"Item in Stock?")
        self.in_stock.setTristate(False)

        self.gridLayout_2.addWidget(self.in_stock, 2, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)

        self.published = QCheckBox(self.groupBox)
        self.published.setObjectName(u"published")

        self.gridLayout_2.addWidget(self.published, 2, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.product_name = QLineEdit(self.groupBox)
        self.product_name.setObjectName(u"product_name")

        self.gridLayout_2.addWidget(self.product_name, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)

        self.list_box = QTextEdit(self.centralwidget)
        self.list_box.setObjectName(u"list_box")

        self.gridLayout.addWidget(self.list_box, 7, 2, 1, 1)

        self.create_list = QPushButton(self.centralwidget)
        self.create_list.setObjectName(u"create_list")

        self.gridLayout.addWidget(self.create_list, 4, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.list_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name Of List", None))
        self.csv_btn.setText(QCoreApplication.translate("MainWindow", u"Create CSV File", None))
        self.csv_file_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name Of CSV File", None))
        self.edit_list.setText(QCoreApplication.translate("MainWindow", u"Edit List", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Basic Product Info", None))
        self.customer_review.setText(QCoreApplication.translate("MainWindow", u"Allow for Customer Reviews", None))
        self.visible.setText(QCoreApplication.translate("MainWindow", u"Visible", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Product ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Product Name:", None))
        self.published.setText(QCoreApplication.translate("MainWindow", u"Published", None))
        self.list_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.list_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name:Value", None))
        self.create_list.setText(QCoreApplication.translate("MainWindow", u"Create List", None))
    # retranslateUi

