import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QGridLayout,
    QPushButton, QApplication)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # Defome the two push button objects
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        # btn1 = QPushButton("Button 1")
        # btn2 = QPushButton("Button 2")

        # When button is clicked execute buttonClicked function
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        # Initialize grid object
        grid = QGridLayout()

        # Define the layout of the main window based on grid
        #self.setLayout(grid)

        # space between grid locations
        grid.setSpacing(10)

        # populate the grid with the two button object
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 1, 0)

        # setup the status bar in main window to display button push
        self.statusBar()

        # setGeometry(topLeft_X,topLeft_Y,Width, Height) geometry of main window.
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        # This fucntion is excecuted when a button is pressed
        # it uses sender module in QMainWindow to find which button
        # was pressed and sends the information to the status bar
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
