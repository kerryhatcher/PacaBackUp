
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.setWindowTitle("PacaBackUp")

        # Vertical layout
        self.layout = QtGui.QVBoxLayout(self)

        # Create widgets
        self.label = QtGui.QLabel("AWS Keys")
        self.key_id = QtGui.QLineEdit("Access Key ID")
        self.secret_key = QtGui.QLineEdit("Secret Access Key")
        self.secret_key.setReadOnly(True)
        self.label2 = QtGui.QLabel("Shall I begin?")
        self.button = QtGui.QPushButton("Engage")

        # Add widgets to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.key_id)
        self.layout.addWidget(self.secret_key)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.button)

        # Connect self.key_id with self.sayHello(name) when text is changed
        #self.connect(self.key_id, QtCore.SIGNAL("textChanged(const QString&)"), self.sayHello)

        # Button event
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.buttonClicked)
        #self.button.clicked(self.buttonClicked())

        #Clear AWS Settings
        #self.connect(self.key_id, QtCore.SIGNAL("focus()"), self.clearSettings)

    #def sayHello(self, name):
        # Set the output text
        #self.secret_key.setText("Hello " + name + "!")

    def buttonClicked(self):
        sender = self.sender()
        self.secret_key.setText("Button Pushed!!")


    #def clearSettings(self):

