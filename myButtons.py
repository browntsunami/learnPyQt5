#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

I am attempting to adapt this exercise
to include two more buttons at the top
left which behave similarly to the ones
in the original exercise.

In this example, we position two push
buttons in the bottom-right corner
of the window.

Author: Jan Bodnar
Adapted: Don Easley
Website: zetcode.com
Original Last edited: August 2017
Adaptation date: 1 May 2019


"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        myButton1 = QPushButton("PushMe")
        myButton2 = QPushButton("PullYou")

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(okButton)
        hbox1.addWidget(cancelButton)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(myButton1)
        hbox2.addWidget(myButton2)
        hbox2.addStretch(1)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
