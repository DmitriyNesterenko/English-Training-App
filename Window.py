# -*- coding: utf-8 -*-

import random, sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLabel, QPushButton, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon

class Window(QMainWindow):

    listWords = []

    def __init__(self):
        try:
            super(Window, self).__init__()
            self.initUI()
        except Exception as exc:
            print(exc.__str__())

    def initUI(self):
        vbox = QVBoxLayout()

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Leave from app.')
        exitAction.triggered.connect(self.closeApplication)
        self.statusBar()
        self.Menu = self.menuBar()
        self.appMenu = self.Menu.addMenu('&Application')
        self.appMenu.addAction(exitAction)

        self.loadWordsLibrary()

        self.lblWord = QLabel('u' + str(random.choice(self.listWords)), self)
        self.lblWord.move(130, 50)

        self.lblTime = QLabel('00:00', self)
        self.lblTime.move(130, 70)

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(130, 100)
        self.btnStart.clicked.connect(self.startAppTimer)
        self.btnStart.minimumSizeHint()

        vbox.addStretch(1)
        vbox.addWidget(self.lblWord)
        vbox.addWidget(self.lblTime)
        vbox.addWidget(self.btnStart)

        self.newWordAction = QAction(QIcon(r"C:\Users\Dmitriy\Desktop\Resouse Images\Word-icon.png"), 'Random word', self)
        self.newWordAction.setShortcut('Ctrl+R')
        self.newWordAction.setStatusTip('Get another word for training')
        self.newWordAction.triggered.connect(self.getNewWord)

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(self.newWordAction)
        self.appMenu.addAction(self.newWordAction)

        self.setLayout(vbox)
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
        self.lblWord.setText(random.choice(self.listWords))

    def startAppTimer(self):
        pass