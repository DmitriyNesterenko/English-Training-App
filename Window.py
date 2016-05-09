import random
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    listWords = []

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 320, 260)
        self.setWindowTitle('English training app')
        self.setWindowIcon(QtGui.QIcon(r"C:\Users\Dmitriy\Desktop\Resouse Images\YNAB-icon.png"))

        self.loadWordsLibrary()
        self.home()

    def home(self):
        randomWord = random.choice(self.listWords)

        self.lblWord = QtGui.QLabel(randomWord, self)
        self.lblWord.move(130, 50)

        self.lblTime = QtGui.QLabel('00:00', self)
        self.lblTime.move(130, 70)

        self.btnStart = QtGui.QPushButton('Start', self)
        self.btnStart.move(130, 100)
        self.btnStart.clicked.connect(self.startTimer)
        self.btnStart.minimumSizeHint()

        self.show()

    def loadWordsLibrary(self):
        with open('wordsLibrary.txt', 'r') as wordLibrary:
            for word in wordLibrary.readlines():
                self.listWords.append(word)

    def startTimer(self):
        pass