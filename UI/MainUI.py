from PySide6.QtCore import (QLocale,
                            QMetaObject,
                            QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QComboBox, QFrame, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit,
                               QPlainTextEdit, QProgressBar, QPushButton,
                               QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
                               QVBoxLayout, QWidget)
from Assets import Resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1344, 745)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 80))
        self.Header.setMaximumSize(QSize(16777215, 80))
        self.Header.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.FeatureF = QFrame(self.Header)
        self.FeatureF.setObjectName(u"FeatureF")
        self.FeatureF.setFrameShape(QFrame.Shape.NoFrame)
        self.FeatureF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.FeatureF)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(9, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_44.addItem(self.horizontalSpacer_4)
        self.LogoFF = QFrame(self.FeatureF)
        self.LogoFF.setObjectName(u"LogoFF")
        self.LogoFF.setMaximumSize(QSize(50, 50))
        self.LogoFF.setFrameShape(QFrame.Shape.NoFrame)
        self.LogoFF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.LogoFF)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.labeLogol = QLabel(self.LogoFF)
        self.labeLogol.setObjectName(u"labeLogol")
        font = QFont()
        font.setPointSize(1)
        self.labeLogol.setFont(font)
        self.labeLogol.setPixmap(QPixmap(u":/Images/Assets/Images/SS.svg"))
        self.labeLogol.setScaledContents(True)
        self.labeLogol.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labeLogol.setWordWrap(False)

        self.verticalLayout_15.addWidget(self.labeLogol)

        self.horizontalLayout_44.addWidget(self.LogoFF)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_44.addItem(self.horizontalSpacer_3)

        self.line_5 = QFrame(self.FeatureF)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Shadow.Plain)
        self.line_5.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_44.addWidget(self.line_5)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_2)

        self.ChLangF = QFrame(self.FeatureF)
        self.ChLangF.setObjectName(u"ChLangF")
        self.ChLangF.setFrameShape(QFrame.Shape.NoFrame)
        self.ChLangF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.ChLangF)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.ChLangFLabel = QLabel(self.ChLangF)
        self.ChLangFLabel.setObjectName(u"ChLangFLabel")

        self.horizontalLayout_45.addWidget(self.ChLangFLabel)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer)

        self.ChLangFcomboBox = QComboBox(self.ChLangF)
        self.ChLangFcomboBox.addItem("")
        self.ChLangFcomboBox.addItem("")
        self.ChLangFcomboBox.addItem("")
        self.ChLangFcomboBox.setObjectName(u"ChLangFcomboBox")
        self.ChLangFcomboBox.setMinimumSize(QSize(0, 30))
        self.ChLangFcomboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_45.addWidget(self.ChLangFcomboBox)

        self.horizontalLayout_44.addWidget(self.ChLangF)

        self.labelSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.labelSpacer)

        self.ThemeF = QFrame(self.FeatureF)
        self.ThemeF.setObjectName(u"ThemeF")
        self.ThemeF.setFrameShape(QFrame.Shape.NoFrame)
        self.ThemeF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.ThemeF)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")

        self.horizontalLayout_44.addWidget(self.ThemeF)

        self.horizontalLayout.addWidget(self.FeatureF, 0, Qt.AlignmentFlag.AlignLeft)

        self.LogoF = QFrame(self.Header)
        self.LogoF.setObjectName(u"LogoF")
        self.LogoF.setFrameShape(QFrame.Shape.NoFrame)
        self.LogoF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.LogoF)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.TitleTTFrame = QFrame(self.LogoF)
        self.TitleTTFrame.setObjectName(u"TitleTTFrame")
        self.TitleTTFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.TitleTTFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.TitleTTFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.TITLEMAIN = QLabel(self.TitleTTFrame)
        self.TITLEMAIN.setObjectName(u"TITLEMAIN")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.TITLEMAIN.setFont(font1)

        self.verticalLayout_20.addWidget(self.TITLEMAIN)

        self.horizontalLayout_43.addWidget(self.TitleTTFrame)

        self.horizontalLayout.addWidget(self.LogoF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.WindowF = QFrame(self.Header)
        self.WindowF.setObjectName(u"WindowF")
        self.WindowF.setFrameShape(QFrame.Shape.NoFrame)
        # self.WindowF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.WindowF)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pbInf = QPushButton(self.WindowF)
        self.pbInf.setObjectName(u"pbInf")
        self.pbInf.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Assets/Icons/Info.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pbInf.setIcon(icon)

        self.horizontalLayout_42.addWidget(self.pbInf)

        self.pBMin = QPushButton(self.WindowF)
        self.pBMin.setObjectName(u"pBMin")
        self.pBMin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Assets/Icons/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBMin.setIcon(icon1)
        self.pBMin.setIconSize(QSize(20, 20))

        self.horizontalLayout_42.addWidget(self.pBMin)

        self.pBClose = QPushButton(self.WindowF)
        self.pBClose.setObjectName(u"pBClose")
        self.pBClose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Assets/Icons/Close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBClose.setIcon(icon2)
        self.pBClose.setIconSize(QSize(20, 20))

        self.horizontalLayout_42.addWidget(self.pBClose)

        self.horizontalLayout.addWidget(self.WindowF, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.Header, 0, Qt.AlignmentFlag.AlignTop)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        self.Body.setFrameShape(QFrame.Shape.StyledPanel)
        self.Body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Body)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ImageF = QFrame(self.Body)
        self.ImageF.setObjectName(u"ImageF")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ImageF.sizePolicy().hasHeightForWidth())
        self.ImageF.setSizePolicy(sizePolicy1)
        self.ImageF.setMinimumSize(QSize(300, 600))
        self.ImageF.setMaximumSize(QSize(300, 600))
        self.ImageF.setFrameShape(QFrame.Shape.NoFrame)
        self.ImageF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ImageF)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Image = QLabel(self.ImageF)
        self.Image.setObjectName(u"Image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Image.sizePolicy().hasHeightForWidth())
        self.Image.setSizePolicy(sizePolicy2)
        self.Image.setStyleSheet((u"border-image:url(:/Images/Assets/Images/IMG.png);\n"
                                  u"border-top-right-radius:50px;\n"
                                  u"border-bottom-right-radius:50px;\n"))
        self.Image.setMinimumSize(QSize(300, 515))
        self.Image.setMaximumSize(QSize(16777215, 900))
        self.Image.setScaledContents(True)
        self.Image.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.Image, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.ImageF)

        self.DataF = QFrame(self.Body)
        self.DataF.setObjectName(u"DataF")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.DataF.sizePolicy().hasHeightForWidth())
        self.DataF.setSizePolicy(sizePolicy3)
        self.DataF.setMinimumSize(QSize(0, 0))
        self.DataF.setMaximumSize(QSize(16777215, 16777215))
        self.DataF.setFrameShape(QFrame.Shape.NoFrame)
        self.DataF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.DataF)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.STQDATA = QStackedWidget(self.DataF)
        self.STQDATA.setObjectName(u"STQDATA")
        self.STQDATA.setFrameShape(QFrame.Shape.NoFrame)
        self.NameMP = QWidget()
        self.NameMP.setObjectName(u"NameMP")
        self.verticalLayout_12 = QVBoxLayout(self.NameMP)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.NameMFrame = QFrame(self.NameMP)
        self.NameMFrame.setObjectName(u"NameMFrame")
        self.NameMFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.NameMFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.NameMFrame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.NameMTF = QFrame(self.NameMFrame)
        self.NameMTF.setObjectName(u"NameMTF")
        self.NameMTF.setFrameShape(QFrame.Shape.Box)
        self.NameMTF.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_33 = QHBoxLayout(self.NameMTF)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.NameMTitleFrame = QLabel(self.NameMTF)
        self.NameMTitleFrame.setObjectName(u"NameMTitleFrame")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.NameMTitleFrame.setFont(font2)

        self.horizontalLayout_33.addWidget(self.NameMTitleFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_11.addWidget(self.NameMTF)

        self.NameMC01F = QGroupBox(self.NameMFrame)
        self.NameMC01F.setObjectName(u"NameMC01F")
        self.horizontalLayout_34 = QHBoxLayout(self.NameMC01F)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.NameM01F = QFrame(self.NameMC01F)
        self.NameM01F.setObjectName(u"NameM01F")
        self.NameM01F.setFrameShape(QFrame.Shape.NoFrame)
        self.NameM01F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.NameM01F)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.NameM01Label = QLabel(self.NameM01F)
        self.NameM01Label.setObjectName(u"NameM01Label")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.NameM01Label.setFont(font3)

        self.horizontalLayout_35.addWidget(self.NameM01Label)

        self.NameM01Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.NameM01Spacer)

        self.NameM01LineE = QLineEdit(self.NameM01F)
        self.NameM01LineE.setObjectName(u"NameM01LineE")
        self.NameM01LineE.setMinimumSize(QSize(200, 30))
        font4 = QFont()
        font4.setPointSize(11)
        self.NameM01LineE.setFont(font4)
        self.NameM01LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NameM01LineE.setClearButtonEnabled(True)

        self.horizontalLayout_35.addWidget(self.NameM01LineE)

        self.horizontalLayout_34.addWidget(self.NameM01F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_11.addWidget(self.NameMC01F)

        self.NameMC02F = QGroupBox(self.NameMFrame)
        self.NameMC02F.setObjectName(u"NameMC02F")
        self.horizontalLayout_36 = QHBoxLayout(self.NameMC02F)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.NameM02F = QFrame(self.NameMC02F)
        self.NameM02F.setObjectName(u"NameM02F")
        self.NameM02F.setFrameShape(QFrame.Shape.NoFrame)
        self.NameM02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.NameM02F)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.NameM02Label = QLabel(self.NameM02F)
        self.NameM02Label.setObjectName(u"NameM02Label")
        self.NameM02Label.setFont(font3)

        self.horizontalLayout_37.addWidget(self.NameM02Label)

        self.NameM02Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.NameM02Spacer)

        self.NameM02FLineE = QLineEdit(self.NameM02F)
        self.NameM02FLineE.setObjectName(u"NameM02FLineE")
        self.NameM02FLineE.setMinimumSize(QSize(200, 30))
        self.NameM02FLineE.setFont(font4)
        self.NameM02FLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NameM02FLineE.setClearButtonEnabled(True)

        self.horizontalLayout_37.addWidget(self.NameM02FLineE)

        self.horizontalLayout_36.addWidget(self.NameM02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_11.addWidget(self.NameMC02F)

        self.NameMC03F = QGroupBox(self.NameMFrame)
        self.NameMC03F.setObjectName(u"NameMC03F")
        self.horizontalLayout_38 = QHBoxLayout(self.NameMC03F)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.NameM03F = QFrame(self.NameMC03F)
        self.NameM03F.setObjectName(u"NameM03F")
        self.NameM03F.setFrameShape(QFrame.Shape.NoFrame)
        self.NameM03F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.NameM03F)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.NameM03Label = QLabel(self.NameM03F)
        self.NameM03Label.setObjectName(u"NameM03Label")
        self.NameM03Label.setFont(font3)

        self.horizontalLayout_39.addWidget(self.NameM03Label)

        self.NameM03Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.NameM03Spacer)

        self.NameM03LineE = QLineEdit(self.NameM03F)
        self.NameM03LineE.setObjectName(u"NameM03LineE")
        self.NameM03LineE.setMinimumSize(QSize(200, 30))
        self.NameM03LineE.setFont(font4)
        self.NameM03LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NameM03LineE.setClearButtonEnabled(True)

        self.horizontalLayout_39.addWidget(self.NameM03LineE)

        self.horizontalLayout_38.addWidget(self.NameM03F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_11.addWidget(self.NameMC03F)

        self.verticalLayout_12.addWidget(self.NameMFrame)

        self.STQDATA.addWidget(self.NameMP)
        self.CarboneP = QWidget()
        self.CarboneP.setObjectName(u"CarboneP")
        self.verticalLayout_3 = QVBoxLayout(self.CarboneP)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.CarboneFrame = QFrame(self.CarboneP)
        self.CarboneFrame.setObjectName(u"CarboneFrame")
        self.CarboneFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.CarboneFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.CarboneFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.CarboneTF = QFrame(self.CarboneFrame)
        self.CarboneTF.setObjectName(u"CarboneTF")
        self.CarboneTF.setFrameShape(QFrame.Shape.Box)
        self.CarboneTF.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.CarboneTF)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.CTitleFrame = QLabel(self.CarboneTF)
        self.CTitleFrame.setObjectName(u"CTitleFrame")
        self.CTitleFrame.setFont(font2)

        self.horizontalLayout_5.addWidget(self.CTitleFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.CarboneTF)

        self.CM01F = QGroupBox(self.CarboneFrame)
        self.CM01F.setObjectName(u"CM01F")
        self.horizontalLayout_6 = QHBoxLayout(self.CM01F)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.CMC01F = QFrame(self.CM01F)
        self.CMC01F.setObjectName(u"CMC01F")
        self.CMC01F.setFrameShape(QFrame.Shape.NoFrame)
        self.CMC01F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.CMC01F)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.CMC01Label = QLabel(self.CMC01F)
        self.CMC01Label.setObjectName(u"CMC01Label")
        self.CMC01Label.setFont(font3)

        self.horizontalLayout_11.addWidget(self.CMC01Label)

        self.CMC0Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.CMC0Spacer)

        self.CMC01LineE = QLineEdit(self.CMC01F)
        self.CMC01LineE.setObjectName(u"CMC01LineE")
        self.CMC01LineE.setMinimumSize(QSize(200, 30))
        self.CMC01LineE.setFont(font4)
        self.CMC01LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CMC01LineE.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.CMC01LineE)

        self.horizontalLayout_6.addWidget(self.CMC01F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.CM01F)

        self.CM02F = QGroupBox(self.CarboneFrame)
        self.CM02F.setObjectName(u"CM02F")
        self.horizontalLayout_8 = QHBoxLayout(self.CM02F)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.CMC02F = QFrame(self.CM02F)
        self.CMC02F.setObjectName(u"CMC02F")
        self.CMC02F.setFrameShape(QFrame.Shape.NoFrame)
        self.CMC02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.CMC02F)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.CMC02Label = QLabel(self.CMC02F)
        self.CMC02Label.setObjectName(u"CMC02Label")
        self.CMC02Label.setFont(font3)

        self.horizontalLayout_9.addWidget(self.CMC02Label)

        self.CMC02Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.CMC02Spacer)

        self.CMC02FLineE = QLineEdit(self.CMC02F)
        self.CMC02FLineE.setObjectName(u"CMC02FLineE")
        self.CMC02FLineE.setMinimumSize(QSize(200, 30))
        self.CMC02FLineE.setFont(font4)
        self.CMC02FLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CMC02FLineE.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.CMC02FLineE)

        self.horizontalLayout_8.addWidget(self.CMC02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.CM02F)

        self.CM03F = QGroupBox(self.CarboneFrame)
        self.CM03F.setObjectName(u"CM03F")
        self.horizontalLayout_7 = QHBoxLayout(self.CM03F)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.CMC03F = QFrame(self.CM03F)
        self.CMC03F.setObjectName(u"CMC03F")
        self.CMC03F.setFrameShape(QFrame.Shape.NoFrame)
        self.CMC03F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CMC03F)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.CMC03Label = QLabel(self.CMC03F)
        self.CMC03Label.setObjectName(u"CMC03Label")
        self.CMC03Label.setFont(font3)

        self.horizontalLayout_10.addWidget(self.CMC03Label)

        self.CMC03Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.CMC03Spacer)

        self.CMC03LineE = QLineEdit(self.CMC03F)
        self.CMC03LineE.setObjectName(u"CMC03LineE")
        self.CMC03LineE.setMinimumSize(QSize(200, 30))
        self.CMC03LineE.setFont(font4)
        self.CMC03LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CMC03LineE.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.CMC03LineE)

        self.horizontalLayout_7.addWidget(self.CMC03F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_4.addWidget(self.CM03F)

        self.verticalLayout_3.addWidget(self.CarboneFrame)

        self.STQDATA.addWidget(self.CarboneP)
        self.NitrogenP = QWidget()
        self.NitrogenP.setObjectName(u"NitrogenP")
        self.verticalLayout_8 = QVBoxLayout(self.NitrogenP)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.NitrogenFrame = QFrame(self.NitrogenP)
        self.NitrogenFrame.setObjectName(u"NitrogenFrame")
        self.NitrogenFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.NitrogenFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.NitrogenFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.NitrogenTF = QFrame(self.NitrogenFrame)
        self.NitrogenTF.setObjectName(u"NitrogenTF")
        self.NitrogenTF.setFrameShape(QFrame.Shape.Box)
        self.NitrogenTF.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_19 = QHBoxLayout(self.NitrogenTF)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.NTitleFrame = QLabel(self.NitrogenTF)
        self.NTitleFrame.setObjectName(u"NTitleFrame")
        self.NTitleFrame.setFont(font2)

        self.horizontalLayout_19.addWidget(self.NTitleFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_7.addWidget(self.NitrogenTF)

        self.NM01F = QGroupBox(self.NitrogenFrame)
        self.NM01F.setObjectName(u"NM01F")
        self.horizontalLayout_20 = QHBoxLayout(self.NM01F)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.NMN01F = QFrame(self.NM01F)
        self.NMN01F.setObjectName(u"NMN01F")
        self.NMN01F.setFrameShape(QFrame.Shape.NoFrame)
        self.NMN01F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.NMN01F)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.NMN01Label = QLabel(self.NMN01F)
        self.NMN01Label.setObjectName(u"NMN01Label")
        self.NMN01Label.setFont(font3)

        self.horizontalLayout_21.addWidget(self.NMN01Label)

        self.NMN01Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.NMN01Spacer)

        self.NMN01LineE = QLineEdit(self.NMN01F)
        self.NMN01LineE.setObjectName(u"NMN01LineE")
        self.NMN01LineE.setMinimumSize(QSize(200, 30))
        self.NMN01LineE.setFont(font4)
        self.NMN01LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NMN01LineE.setClearButtonEnabled(True)

        self.horizontalLayout_21.addWidget(self.NMN01LineE)

        self.horizontalLayout_20.addWidget(self.NMN01F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_7.addWidget(self.NM01F)

        self.NM02F = QGroupBox(self.NitrogenFrame)
        self.NM02F.setObjectName(u"NM02F")
        self.horizontalLayout_22 = QHBoxLayout(self.NM02F)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.NMN02F = QFrame(self.NM02F)
        self.NMN02F.setObjectName(u"NMN02F")
        self.NMN02F.setFrameShape(QFrame.Shape.NoFrame)
        self.NMN02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.NMN02F)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.NMN02Label = QLabel(self.NMN02F)
        self.NMN02Label.setObjectName(u"NMN02Label")
        self.NMN02Label.setFont(font3)

        self.horizontalLayout_23.addWidget(self.NMN02Label)

        self.NMN02Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.NMN02Spacer)

        self.NMN02FLineE = QLineEdit(self.NMN02F)
        self.NMN02FLineE.setObjectName(u"NMN02FLineE")
        self.NMN02FLineE.setMinimumSize(QSize(200, 30))
        self.NMN02FLineE.setFont(font4)
        self.NMN02FLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NMN02FLineE.setClearButtonEnabled(True)

        self.horizontalLayout_23.addWidget(self.NMN02FLineE)

        self.horizontalLayout_22.addWidget(self.NMN02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_7.addWidget(self.NM02F)

        self.NM03F = QGroupBox(self.NitrogenFrame)
        self.NM03F.setObjectName(u"NM03F")
        self.horizontalLayout_24 = QHBoxLayout(self.NM03F)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.NMN03F = QFrame(self.NM03F)
        self.NMN03F.setObjectName(u"NMN03F")
        self.NMN03F.setFrameShape(QFrame.Shape.NoFrame)
        self.NMN03F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.NMN03F)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.NMN03Label = QLabel(self.NMN03F)
        self.NMN03Label.setObjectName(u"NMN03Label")
        self.NMN03Label.setFont(font3)

        self.horizontalLayout_25.addWidget(self.NMN03Label)

        self.NMN03Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.NMN03Spacer)

        self.NMN03LineE = QLineEdit(self.NMN03F)
        self.NMN03LineE.setObjectName(u"NMN03LineE")
        self.NMN03LineE.setMinimumSize(QSize(200, 30))
        self.NMN03LineE.setFont(font4)
        self.NMN03LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.NMN03LineE.setClearButtonEnabled(True)

        self.horizontalLayout_25.addWidget(self.NMN03LineE)

        self.horizontalLayout_24.addWidget(self.NMN03F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_7.addWidget(self.NM03F)

        self.verticalLayout_8.addWidget(self.NitrogenFrame)

        self.STQDATA.addWidget(self.NitrogenP)
        self.MoistureP = QWidget()
        self.MoistureP.setObjectName(u"MoistureP")
        self.verticalLayout_6 = QVBoxLayout(self.MoistureP)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.MoistureFrame = QFrame(self.MoistureP)
        self.MoistureFrame.setObjectName(u"MoistureFrame")
        self.MoistureFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.MoistureFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MoistureFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MoisturTF = QFrame(self.MoistureFrame)
        self.MoisturTF.setObjectName(u"MoisturTF")
        self.MoisturTF.setFrameShape(QFrame.Shape.Box)
        self.MoisturTF.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.MoisturTF)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.MTitleFrame = QLabel(self.MoisturTF)
        self.MTitleFrame.setObjectName(u"MTitleFrame")
        self.MTitleFrame.setFont(font2)

        self.horizontalLayout_12.addWidget(self.MTitleFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5.addWidget(self.MoisturTF)

        self.MM01F = QGroupBox(self.MoistureFrame)
        self.MM01F.setObjectName(u"MM01F")
        self.horizontalLayout_13 = QHBoxLayout(self.MM01F)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.MMM01F = QFrame(self.MM01F)
        self.MMM01F.setObjectName(u"MMM01F")
        self.MMM01F.setFrameShape(QFrame.Shape.NoFrame)
        self.MMM01F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.MMM01F)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.MMM01Label = QLabel(self.MMM01F)
        self.MMM01Label.setObjectName(u"MMM01Label")
        self.MMM01Label.setFont(font3)

        self.horizontalLayout_14.addWidget(self.MMM01Label)

        self.MMM01Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.MMM01Spacer)

        self.MMM01LineE = QLineEdit(self.MMM01F)
        self.MMM01LineE.setObjectName(u"MMM01LineE")
        self.MMM01LineE.setMinimumSize(QSize(200, 30))
        self.MMM01LineE.setFont(font4)
        self.MMM01LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MMM01LineE.setClearButtonEnabled(True)

        self.horizontalLayout_14.addWidget(self.MMM01LineE)

        self.horizontalLayout_13.addWidget(self.MMM01F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5.addWidget(self.MM01F)

        self.MM02F = QGroupBox(self.MoistureFrame)
        self.MM02F.setObjectName(u"MM02F")
        self.horizontalLayout_15 = QHBoxLayout(self.MM02F)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.MMM02F = QFrame(self.MM02F)
        self.MMM02F.setObjectName(u"MMM02F")
        self.MMM02F.setFrameShape(QFrame.Shape.NoFrame)
        self.MMM02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.MMM02F)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.MMM02Label = QLabel(self.MMM02F)
        self.MMM02Label.setObjectName(u"MMM02Label")
        self.MMM02Label.setFont(font3)

        self.horizontalLayout_16.addWidget(self.MMM02Label)

        self.MMM02Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.MMM02Spacer)

        self.MMM02FLineE = QLineEdit(self.MMM02F)
        self.MMM02FLineE.setObjectName(u"MMM02FLineE")
        self.MMM02FLineE.setMinimumSize(QSize(200, 30))
        self.MMM02FLineE.setFont(font4)
        self.MMM02FLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MMM02FLineE.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.MMM02FLineE)

        self.horizontalLayout_15.addWidget(self.MMM02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5.addWidget(self.MM02F)

        self.MM03F = QGroupBox(self.MoistureFrame)
        self.MM03F.setObjectName(u"MM03F")
        self.horizontalLayout_17 = QHBoxLayout(self.MM03F)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.MMM03F = QFrame(self.MM03F)
        self.MMM03F.setObjectName(u"MMM03F")
        self.MMM03F.setFrameShape(QFrame.Shape.NoFrame)
        self.MMM03F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.MMM03F)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.MMM03Label = QLabel(self.MMM03F)
        self.MMM03Label.setObjectName(u"MMM03Label")
        self.MMM03Label.setFont(font3)

        self.horizontalLayout_18.addWidget(self.MMM03Label)

        self.MMM03Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.MMM03Spacer)

        self.MMM03LineE = QLineEdit(self.MMM03F)
        self.MMM03LineE.setObjectName(u"MMM03LineE")
        self.MMM03LineE.setMinimumSize(QSize(200, 30))
        self.MMM03LineE.setFont(font4)
        self.MMM03LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MMM03LineE.setClearButtonEnabled(True)

        self.horizontalLayout_18.addWidget(self.MMM03LineE)

        self.horizontalLayout_17.addWidget(self.MMM03F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5.addWidget(self.MM03F)

        self.verticalLayout_6.addWidget(self.MoistureFrame)

        self.STQDATA.addWidget(self.MoistureP)
        self.TargetP = QWidget()
        self.TargetP.setObjectName(u"TargetP")
        self.verticalLayout_10 = QVBoxLayout(self.TargetP)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.TargetFrame = QFrame(self.TargetP)
        self.TargetFrame.setObjectName(u"TargetFrame")
        self.TargetFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.TargetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.TargetFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.TargetTF = QFrame(self.TargetFrame)
        self.TargetTF.setObjectName(u"TargetTF")
        self.TargetTF.setFrameShape(QFrame.Shape.Box)
        self.TargetTF.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_26 = QHBoxLayout(self.TargetTF)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.TargetTitleFrame = QLabel(self.TargetTF)
        self.TargetTitleFrame.setObjectName(u"TargetTitleFrame")
        self.TargetTitleFrame.setFont(font2)

        self.horizontalLayout_26.addWidget(self.TargetTitleFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_9.addWidget(self.TargetTF)

        self.CNR01 = QGroupBox(self.TargetFrame)
        self.CNR01.setObjectName(u"CNR01")
        self.horizontalLayout_27 = QHBoxLayout(self.CNR01)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.CN01F = QFrame(self.CNR01)
        self.CN01F.setObjectName(u"CN01F")
        self.CN01F.setFrameShape(QFrame.Shape.NoFrame)
        self.CN01F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.CN01F)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.CN01Label = QLabel(self.CN01F)
        self.CN01Label.setObjectName(u"CN01Label")
        self.CN01Label.setFont(font3)

        self.horizontalLayout_28.addWidget(self.CN01Label)

        self.CN01Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.CN01Spacer)

        self.CN01LineE = QLineEdit(self.CN01F)
        self.CN01LineE.setObjectName(u"CN01LineE")
        self.CN01LineE.setMinimumSize(QSize(200, 30))
        self.CN01LineE.setFont(font4)
        self.CN01LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CN01LineE.setClearButtonEnabled(True)

        self.horizontalLayout_28.addWidget(self.CN01LineE)

        self.horizontalLayout_27.addWidget(self.CN01F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_9.addWidget(self.CNR01)

        self.MCC02F = QGroupBox(self.TargetFrame)
        self.MCC02F.setObjectName(u"MCC02F")
        self.horizontalLayout_29 = QHBoxLayout(self.MCC02F)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.MC02F = QFrame(self.MCC02F)
        self.MC02F.setObjectName(u"MC02F")
        self.MC02F.setFrameShape(QFrame.Shape.NoFrame)
        self.MC02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.MC02F)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.MC02Label = QLabel(self.MC02F)
        self.MC02Label.setObjectName(u"MC02Label")
        self.MC02Label.setFont(font3)

        self.horizontalLayout_30.addWidget(self.MC02Label)

        self.MC02Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.MC02Spacer)

        self.MC02FLineE = QLineEdit(self.MC02F)
        self.MC02FLineE.setObjectName(u"MC02FLineE")
        self.MC02FLineE.setMinimumSize(QSize(200, 30))
        self.MC02FLineE.setFont(font4)
        self.MC02FLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MC02FLineE.setClearButtonEnabled(True)

        self.horizontalLayout_30.addWidget(self.MC02FLineE)

        self.horizontalLayout_29.addWidget(self.MC02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_9.addWidget(self.MCC02F)

        self.WtC03F = QGroupBox(self.TargetFrame)
        self.WtC03F.setObjectName(u"WtC03F")
        self.horizontalLayout_31 = QHBoxLayout(self.WtC03F)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.Wt03F = QFrame(self.WtC03F)
        self.Wt03F.setObjectName(u"Wt03F")
        self.Wt03F.setFrameShape(QFrame.Shape.NoFrame)
        self.Wt03F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.Wt03F)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.Wt03Label = QLabel(self.Wt03F)
        self.Wt03Label.setObjectName(u"Wt03Label")
        self.Wt03Label.setFont(font3)

        self.horizontalLayout_32.addWidget(self.Wt03Label)

        self.Wt03Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.Wt03Spacer)

        self.Wt03LineE = QLineEdit(self.Wt03F)
        self.Wt03LineE.setObjectName(u"Wt03LineE")
        self.Wt03LineE.setMinimumSize(QSize(200, 30))
        self.Wt03LineE.setFont(font4)
        self.Wt03LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Wt03LineE.setClearButtonEnabled(True)

        self.horizontalLayout_32.addWidget(self.Wt03LineE)

        self.horizontalLayout_31.addWidget(self.Wt03F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_9.addWidget(self.WtC03F)

        self.verticalLayout_10.addWidget(self.TargetFrame)

        self.STQDATA.addWidget(self.TargetP)

        self.horizontalLayout_4.addWidget(self.STQDATA)

        self.horizontalLayout_2.addWidget(self.DataF)

        self.line = QFrame(self.Body)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_2.addWidget(self.line)

        self.ViewRFrame = QFrame(self.Body)
        self.ViewRFrame.setObjectName(u"ViewRFrame")
        self.ViewRFrame.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.ViewRFrame.sizePolicy().hasHeightForWidth())
        self.ViewRFrame.setSizePolicy(sizePolicy2)
        self.ViewRFrame.setMaximumSize(QSize(700, 16777215))
        self.ViewRFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.ViewRFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.ViewRFrame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.ViewPFrame = QFrame(self.ViewRFrame)
        self.ViewPFrame.setObjectName(u"ViewPFrame")
        self.ViewPFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.ViewPFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.ViewPFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ViewPTF = QFrame(self.ViewPFrame)
        self.ViewPTF.setObjectName(u"ViewPTF")
        self.ViewPTF.setFrameShape(QFrame.Shape.Box)
        self.ViewPTF.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_47 = QHBoxLayout(self.ViewPTF)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.ViewPTitleFrame = QLabel(self.ViewPTF)
        self.ViewPTitleFrame.setObjectName(u"ViewPTitleFrame")
        self.ViewPTitleFrame.setFont(font2)

        self.horizontalLayout_47.addWidget(self.ViewPTitleFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_14.addWidget(self.ViewPTF)

        self.FeedSChFBox = QGroupBox(self.ViewPFrame)
        self.FeedSChFBox.setObjectName(u"FeedSChFBox")
        self.FeedSChFBox.setFont(font3)
        self.FeedSChFBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.FeedSChFBox.setFlat(False)
        self.FeedSChFBox.setCheckable(True)
        self.FeedSChFBox.setChecked(False)
        self.verticalLayout_16 = QVBoxLayout(self.FeedSChFBox)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.Feed01F = QGroupBox(self.FeedSChFBox)
        self.Feed01F.setObjectName(u"Feed01F")
        self.Feed01F.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed01F.setFlat(True)
        self.horizontalLayout_48 = QHBoxLayout(self.Feed01F)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.Feed01CF = QFrame(self.Feed01F)
        self.Feed01CF.setObjectName(u"Feed01CF")
        self.Feed01CF.setFrameShape(QFrame.Shape.NoFrame)
        self.Feed01CF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.Feed01CF)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.Feed01CLabel = QLabel(self.Feed01CF)
        self.Feed01CLabel.setObjectName(u"Feed01CLabel")
        self.Feed01CLabel.setFont(font3)

        self.horizontalLayout_49.addWidget(self.Feed01CLabel)

        self.Feed01CSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.Feed01CSpacer)

        self.Feed01CLineE = QLineEdit(self.Feed01CF)
        self.Feed01CLineE.setObjectName(u"Feed01CLineE")
        self.Feed01CLineE.setEnabled(True)
        self.Feed01CLineE.setMinimumSize(QSize(100, 30))
        self.Feed01CLineE.setFont(font3)
        self.Feed01CLineE.setFrame(True)
        self.Feed01CLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed01CLineE.setDragEnabled(True)
        self.Feed01CLineE.setReadOnly(False)
        self.Feed01CLineE.setClearButtonEnabled(False)

        self.horizontalLayout_49.addWidget(self.Feed01CLineE)

        self.horizontalLayout_48.addWidget(self.Feed01CF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Feed01NLine01 = QFrame(self.Feed01F)
        self.Feed01NLine01.setObjectName(u"Feed01NLine01")
        self.Feed01NLine01.setFrameShadow(QFrame.Shadow.Plain)
        self.Feed01NLine01.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_48.addWidget(self.Feed01NLine01)

        self.Feed01NF = QFrame(self.Feed01F)
        self.Feed01NF.setObjectName(u"Feed01NF")
        self.Feed01NF.setFrameShape(QFrame.Shape.NoFrame)
        self.Feed01NF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.Feed01NF)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.Feed01NLabel = QLabel(self.Feed01NF)
        self.Feed01NLabel.setObjectName(u"Feed01NLabel")
        self.Feed01NLabel.setFont(font3)

        self.horizontalLayout_57.addWidget(self.Feed01NLabel)

        self.Feed01NSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.Feed01NSpacer)

        self.Feed01NLineE = QLineEdit(self.Feed01NF)
        self.Feed01NLineE.setObjectName(u"Feed01NLineE")
        self.Feed01NLineE.setMinimumSize(QSize(100, 30))
        self.Feed01NLineE.setFont(font3)
        self.Feed01NLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed01NLineE.setDragEnabled(True)
        self.Feed01NLineE.setReadOnly(False)
        self.Feed01NLineE.setClearButtonEnabled(False)

        self.horizontalLayout_57.addWidget(self.Feed01NLineE)

        self.horizontalLayout_48.addWidget(self.Feed01NF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Feed01Line02 = QFrame(self.Feed01F)
        self.Feed01Line02.setObjectName(u"Feed01Line02")
        self.Feed01Line02.setFrameShadow(QFrame.Shadow.Plain)
        self.Feed01Line02.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_48.addWidget(self.Feed01Line02)

        self.Feed01MCF = QFrame(self.Feed01F)
        self.Feed01MCF.setObjectName(u"Feed01MCF")
        self.Feed01MCF.setFrameShape(QFrame.Shape.NoFrame)
        self.Feed01MCF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.Feed01MCF)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.Feed01MCLabel = QLabel(self.Feed01MCF)
        self.Feed01MCLabel.setObjectName(u"Feed01MCLabel")
        self.Feed01MCLabel.setFont(font3)

        self.horizontalLayout_56.addWidget(self.Feed01MCLabel)

        self.Feed01MCSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.Feed01MCSpacer)

        self.Feed01MCLineE = QLineEdit(self.Feed01MCF)
        self.Feed01MCLineE.setObjectName(u"Feed01MCLineE")
        self.Feed01MCLineE.setMinimumSize(QSize(100, 30))
        self.Feed01MCLineE.setFont(font3)
        self.Feed01MCLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed01MCLineE.setDragEnabled(True)
        self.Feed01MCLineE.setReadOnly(False)
        self.Feed01MCLineE.setClearButtonEnabled(False)

        self.horizontalLayout_56.addWidget(self.Feed01MCLineE)

        self.horizontalLayout_48.addWidget(self.Feed01MCF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_16.addWidget(self.Feed01F)

        self.Feed02F = QGroupBox(self.FeedSChFBox)
        self.Feed02F.setObjectName(u"Feed02F")
        self.Feed02F.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed02F.setFlat(True)
        self.horizontalLayout_50 = QHBoxLayout(self.Feed02F)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.FeedC02F = QFrame(self.Feed02F)
        self.FeedC02F.setObjectName(u"FeedC02F")
        self.FeedC02F.setFrameShape(QFrame.Shape.NoFrame)
        self.FeedC02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.FeedC02F)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.Feed02Label = QLabel(self.FeedC02F)
        self.Feed02Label.setObjectName(u"Feed02Label")
        self.Feed02Label.setFont(font3)

        self.horizontalLayout_51.addWidget(self.Feed02Label)

        self.Feed02Spacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.Feed02Spacer)

        self.Feed02CLineE = QLineEdit(self.FeedC02F)
        self.Feed02CLineE.setObjectName(u"Feed02CLineE")
        self.Feed02CLineE.setMinimumSize(QSize(100, 30))
        self.Feed02CLineE.setFont(font3)
        self.Feed02CLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed02CLineE.setDragEnabled(True)
        self.Feed02CLineE.setReadOnly(False)

        self.horizontalLayout_51.addWidget(self.Feed02CLineE)

        self.horizontalLayout_50.addWidget(self.FeedC02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Feed02NLine01 = QFrame(self.Feed02F)
        self.Feed02NLine01.setObjectName(u"Feed02NLine01")
        self.Feed02NLine01.setFrameShadow(QFrame.Shadow.Plain)
        self.Feed02NLine01.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_50.addWidget(self.Feed02NLine01)

        self.FeedN02F = QFrame(self.Feed02F)
        self.FeedN02F.setObjectName(u"FeedN02F")
        self.FeedN02F.setFrameShape(QFrame.Shape.NoFrame)
        self.FeedN02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.FeedN02F)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.Feed02NLabel = QLabel(self.FeedN02F)
        self.Feed02NLabel.setObjectName(u"Feed02NLabel")
        self.Feed02NLabel.setFont(font3)

        self.horizontalLayout_59.addWidget(self.Feed02NLabel)

        self.Feed02NSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.Feed02NSpacer)

        self.Feed02NLineE = QLineEdit(self.FeedN02F)
        self.Feed02NLineE.setObjectName(u"Feed02NLineE")
        self.Feed02NLineE.setMinimumSize(QSize(100, 30))
        self.Feed02NLineE.setFont(font3)
        self.Feed02NLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed02NLineE.setDragEnabled(True)
        self.Feed02NLineE.setReadOnly(False)

        self.horizontalLayout_59.addWidget(self.Feed02NLineE)

        self.horizontalLayout_50.addWidget(self.FeedN02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Feed02NLine02 = QFrame(self.Feed02F)
        self.Feed02NLine02.setObjectName(u"Feed02NLine02")
        self.Feed02NLine02.setFrameShadow(QFrame.Shadow.Plain)
        self.Feed02NLine02.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_50.addWidget(self.Feed02NLine02)

        self.FeedMC02F = QFrame(self.Feed02F)
        self.FeedMC02F.setObjectName(u"FeedMC02F")
        self.FeedMC02F.setFrameShape(QFrame.Shape.NoFrame)
        self.FeedMC02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.FeedMC02F)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.Feed02MCLabel = QLabel(self.FeedMC02F)
        self.Feed02MCLabel.setObjectName(u"Feed02MCLabel")
        self.Feed02MCLabel.setFont(font3)

        self.horizontalLayout_58.addWidget(self.Feed02MCLabel)

        self.Feed02MCSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_58.addItem(self.Feed02MCSpacer)

        self.Feed02MCLineE = QLineEdit(self.FeedMC02F)
        self.Feed02MCLineE.setObjectName(u"Feed02MCLineE")
        self.Feed02MCLineE.setMinimumSize(QSize(100, 30))
        self.Feed02MCLineE.setFont(font3)
        self.Feed02MCLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed02MCLineE.setDragEnabled(True)
        self.Feed02MCLineE.setReadOnly(False)

        self.horizontalLayout_58.addWidget(self.Feed02MCLineE)

        self.horizontalLayout_50.addWidget(self.FeedMC02F, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_16.addWidget(self.Feed02F)

        self.Feed03F = QGroupBox(self.FeedSChFBox)
        self.Feed03F.setObjectName(u"Feed03F")
        self.Feed03F.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed03F.setFlat(True)
        self.horizontalLayout_54 = QHBoxLayout(self.Feed03F)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.Feed03CF = QFrame(self.Feed03F)
        self.Feed03CF.setObjectName(u"Feed03CF")
        self.Feed03CF.setFrameShape(QFrame.Shape.NoFrame)
        self.Feed03CF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.Feed03CF)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.Feed03CLabel = QLabel(self.Feed03CF)
        self.Feed03CLabel.setObjectName(u"Feed03CLabel")
        self.Feed03CLabel.setFont(font3)

        self.horizontalLayout_55.addWidget(self.Feed03CLabel)

        self.Feed03CSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.Feed03CSpacer)

        self.Feed03CLineE = QLineEdit(self.Feed03CF)
        self.Feed03CLineE.setObjectName(u"Feed03CLineE")
        self.Feed03CLineE.setMinimumSize(QSize(100, 30))
        self.Feed03CLineE.setFont(font3)
        self.Feed03CLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed03CLineE.setDragEnabled(True)
        self.Feed03CLineE.setReadOnly(False)

        self.horizontalLayout_55.addWidget(self.Feed03CLineE)

        self.horizontalLayout_54.addWidget(self.Feed03CF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Feed03Line01 = QFrame(self.Feed03F)
        self.Feed03Line01.setObjectName(u"Feed03Line01")
        self.Feed03Line01.setFrameShadow(QFrame.Shadow.Plain)
        self.Feed03Line01.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_54.addWidget(self.Feed03Line01)

        self.Feed03MCF = QFrame(self.Feed03F)
        self.Feed03MCF.setObjectName(u"Feed03MCF")
        self.Feed03MCF.setFrameShape(QFrame.Shape.NoFrame)
        self.Feed03MCF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.Feed03MCF)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.Feed03MCLabel = QLabel(self.Feed03MCF)
        self.Feed03MCLabel.setObjectName(u"Feed03MCLabel")
        self.Feed03MCLabel.setFont(font3)

        self.horizontalLayout_61.addWidget(self.Feed03MCLabel)

        self.Feed03MCSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.Feed03MCSpacer)

        self.Feed03NLineE = QLineEdit(self.Feed03MCF)
        self.Feed03NLineE.setObjectName(u"Feed03NLineE")
        self.Feed03NLineE.setMinimumSize(QSize(100, 30))
        self.Feed03NLineE.setFont(font3)
        self.Feed03NLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed03NLineE.setDragEnabled(True)
        self.Feed03NLineE.setReadOnly(False)

        self.horizontalLayout_61.addWidget(self.Feed03NLineE)

        self.horizontalLayout_54.addWidget(self.Feed03MCF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.Feed03Line02 = QFrame(self.Feed03F)
        self.Feed03Line02.setObjectName(u"Feed03Line02")
        self.Feed03Line02.setFrameShadow(QFrame.Shadow.Plain)
        self.Feed03Line02.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_54.addWidget(self.Feed03Line02)

        self.Feed03NF = QFrame(self.Feed03F)
        self.Feed03NF.setObjectName(u"Feed03NF")
        self.Feed03NF.setFrameShape(QFrame.Shape.NoFrame)
        self.Feed03NF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.Feed03NF)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.Feed03NLabel = QLabel(self.Feed03NF)
        self.Feed03NLabel.setObjectName(u"Feed03NLabel")
        self.Feed03NLabel.setFont(font3)

        self.horizontalLayout_60.addWidget(self.Feed03NLabel)

        self.Feed03NSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.Feed03NSpacer)

        self.Feed03MCLineE = QLineEdit(self.Feed03NF)
        self.Feed03MCLineE.setObjectName(u"Feed03MCLineE")
        self.Feed03MCLineE.setMinimumSize(QSize(100, 30))
        self.Feed03MCLineE.setFont(font3)
        self.Feed03MCLineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Feed03MCLineE.setDragEnabled(True)
        self.Feed03MCLineE.setReadOnly(False)

        self.horizontalLayout_60.addWidget(self.Feed03MCLineE)

        self.horizontalLayout_54.addWidget(self.Feed03NF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_16.addWidget(self.Feed03F)

        self.verticalLayout_14.addWidget(self.FeedSChFBox)

        self.line_9 = QFrame(self.ViewPFrame)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_9)

        self.VWP03F = QGroupBox(self.ViewPFrame)
        self.VWP03F.setObjectName(u"VWP03F")
        self.VWP03F.setFont(font3)
        self.VWP03F.setFlat(False)
        self.verticalLayout_18 = QVBoxLayout(self.VWP03F)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.VWPrrF = QFrame(self.VWP03F)
        self.VWPrrF.setObjectName(u"VWPrrF")
        self.VWPrrF.setFrameShape(QFrame.Shape.StyledPanel)
        self.VWPrrF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.VWPrrF)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.VWPT01F = QFrame(self.VWPrrF)
        self.VWPT01F.setObjectName(u"VWPT01F")
        self.VWPT01F.setFrameShape(QFrame.Shape.NoFrame)
        self.VWPT01F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.VWPT01F)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.VWP01Label = QLabel(self.VWPT01F)
        self.VWP01Label.setObjectName(u"VWP01Label")
        self.VWP01Label.setFont(font3)

        self.horizontalLayout_63.addWidget(self.VWP01Label)

        self.VWP01Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.VWP01Spacer)

        self.VWP01LineE = QLineEdit(self.VWPT01F)
        self.VWP01LineE.setObjectName(u"VWP01LineE")
        self.VWP01LineE.setMinimumSize(QSize(100, 30))
        self.VWP01LineE.setFont(font3)
        self.VWP01LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VWP01LineE.setReadOnly(True)

        self.horizontalLayout_63.addWidget(self.VWP01LineE)

        self.horizontalLayout_52.addWidget(self.VWPT01F)

        self.VWPT02F = QFrame(self.VWPrrF)
        self.VWPT02F.setObjectName(u"VWPT02F")
        self.VWPT02F.setFrameShape(QFrame.Shape.NoFrame)
        self.VWPT02F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.VWPT02F)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.VWP02Label = QLabel(self.VWPT02F)
        self.VWP02Label.setObjectName(u"VWP02Label")
        self.VWP02Label.setFont(font3)

        self.horizontalLayout_53.addWidget(self.VWP02Label)

        self.VWP2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.VWP2Spacer)

        self.VWP02LineE = QLineEdit(self.VWPT02F)
        self.VWP02LineE.setObjectName(u"VWP02LineE")
        self.VWP02LineE.setMinimumSize(QSize(100, 30))
        self.VWP02LineE.setFont(font3)
        self.VWP02LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VWP02LineE.setReadOnly(True)

        self.horizontalLayout_53.addWidget(self.VWP02LineE)

        self.horizontalLayout_52.addWidget(self.VWPT02F)

        self.VWPT03F = QFrame(self.VWPrrF)
        self.VWPT03F.setObjectName(u"VWPT03F")
        self.VWPT03F.setEnabled(True)
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.VWPT03F.setFont(font5)
        self.VWPT03F.setFrameShape(QFrame.Shape.NoFrame)
        self.VWPT03F.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.VWPT03F)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.VWP03Label = QLabel(self.VWPT03F)
        self.VWP03Label.setObjectName(u"VWP03Label")
        self.VWP03Label.setFont(font3)

        self.horizontalLayout_62.addWidget(self.VWP03Label)

        self.VWP03Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.VWP03Spacer)

        self.VWP03LineE = QLineEdit(self.VWPT03F)
        self.VWP03LineE.setObjectName(u"VWP03LineE")
        self.VWP03LineE.setMinimumSize(QSize(100, 30))
        self.VWP03LineE.setFont(font3)
        self.VWP03LineE.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.VWP03LineE.setReadOnly(True)

        self.horizontalLayout_62.addWidget(self.VWP03LineE)

        self.horizontalLayout_52.addWidget(self.VWPT03F)

        self.verticalLayout_18.addWidget(self.VWPrrF)

        self.ResultF = QFrame(self.VWP03F)
        self.ResultF.setObjectName(u"ResultF")
        self.ResultF.setFrameShape(QFrame.Shape.StyledPanel)
        self.ResultF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.ResultF)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.ResultLLF = QFrame(self.ResultF)
        self.ResultLLF.setObjectName(u"ResultLLF")
        self.ResultLLF.setFrameShape(QFrame.Shape.NoFrame)
        self.ResultLLF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.ResultLLF)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ResultLineE = QPlainTextEdit(self.ResultLLF)
        self.ResultLineE.setObjectName(u"ResultLineE")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ResultLineE.sizePolicy().hasHeightForWidth())
        self.ResultLineE.setSizePolicy(sizePolicy4)
        self.ResultLineE.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.ResultLineE.setFont(font6)
        self.ResultLineE.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

        self.verticalLayout_19.addWidget(self.ResultLineE)

        self.horizontalLayout_69.addWidget(self.ResultLLF)

        self.RounDFrame = QFrame(self.ResultF)
        self.RounDFrame.setObjectName(u"RounDFrame")
        self.RounDFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.RounDFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.RounDFrame)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.RounDspinBox = QSpinBox(self.RounDFrame)
        self.RounDspinBox.setObjectName(u"RounDspinBox")
        self.RounDspinBox.setMinimumSize(QSize(60, 40))
        self.RounDspinBox.setFont(font3)
        self.RounDspinBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_68.addWidget(self.RounDspinBox)

        self.horizontalLayout_69.addWidget(self.RounDFrame)

        self.verticalLayout_18.addWidget(self.ResultF)

        self.verticalLayout_14.addWidget(self.VWP03F)

        self.verticalLayout_17.addWidget(self.ViewPFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.ViewRFrame)

        self.verticalLayout.addWidget(self.Body)

        self.ProgressFrame = QFrame(self.centralwidget)
        self.ProgressFrame.setObjectName(u"ProgressFrame")
        self.ProgressFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.ProgressFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.ProgressFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.progressBar = QProgressBar(self.ProgressFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font3)
        self.progressBar.setValue(0)

        self.verticalLayout_13.addWidget(self.progressBar)

        self.verticalLayout.addWidget(self.ProgressFrame)

        self.Foot = QFrame(self.centralwidget)
        self.Foot.setObjectName(u"Foot")
        self.Foot.setMinimumSize(QSize(0, 90))
        self.Foot.setMaximumSize(QSize(16777215, 90))
        self.Foot.setFrameShape(QFrame.Shape.StyledPanel)
        self.Foot.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Foot)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 9, 0, 9)
        self.NPF = QFrame(self.Foot)
        self.NPF.setObjectName(u"NPF")
        self.NPF.setFrameShape(QFrame.Shape.NoFrame)
        self.NPF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.NPF)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, -1, 0, -1)
        self.StartFrame = QFrame(self.NPF)
        self.StartFrame.setObjectName(u"StartFrame")
        self.StartFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.StartFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.StartFrame)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.pBStart = QPushButton(self.StartFrame)
        self.pBStart.setObjectName(u"pBStart")
        self.pBStart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Assets/Icons/Start.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBStart.setIcon(icon3)
        self.pBStart.setIconSize(QSize(30, 30))

        self.horizontalLayout_65.addWidget(self.pBStart)

        self.horizontalLayout_40.addWidget(self.StartFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.line_3 = QFrame(self.NPF)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_40.addWidget(self.line_3)

        self.NextPrevFram = QFrame(self.NPF)
        self.NextPrevFram.setObjectName(u"NextPrevFram")
        self.NextPrevFram.setFrameShape(QFrame.Shape.NoFrame)
        self.NextPrevFram.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.NextPrevFram)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.pBPrev = QPushButton(self.NextPrevFram)
        self.pBPrev.setObjectName(u"pBPrev")
        self.pBPrev.setEnabled(True)
        self.pBPrev.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Assets/Icons/Prev.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBPrev.setIcon(icon4)
        self.pBPrev.setIconSize(QSize(30, 30))

        self.horizontalLayout_64.addWidget(self.pBPrev)

        self.pBNext = QPushButton(self.NextPrevFram)
        self.pBNext.setObjectName(u"pBNext")
        self.pBNext.setEnabled(True)
        self.pBNext.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Assets/Icons/Next.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBNext.setIcon(icon5)
        self.pBNext.setIconSize(QSize(30, 30))
        self.pBNext.setAutoRepeat(False)
        self.pBNext.setAutoExclusive(False)

        self.horizontalLayout_64.addWidget(self.pBNext)

        self.horizontalLayout_40.addWidget(self.NextPrevFram)

        self.horizontalLayout_3.addWidget(self.NPF)

        self.line_2 = QFrame(self.Foot)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.CalcF = QFrame(self.Foot)
        self.CalcF.setObjectName(u"CalcF")
        self.CalcF.setFrameShape(QFrame.Shape.NoFrame)
        self.CalcF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.CalcF)
        self.horizontalLayout_41.setSpacing(6)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 9, 0, 9)
        self.CalcCF = QFrame(self.CalcF)
        self.CalcCF.setObjectName(u"CalcCF")
        self.CalcCF.setFrameShape(QFrame.Shape.NoFrame)
        self.CalcCF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.CalcCF)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.pBCalc = QPushButton(self.CalcCF)
        self.pBCalc.setObjectName(u"pBCalc")
        self.pBCalc.setEnabled(True)
        self.pBCalc.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Assets/Icons/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBCalc.setIcon(icon6)
        self.pBCalc.setIconSize(QSize(30, 30))

        self.horizontalLayout_67.addWidget(self.pBCalc)

        self.horizontalLayout_41.addWidget(self.CalcCF)

        self.line_4 = QFrame(self.CalcF)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_41.addWidget(self.line_4)

        self.ResExpdF = QFrame(self.CalcF)
        self.ResExpdF.setObjectName(u"ResExpdF")
        self.ResExpdF.setFrameShape(QFrame.Shape.NoFrame)
        self.ResExpdF.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.ResExpdF)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.pBRestart = QPushButton(self.ResExpdF)
        self.pBRestart.setObjectName(u"pBRestart")
        self.pBRestart.setEnabled(True)
        self.pBRestart.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Assets/Icons/Restart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pBRestart.setIcon(icon7)
        self.pBRestart.setIconSize(QSize(30, 30))

        self.horizontalLayout_66.addWidget(self.pBRestart)

        self.horizontalLayout_41.addWidget(self.ResExpdF, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3.addWidget(self.CalcF)

        self.verticalLayout.addWidget(self.Foot, 0, Qt.AlignmentFlag.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.STQDATA.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setStyleSheet(u"QMainWindow#centralwidget{\n"
                                 u"    border-radius: 15px;\n"
                                 "}\n"
                                 u"QWidget#centralwidget {\n"
                                 u"    border-radius: 15px;\n"
                                 u"background-color: #1e1e1e;\n"
                                 " \n"
                                 "    }\n"
                                 "\n"
                                 "\n"
                                 u"QFrame#Header, QFrame#WindowF{\n"
                                 "    border-top-right-radius: 15px;\n"
                                 "    }\n"
                                 "\n"
                                 u"QFrame#LogoFF, QFrame#FeatureF{\n"
                                 "    border-top-left-radius: 15px;\n"
                                 "    }\n"
                                 u"QFrame#Foot,QFrame#CalcF,QFrame#NPF{\n"
                                 "    border-bottom-right-radius: 15px;\n"
                                 "    border-bottom-left-radius: 15px;\n"
                                 "    }")
        # setupUi
        self.__langchanged()
        self.ChLangFcomboBox.currentTextChanged.connect(self.__langchanged)

    def __langchanged(self, lang=None):
        import json
        with open('Assets/translations.json', 'r', encoding='utf-8') as file:
            translations = json.load(file)

        language = lang
        if not lang:
            language = QLocale.system().name()
            if language not in translations:
                language = "en_US"  # Default language

        translation = translations[language]

        self.ChLangFLabel.setText(translation["Language"])
        self.ChLangFcomboBox.setItemText(0, "ar_Ar")
        self.ChLangFcomboBox.setItemText(1, "fr_FR")
        self.ChLangFcomboBox.setItemText(2, "en_US")
        self.ChLangFcomboBox.setItemText(3, "zh_CN")

        self.labeLogol.setText("")
        self.TITLEMAIN.setText(translation["Compost Recipe Calculator"])
        self.pbInf.setText("")
        self.pBMin.setText("")
        self.pBClose.setText("")
        self.Image.setText("")
        self.NameMTitleFrame.setText(translation["Names"])
        self.NameMC01F.setTitle("")
        self.NameM01Label.setText(translation["M01"])
        self.NameM01LineE.setPlaceholderText(translation["FeedStock 01"])
        self.NameMC02F.setTitle("")
        self.NameM02Label.setText(translation["M02"])
        self.NameM02FLineE.setPlaceholderText(translation["FeedStock 02"])
        self.NameMC03F.setTitle("")
        self.NameM03Label.setText(translation["M03"])
        self.NameM03LineE.setPlaceholderText(translation["FeedStock 03"])
        self.CTitleFrame.setText(translation["Carbon Source Material"])
        self.CM01F.setTitle("")
        self.CMC01Label.setText(translation["M01"])
        self.CMC01LineE.setPlaceholderText(translation["Carbon Concentration 01"])
        self.CM02F.setTitle("")
        self.CMC02Label.setText(translation["M02"])
        self.CMC02FLineE.setPlaceholderText(translation["Carbon Concentration 02"])
        self.CM03F.setTitle("")
        self.CMC03Label.setText(translation["M03"])
        self.CMC03LineE.setPlaceholderText(translation["Carbon Concentration 03"])
        self.NTitleFrame.setText(translation["Nitrogen Content Material"])
        self.NM01F.setTitle("")
        self.NMN01Label.setText(translation["M01"])
        self.NMN01LineE.setPlaceholderText(translation["Nitrogen Concentration 01"])
        self.NM02F.setTitle("")
        self.NMN02Label.setText(translation["M02"])
        self.NMN02FLineE.setPlaceholderText(
            translation["Nitrogen Concentration 02"])
        self.NM03F.setTitle("")
        self.NMN03Label.setText(translation["M03"])
        self.NMN03LineE.setPlaceholderText(translation["Nitrogen Concentration 03"])
        self.MTitleFrame.setText(translation["Moisture Content Material"])
        self.MM01F.setTitle("")
        self.MMM01Label.setText(translation["M01"])
        self.MMM01LineE.setPlaceholderText(translation["Moisture Content 01"])
        self.MM02F.setTitle("")
        self.MMM02Label.setText(translation["M02"])
        self.MMM02FLineE.setPlaceholderText(translation["Moisture Content 02"])
        self.MM03F.setTitle("")
        self.MMM03Label.setText(translation["M03"])
        self.MMM03LineE.setPlaceholderText(translation["Moisture Content 03"])
        self.TargetTitleFrame.setText(translation["Mixture"])
        self.CNR01.setTitle("")
        self.CN01Label.setText(translation["C/N ratio"])
        self.CN01LineE.setPlaceholderText(translation["Final C/N ratio"])
        self.MCC02F.setTitle("")
        self.MC02Label.setText(translation["Moisture"])
        self.MC02FLineE.setPlaceholderText(translation["Final Moisture Content"])
        self.WtC03F.setTitle("")
        self.Wt03Label.setText(translation["Weight"])
        self.Wt03LineE.setPlaceholderText(translation["Total Weight"])
        self.ViewPTitleFrame.setText(translation["Total Weight"])
        self.FeedSChFBox.setTitle(translation["FeedStocks Characteristics"])
        self.Feed01F.setTitle(translation["FeedStock 01"])
        self.Feed01CLabel.setText(translation["C01"])
        self.Feed01CLineE.setPlaceholderText(translation["TOC 01"])
        self.Feed01NLabel.setText(translation["N01"])
        self.Feed01NLineE.setPlaceholderText(translation["TN 01"])
        self.Feed01MCLabel.setText(translation["MC01"])
        self.Feed01MCLineE.setPlaceholderText(translation["Moisture01"])
        self.Feed02F.setTitle(translation["FeedStock 02"])
        self.Feed02Label.setText(translation["C02"])
        self.Feed02CLineE.setPlaceholderText(translation["TOC 02"])
        self.Feed02NLabel.setText(translation["N02"])
        self.Feed02NLineE.setPlaceholderText(translation["TN 02"])
        self.Feed02MCLabel.setText(translation["MC02"])
        self.Feed02MCLineE.setPlaceholderText(translation["Moisture02"])
        self.Feed03F.setTitle(translation["FeedStock 03"])
        self.Feed03CLabel.setText(translation["C03"])
        self.Feed03CLineE.setPlaceholderText(translation["TOC 03"])
        self.Feed03MCLabel.setText(translation["N03"])
        self.Feed03NLineE.setPlaceholderText(translation["TN 03"])
        self.Feed03NLabel.setText(translation["MC03"])
        self.Feed03MCLineE.setPlaceholderText(translation["Moisture03"])
        self.VWP03F.setTitle(translation["recipe"])
        self.VWP01Label.setText(translation["Wt01"])
        self.VWP01LineE.setPlaceholderText(translation["Weight 01"])
        self.VWP02Label.setText(translation["Wt02"])
        self.VWP02LineE.setPlaceholderText(translation["Weight 02"])
        self.VWP03Label.setText(translation["Wt03"])
        self.VWP03LineE.setPlaceholderText(translation["Weight 03"])
        self.pBStart.setText(translation["Start"])
        self.pBPrev.setText(translation["Previous"])
        self.pBNext.setText(translation["Next"])
        self.pBCalc.setText(translation["Calculate"])
        self.pBRestart.setText(translation["Clear"])
        # retranslateUi
