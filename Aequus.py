# Aequus
# Stock Price Info GUI

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QLabel, QComboBox
from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    
    def __init__(self):

        super(MainWindow, self).__init__()

        self.setGeometry(300, 300, 1618, 1000)
        self.setWindowTitle('Aequus')
        
        self.setWindowIcon(QIcon('money-icon.png'))

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

        self.stocks_list()
    
    def close_app(self):
        sys.exit()
    
    def welcome(self):

        # Display Welcome Image & Text

        # Buttons

        stock_btn = QPushButton('Stocks List', self)
        stock_btn.clicked.connect(self.stocks_list)
        stock_btn.resize(100, 60)
        stock_btn.move(100, 200)

        self.show()
    
    def stocks_list(self):

        index_label = QLabel('Index:', self)
        index_label.move(30, 20)

        index_cb = QComboBox(self)
        index_cb.addItem('SPY')
        index_cb.addItem('DJI')
        index_cb.addItem('IXIC')
        index_cb.addItem('UKX')

        index_cb.move(30, 50)

        index_cb.activated[str].connect(self.get_stock_list)

        self.show()

    def get_stock_list(self, index):

        # Call function to grab top n stocks in index data
        
        # For each item in list create line to display data

        return

    
def run_app():
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_app()

