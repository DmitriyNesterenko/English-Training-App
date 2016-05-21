# -*- coding: utf-8 -*-

import random, sys
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QLabel, QPushButton,
                             QAction, QVBoxLayout, QProgressBar, QApplication,
                             QStyleFactory, QComboBox, qApp)
from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QIcon

styles = ["Plastique","Cleanlooks","CDE","Motif","GTK+"]

class Window(QMainWindow):

    global styles
    listWords = []

    def __init__(self):
        try:
            super(Window, self).__init__()
            self.initUI()
        except Exception as exc:
            print(exc.__str__())

    def initUI(self):
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(styles)
        self.comboBox.move(20, 60)
        self.comboBox.activated[str].connect(self.styleChoice)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Leave from app.')
        exitAction.triggered.connect(self.closeApplication)
        self.statusBar()
        self.Menu = self.menuBar()
        self.appMenu = self.Menu.addMenu('&Application')
        self.appMenu.addAction(exitAction)

        self.loadWordsLibrary()

        self.lblWord = QLabel('', self)
        self.lblWord.move(130, 50)
        self.getNewWord()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(130, 70, 200, 25)
        self.pbar.setMaximum(500)

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(130, 100)
        self.btnStart.clicked.connect(self.startAppTimer)
        self.btnStart.minimumSizeHint()

        newWordAction = QAction(QIcon(r"C:\Users\Dmitriy\Desktop\Resouse Images\Word-icon.png"), 'Random word', self)
        newWordAction.setShortcut('Ctrl+R')
        newWordAction.setStatusTip('Get another word for training')
        newWordAction.triggered.connect(self.getNewWord)

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(newWordAction)
        self.appMenu.addAction(newWordAction)

        # Set up the layout of our app.
        vbox = QVBoxLayout()
        vbox.addWidget(self.lblWord)
        vbox.addWidget(self.pbar)
        vbox.addWidget(self.btnStart)
        self.setLayout(vbox)

        # Set up timer.
        self.timer = QBasicTimer()
        self.time = 500

        # Set up window.
        self.setGeometry(50, 50, 320, 260)
        self.setWindowTitle('English training app')
        self.setWindowIcon(QIcon(r"C:\Users\Dmitriy\Desktop\Resouse Images\YNAB-icon.png"))

        self.show()

    def loadWordsLibrary(self):
        with open('wordsLibrary.txt', 'r') as wordLibrary:
            for word in wordLibrary.readlines():
                self.listWords.append(word)

    def closeApplication(self):
        choice = QMessageBox.question(self, 'Extract',
                                            'Do you want to exit?',
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()

    def closeEvent(self, QCloseEvent):
        choice = QMessageBox.question(self, 'Extract',
                                      'Do you want to exit?',
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def getNewWord(self):
        newWord = random.choice(self.listWords)
        self.lblWord.setText(newWord)

    def timerEvent(self, e):
        try:
            if self.time <= 0:
                self.timer.stop()
                self.lblTime.setText('00:00')
                return

            self.time -= 1
            self.pbar.setValue(self.time)
        except Exception as exc:
            print(exc.__str__())
            print(exc.__traceback__)

    def startAppTimer(self):
        try:
            if self.timer.isActive():
                self.timer.stop()
                self.btnStart.setText('Start')
            else:
                self.timer.start(300, self)
                self.btnStart.setText('Stop')
        except Exception as exc:
            print(exc.__str__())
            print(exc.__traceback__)

    def styleChoice(self, text):
        qApp.setStyle(text)

    def getStyle(self):
        return self.comboBox.currentIndex()