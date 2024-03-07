# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hv.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(649, 536)
        icon = QIcon()
        icon.addFile(u":/on/icons/on/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(64, 64))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icons_only_widget = QWidget(self.centralwidget)
        self.icons_only_widget.setObjectName(u"icons_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icons_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logo_label_1 = QLabel(self.icons_only_widget)
        self.logo_label_1.setObjectName(u"logo_label_1")
        self.logo_label_1.setMinimumSize(QSize(50, 50))
        self.logo_label_1.setMaximumSize(QSize(50, 50))
        self.logo_label_1.setPixmap(QPixmap(u":/others_off/icons/others_off/box.svg"))
        self.logo_label_1.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo_label_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.system_infos_btn_1 = QPushButton(self.icons_only_widget)
        self.system_infos_btn_1.setObjectName(u"system_infos_btn_1")
        self.system_infos_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/off/icons/off/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/on/icons/on/airplay.svg", QSize(), QIcon.Normal, QIcon.On)
        self.system_infos_btn_1.setIcon(icon1)
        self.system_infos_btn_1.setIconSize(QSize(20, 20))
        self.system_infos_btn_1.setCheckable(True)
        self.system_infos_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.system_infos_btn_1)

        self.activity_btn_1 = QPushButton(self.icons_only_widget)
        self.activity_btn_1.setObjectName(u"activity_btn_1")
        self.activity_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/off/icons/off/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/on/icons/on/activity.svg", QSize(), QIcon.Normal, QIcon.On)
        self.activity_btn_1.setIcon(icon2)
        self.activity_btn_1.setIconSize(QSize(20, 20))
        self.activity_btn_1.setCheckable(True)
        self.activity_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.activity_btn_1)

        self.disks_btn_1 = QPushButton(self.icons_only_widget)
        self.disks_btn_1.setObjectName(u"disks_btn_1")
        self.disks_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/off/icons/off/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/on/icons/on/disc.svg", QSize(), QIcon.Normal, QIcon.On)
        self.disks_btn_1.setIcon(icon3)
        self.disks_btn_1.setIconSize(QSize(20, 20))
        self.disks_btn_1.setCheckable(True)
        self.disks_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.disks_btn_1)

        self.cpu_btn_1 = QPushButton(self.icons_only_widget)
        self.cpu_btn_1.setObjectName(u"cpu_btn_1")
        self.cpu_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/off/icons/off/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/on/icons/on/cpu.svg", QSize(), QIcon.Normal, QIcon.On)
        self.cpu_btn_1.setIcon(icon4)
        self.cpu_btn_1.setIconSize(QSize(20, 20))
        self.cpu_btn_1.setCheckable(True)
        self.cpu_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.cpu_btn_1)

        self.network_btn_1 = QPushButton(self.icons_only_widget)
        self.network_btn_1.setObjectName(u"network_btn_1")
        self.network_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/off/icons/off/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/on/icons/on/wifi.svg", QSize(), QIcon.Normal, QIcon.On)
        self.network_btn_1.setIcon(icon5)
        self.network_btn_1.setIconSize(QSize(20, 20))
        self.network_btn_1.setCheckable(True)
        self.network_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.network_btn_1)

        self.about_btn_1 = QPushButton(self.icons_only_widget)
        self.about_btn_1.setObjectName(u"about_btn_1")
        self.about_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/off/icons/off/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/on/icons/on/info.svg", QSize(), QIcon.Normal, QIcon.On)
        self.about_btn_1.setIcon(icon6)
        self.about_btn_1.setIconSize(QSize(20, 20))
        self.about_btn_1.setCheckable(True)
        self.about_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.about_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 324, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.quit_btn_1 = QPushButton(self.icons_only_widget)
        self.quit_btn_1.setObjectName(u"quit_btn_1")
        self.quit_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/off/icons/off/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_btn_1.setIcon(icon7)
        self.quit_btn_1.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.quit_btn_1)


        self.gridLayout.addWidget(self.icons_only_widget, 0, 0, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_2 = QLabel(self.full_menu_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u":/others_off/icons/others_off/box.svg"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font = QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.system_infos_btn_2 = QPushButton(self.full_menu_widget)
        self.system_infos_btn_2.setObjectName(u"system_infos_btn_2")
        self.system_infos_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.system_infos_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.system_infos_btn_2.setIcon(icon1)
        self.system_infos_btn_2.setIconSize(QSize(18, 18))
        self.system_infos_btn_2.setCheckable(True)
        self.system_infos_btn_2.setAutoExclusive(True)
        self.system_infos_btn_2.setFlat(False)

        self.verticalLayout_2.addWidget(self.system_infos_btn_2, 0, Qt.AlignVCenter)

        self.activity_btn_2 = QPushButton(self.full_menu_widget)
        self.activity_btn_2.setObjectName(u"activity_btn_2")
        self.activity_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.activity_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.activity_btn_2.setIcon(icon2)
        self.activity_btn_2.setIconSize(QSize(18, 18))
        self.activity_btn_2.setCheckable(True)
        self.activity_btn_2.setAutoExclusive(True)
        self.activity_btn_2.setFlat(False)

        self.verticalLayout_2.addWidget(self.activity_btn_2, 0, Qt.AlignVCenter)

        self.disks_btn_2 = QPushButton(self.full_menu_widget)
        self.disks_btn_2.setObjectName(u"disks_btn_2")
        self.disks_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.disks_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.disks_btn_2.setIcon(icon3)
        self.disks_btn_2.setIconSize(QSize(18, 18))
        self.disks_btn_2.setCheckable(True)
        self.disks_btn_2.setAutoExclusive(True)
        self.disks_btn_2.setFlat(False)

        self.verticalLayout_2.addWidget(self.disks_btn_2, 0, Qt.AlignVCenter)

        self.cpu_btn_2 = QPushButton(self.full_menu_widget)
        self.cpu_btn_2.setObjectName(u"cpu_btn_2")
        self.cpu_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.cpu_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.cpu_btn_2.setIcon(icon4)
        self.cpu_btn_2.setIconSize(QSize(18, 18))
        self.cpu_btn_2.setCheckable(True)
        self.cpu_btn_2.setAutoExclusive(True)
        self.cpu_btn_2.setFlat(False)

        self.verticalLayout_2.addWidget(self.cpu_btn_2, 0, Qt.AlignVCenter)

        self.network_btn_2 = QPushButton(self.full_menu_widget)
        self.network_btn_2.setObjectName(u"network_btn_2")
        self.network_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.network_btn_2.setLayoutDirection(Qt.LeftToRight)
        self.network_btn_2.setIcon(icon5)
        self.network_btn_2.setIconSize(QSize(18, 18))
        self.network_btn_2.setCheckable(True)
        self.network_btn_2.setAutoExclusive(True)
        self.network_btn_2.setFlat(False)

        self.verticalLayout_2.addWidget(self.network_btn_2, 0, Qt.AlignVCenter)

        self.about_btn_2 = QPushButton(self.full_menu_widget)
        self.about_btn_2.setObjectName(u"about_btn_2")
        self.about_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_btn_2.setIcon(icon6)
        self.about_btn_2.setIconSize(QSize(18, 18))
        self.about_btn_2.setCheckable(True)
        self.about_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.about_btn_2, 0, Qt.AlignVCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 328, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.quit_btn_2 = QPushButton(self.full_menu_widget)
        self.quit_btn_2.setObjectName(u"quit_btn_2")
        self.quit_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.quit_btn_2.setIcon(icon7)
        self.quit_btn_2.setIconSize(QSize(14, 14))

        self.verticalLayout_4.addWidget(self.quit_btn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.widget_3)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 9, 5)
        self.change_btn = QPushButton(self.header_widget)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/others_off/icons/others_off/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon8)
        self.change_btn.setIconSize(QSize(20, 20))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.change_btn)

        self.horizontalSpacer = QSpacerItem(187, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_input = QLineEdit(self.header_widget)
        self.search_input.setObjectName(u"search_input")

        self.horizontalLayout.addWidget(self.search_input)

        self.search_btn = QPushButton(self.header_widget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/on/icons/on/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon9)
        self.search_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(187, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.user_btn = QPushButton(self.header_widget)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/on/icons/on/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon10)
        self.user_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.user_btn)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_6 = QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_7 = QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_9 = QLabel(self.page_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_8 = QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_10 = QLabel(self.page_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setStyleSheet(u"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_9 = QGridLayout(self.page_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_2 = QLabel(self.page_8)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_8)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.change_btn.toggled.connect(self.icons_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.system_infos_btn_1.toggled.connect(self.system_infos_btn_2.setChecked)
        self.disks_btn_1.toggled.connect(self.disks_btn_2.setChecked)
        self.cpu_btn_1.toggled.connect(self.cpu_btn_2.setChecked)
        self.activity_btn_1.toggled.connect(self.activity_btn_2.setChecked)
        self.network_btn_1.toggled.connect(self.network_btn_2.setChecked)
        self.system_infos_btn_2.toggled.connect(self.system_infos_btn_1.setChecked)
        self.disks_btn_2.toggled.connect(self.disks_btn_1.setChecked)
        self.cpu_btn_2.toggled.connect(self.cpu_btn_1.setChecked)
        self.activity_btn_2.toggled.connect(self.activity_btn_1.setChecked)
        self.network_btn_2.toggled.connect(self.network_btn_1.setChecked)
        self.quit_btn_2.clicked.connect(MainWindow.close)
        self.quit_btn_1.clicked.connect(MainWindow.close)
        self.about_btn_1.toggled.connect(self.about_btn_2.setChecked)
        self.about_btn_2.toggled.connect(self.about_btn_1.setChecked)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label_1.setText("")
        self.system_infos_btn_1.setText("")
        self.activity_btn_1.setText("")
        self.disks_btn_1.setText("")
        self.cpu_btn_1.setText("")
        self.network_btn_1.setText("")
        self.about_btn_1.setText("")
        self.quit_btn_1.setText("")
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"Hardware View", None))
        self.system_infos_btn_2.setText(QCoreApplication.translate("MainWindow", u"System Infos", None))
        self.activity_btn_2.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.disks_btn_2.setText(QCoreApplication.translate("MainWindow", u"Disks", None))
        self.cpu_btn_2.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.network_btn_2.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.about_btn_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.quit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.change_btn.setText("")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.search_btn.setText("")
        self.user_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"System Infos Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Activity Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Disks Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CPU Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Network page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"User Page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"About Page", None))
    # retranslateUi

