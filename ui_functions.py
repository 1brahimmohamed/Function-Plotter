# ---------------------------------------------------------
# UI Functionalities
# ---------------------------------------------------------

from PyQt5.uic.properties import QtGui

# UI file
from main import *

# Global Variables
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True


class UIFunctions(MainWindow):
    """
    Class containing all the UI functions

    ...

    Attributes
    ----------
    GLOBAL_STATE : int
        Global state of the window
    GLOBAL_TITLE_BAR : bool
        Global title bar of the window

    Methods
    -------
    maximize_restore()
        Maximize or restore the window
    returStatus()
        Return the status of the window
    setStatus(status)
        Set the status of the window
    enableMaximumSize(width, height)
        Enable the maximum size of the window
    toggleMenu(maxWidth, enable)
        Toggle the menu
    removeTitleBar(status)
        Remove the title bar
    labelTitle(text)
        Set the title of the label
    labelDescription(text)
        Set the description of the label
    addNewMenu(name, objName, icon, isTopMenu)
        Add a new menu
    selectMenu(getStyle)
        Select the menu
    setMaxMinLimitNoError(obj)
        Sets the max and min limit to no error
    setMaxMinLimitError(obj, message)
        Sets the max and min limit to error
    setFunctionStringNoError()
        Sets the function string to no error
    """

    # Global Variables
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    # UI Functions
    def maximize_restore(self):

        """
        Maximize or restore the window
        :return: None
        """

        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    def returnStatus(self):
        """
        Return the current status of the window
        :return:
        """
        return GLOBAL_STATE

    def setStatus(status):
        """
        Set the status of the window
        :return: None
        """
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enableMaximumSize(self, width, height):
        """
        Enable the maximum size of the window
        :param width: the width of the window
        :param height: the height of the window
        :return: None
        """
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def toggleMenu(self, maxWidth, enable):

        """
        function to toggle the menu side bar
        :param maxWidth: the maximum allowed width of the menu
        :param enable: enable the menu
        :return: None
        """

        if enable:
            # get the current width of the menu
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # set the width of the menu
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # side bar animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def removeTitleBar(status):

        """
        Remove the title bar of the window
        :return: None
        """

        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def labelTitle(self, text):

        """
        Set the title of the window
        :param text: window title
        :return:  None
        """
        self.ui.label_title_bar_top.setText(text)

    def addNewMenu(self, name, objName, icon, isTopMenu):

        """
        Function to add a new menu to the menu bar and application
        :param name: name of the menu
        :param objName:  object name of the menu
        :param icon:  icon of the menu
        :param isTopMenu:  is the menu a top menu
        :return:  None
        """

        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton('Menu Btn', self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.ButtonPressEvent)
        button.setStyleSheet(UIFunctions.selectMenu(button.styleSheet()))

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    def selectMenu(getStyle):
        """
        Function to select the menu and change the style of the button
        :param getStyle: get the current style of the button
        :return: select: the new style of the button
        """
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(85, 170, 255); }")
        return select

    def setMaxMinLimitNoError(self, obj):
        obj.setStyleSheet(u"QSpinBox {\n"
                          "	background-color: rgb(27, 29, 35);\n"
                          "	border-radius: 5px;\n"
                          "	border: 1px solid rgb(27, 29, 35);\n"
                          "	padding-left: 10px;\n"
                          "}\n"
                          "QSpinBox:hover {\n"
                          "	border: 2px solid rgb(64, 71, 88);\n"
                          "}\n"
                          "QSpinBox:focus {\n"
                          "	border: 2px solid rgb(91, 101, 124);\n"
                          "}")
        UIFunctions.clearErrorMessage(self)

    def setMaxMinLimitError(self, obj, message):
        obj.setStyleSheet(u"QSpinBox {\n"
                          "	background-color: rgb(27, 29, 35);\n"
                          "	border-radius: 5px;\n"
                          "	border: 1px solid red;\n"
                          "	padding-left: 10px;\n"
                          "}\n")
        UIFunctions.showErrorMessage(self,message)

    def setFunctionStringNoError(self):
        self.ui.functionString.setStyleSheet(u"QLineEdit {\n"
                                             "	background-color: rgb(27, 29, 35);\n"
                                             "	border-radius: 5px;\n"
                                             "	border: 2px solid rgb(27, 29, 35);\n"
                                             "	padding-left: 10px;\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "	border: 2px solid rgb(64, 71, 88);\n"
                                             "}\n"
                                             "QLineEdit:focus {\n"
                                             "	border: 2px solid rgb(91, 101, 124);\n"
                                             "}")
        UIFunctions.clearErrorMessage(self)

    def setFunctionStringError(self, message):
        self.ui.functionString.setStyleSheet(u"QLineEdit {\n"
                                             "	background-color: rgb(27, 29, 35);\n"
                                             "	border-radius: 5px;\n"
                                             "	border: 1px solid red;\n"
                                             "	padding-left: 10px;\n"
                                             "}\n")

        UIFunctions.showErrorMessage(self,message)

    def showErrorMessage(self, message):
        self.ui.errorLabel.setText(message)

    def clearErrorMessage(self):
        self.ui.errorLabel.setText('')

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # If the window is maximized
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        # remove title bar
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        # set window shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        # resize window
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # mimimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # maximize/restore
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # show close
        self.ui.btn_close.clicked.connect(lambda: self.close())
