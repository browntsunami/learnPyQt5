#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

Author: Jan Bodnar
Website: zetcode.com
Last edited: January 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # Setting up  a variable for initial value the slider and display
        # will take.
        initValue = 50

        # Create LCD display object
        lcd = QLCDNumber(self)
        # Initialize the value displayed by our LCD display object
        lcd.display(initValue)

        # Create a slider bar object that is oriented horizontally
        sld = QSlider(Qt.Horizontal, self)
        # Set the minimum and maximum range of the slider object
        sld.setMinimum(10)
        sld.setMaximum(250)
        # Set initial value of slider (which matches the initial value of
        # our LCD display)
        sld.setValue(initValue)

        # Create a vertical stacked box object to store our widgets
        vbox = QVBoxLayout()
        # Populate the vertical box object with our lcd and slider object
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        # Format our layout using the configured vertical box
        self.setLayout(vbox)

        # Connect the changes of the slider bar to what is displayed
        # on the LCD dispaly
        sld.valueChanged.connect(lcd.display)

        # Setting up the geometry and title of the main window
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')

        # Display the completed object
        self.show()

    # reimplement the keyPressEvent() event handler. This will allow the user
    # to terminate the process using the escape key.
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
