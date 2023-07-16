import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# import application modules
from app_modules import *


class MainWindow(QMainWindow):
    """
    Main window class
    This class defines the main driver logic for the application

    ...

    Attributes
    ----------
    figure : matplotlib.figure.Figure
        The figure object that will be used to plot the function
    canvas : matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg
        The canvas object that will be used to display the figure
    plotExists : bool
        A boolean value that indicates whether or not a plot has been created
    ui : Ui_MainWindow
        The user interface object that is created from the compiled qt designer file

    Methods
    -------
    Button()
        This function is called when a button sends a signal
    moveWindow(event)
        This function is called when the mouse is moved

    """

    def __init__(self):

        QMainWindow.__init__(self)

        # Set up the user interface from compiled qt designer file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up the plot area and add it to the layout (using matplotlib)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.plotLayout.addWidget(self.canvas)
        self.figure.set_facecolor('#272c36')
        self.plotExists = False

        # Window Attributes
        UIFunctions.removeTitleBar(True)
        UIFunctions.labelTitle(self, 'Master Micro - Function Plotter')

        # Set up Window size
        startSize = QSize(1140, 800)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        # Menu toggle button
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        # Add widget to Stacked Widget
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Function Plotter", "function_plotter_btn",
                               "url(:/16x16/icons/16x16/cil-equalizer.png)", True)

        # Set up Start page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)

        # set up the plot button to fire event
        self.ui.plotBtn.clicked.connect(self.ButtonPressEvent)

        def moveWindow(event):

            """
            This function is called when the mouse is moved
            :param event:
            :return: None
            """

            # if maximized, do not allow to move the window
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            # move window if window is normal size
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # set up the mouse move event
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        # ==> END #

        UIFunctions.uiDefinitions(self)

        # Show window
        self.show()

    def ButtonPressEvent(self):

        """
        This function is called when a button send a signal
        :return: None
        """

        # Get the clicked button
        btnWidget = self.sender()

        # call plot function if the plot button is clicked
        if btnWidget.objectName() == "plotBtn":
            Functions.plot(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def resizeEvent(self, event):
        return super(MainWindow, self).resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
