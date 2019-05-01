#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a bit
more complicated window layout using
the QGridLayout manager.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        # Set up lables for entry boxes
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        
        # Set up single line entry box
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        # Set up multi-line entry box
        reviewEdit = QTextEdit()

        # Initialize grid object
        grid = QGridLayout()
        # space between grid locations
        grid.setSpacing(10)

        #Add labels and line and text edit boxes to grid
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # addWidget(reviewEdit,GritRow,GridColumn,Height,Width)
        # the Height does not seem to effect anything until high enough a number
        # (for this example is around 21) then it will extend the parent window.
        # The width parameter does not seem to behave the same way. Any value
        # greater than 1, you will the parent window does not increase in width
        # the other windows seem to start scaling down as the reviewEdit window
        # remains the same. If you use a value less than1 the reviewEdit window
        # disappears.
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        self.setLayout(grid)

        # setGeometry(topLeft_X,topLeft_Y,Width, Height) geometry of main window.
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
