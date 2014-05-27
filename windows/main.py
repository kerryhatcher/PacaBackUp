
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.setWindowTitle("Hello Qt")

        # Vertical layout
        self.layout = QtGui.QVBoxLayout(self)

        # Create widgets
        self.label = QtGui.QLabel("What's your name?")
        self.name = QtGui.QLineEdit()
        self.output = QtGui.QLineEdit()
        self.output.setReadOnly(True)
        self.label2 = QtGui.QLabel("What's yo number?")
        self.button = QtGui.QPushButton("test")

        # Add widgets to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.button)

        # Connect self.name with self.sayHello(name) when text is changed
        self.connect(self.name, QtCore.SIGNAL("textChanged(const QString&)"), self.sayHello)

        # Button event
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.buttonClicked)
        #self.button.clicked(self.buttonClicked())

    def sayHello(self, name):
        # Set the output text
        self.output.setText("Hello " + name + "!")

    def buttonClicked(self):
        sender = self.sender()
        self.output.setText("Button Pushed!!")

