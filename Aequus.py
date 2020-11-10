# Aequus
# Stock Price Info GUI

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction
from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    
    def __init__(self):

        super(MainWindow, self).__init__()

        self.setWindowTitle('Aequus')
        
        # self.setWindowIcon(QIcon('img.png'))

        # self.setLayout(qtw.QVBoxLayout())

        # Menu Actions

        # Quit Action
        quitAction = QAction('&Quit', self)
        quitAction.setStatusTip('Quit the application')
        quitAction.setShortcut('Ctrl+Q')
        quitAction.triggered.connect(self.close_app)

        # Test Action
        testAction = QAction('&Test', self)
        testAction.setStatusTip('Test action')

        # Initialise Status Bar
        self.statusBar()

        # Main Menu Items
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        editMenu = mainMenu.addMenu('&Edit')

        # File Menu Actions
        fileMenu.addAction(quitAction)

        # Edit Menu Actions
        editMenu.addAction(testAction)


        self.welcome()
    
    def close_app(self):
        sys.exit()
    
    def welcome(self):

        # Display Welcome Image & Text

        # Buttons

        exit_btn = QPushButton('Exit', self)

        exit_btn.resize(exit_btn.sizeHint())
        exit_btn.move(10,100)

        self.show()
    
def run_app():
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_app()

