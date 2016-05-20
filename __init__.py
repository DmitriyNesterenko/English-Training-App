from EnglishTrainingApp.Window import Window
import sys
from PyQt5 import QtGui, QtCore

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()