#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Trying to set up a grid of buttons and labels
with some event source work
12April2019
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QGridLayout, QLabel,
    QPushButton, QApplication)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.name1 = "1 not pressed"
        self.name2 = "2 not pressed"

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Defome the two push button objects
        self.btn1 = QPushButton("Push Button 1")
        self.btn2 = QPushButton("Push Button 2")
        # Position buttons within grid
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 1, 0)

        # Define two lables associated with the buttons
        self.lbl1 = QLabel(self.name1)
        self.lbl2 = QLabel(self.name2)
        # Position labels within grid
        self.grid.addWidget(self.lbl1, 0, 1)
        self.grid.addWidget(self.lbl2, 1, 1)

        # conntect the button click/push event to appropriate module
        self.btn1.clicked.connect(self.buttonClicked)
        self.btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.move(300, 150)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('My Buttons and Lables')
        self.show()

    def buttonClicked(self):
        # Button click event handling module
        sender = self.sender()
        print(sender.text())
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
