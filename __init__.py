from EnglishTrainingApp.Window import Window
import sys
from PyQt5.QtWidgets import QApplication

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    run()