#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender
object.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QGridLayout,
    QPushButton, QApplication)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # Original Implimentation as in tutorial
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
        """
        # Implimentation with gridLayout
        # Defome the two push button objects
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        # Initialize grid object
        grid = QGridLayout()
        # space between grid locations
        grid.setSpacing(10)

        # populate the grid with the two button object
        grid.addWidget(btn1, 2, 1)
        grid.addWidget(btn2, 2, 2)

        # Connet the button clicking event to buttonClicked function below
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        # Initiate statusbar to display the button clicked message
        self.statusBar()

        self.setLayout(grid)
        # setGeometry(topLeft_X,topLeft_Y,Width, Height) geometry of main window.
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Event sender')
        self.show()
        """

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
