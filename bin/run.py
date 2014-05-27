#!/usr/bin/env python

import sys

from PyQt4 import QtGui

from Paca.windows import main


if __name__ == "__main__":
        # Create QApplication
        app = QtGui.QApplication(sys.argv)

        # Create a HelloQt window and show it
        mainwindow = main.MainWindow()
        mainwindow.show()
        
        # Run the mainloop
        sys.exit(app.exec_())
