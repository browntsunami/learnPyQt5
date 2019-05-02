#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

Slightly modified this exercise by adding some non-functioning buttons
to better show how the label is aligned and place the label in cell (1,1)

In this example, we display the x and y
coordinates of a mouse pointer in a label widget.

Original Author: Jan Bodnar
Modified by: Don Easley

Website: zetcode.com
Original edited: August 2017
Modified date: 2 May 2019
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout() # Initialize a grid object

        x = 0 # Initial value for x independent of mouse location
        y = 0 # Initial value for y independent of mouse location

        # I added three buttons only to  bettershow that the label is aligned
        # to the top of the cell. This was not in original exercise.
        Button1 = QPushButton('button 1')
        Button2 = QPushButton('button 2')
        Button3 = QPushButton('button 3')

        # The .format(x0,x1,x2,...,xn) method for a string, substitutes in order
        # {0},{1},{2},...,{n} in the text string the values associated with
        # variables (x0,x1,x2,...,xn). You can aslo use indexed replacement say
        # mystring = "I have {numApples} apples and {numOranges} oranges".
        # format(numApples=2, numOranges=3). Then myString will have the value
        # "I have 2 apples and 3 oranges".
        self.text = "x: {0},  y: {1}".format(x, y) # Initialize label text

        # Adding my ad hoc buttons to the grid, not in original exercise.
        grid.addWidget(Button1, 0, 0)
        grid.addWidget(Button2, 0, 1)
        grid.addWidget(Button3, 1, 0)

        self.label = QLabel(self.text, self) # Place text string in a QLabel

        # Add the label widget to the grid at cell (1,1) with text aligned
        # to the top of the cell (note: not the widget)
        # to see t6he difference change the comment below to exicutable
        grid.addWidget(self.label, 1, 1, Qt.AlignBottom) # Add QLabel to grid
        # grid.addWidget(self.label, 1, 1, Qt.AlignTop) # Add QLabel to grid

        self.setMouseTracking(True) # Mouse tracking is off by default

        # set the layout of displayed window based on out grid
        self.setLayout(grid)

        # set position and size of displayed window
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object') # set titie of displyed window
        self.show() # Bring our designed window in memory to display terminal

    # reimplementaion of the mouseMoveEvent the event object is "event"
    def mouseMoveEvent(self, event):

        # The .x() and .y() methods provides the x,y coordinates in pixels
        # of the mouse movement event within the window
        x = event.x()
        y = event.y()

        # creating the text new text string based on the new (x,y) coordinates
        text = "x: {0},  y: {1}".format(x, y)
        # updating the label with the new text (note: the text here is local)
        self.label.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
