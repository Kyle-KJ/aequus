# Aequus
# Stock Price Info GUI

import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):

        super().__init__()

        self.setWindowTitle('Aequus')

        self.show()


app = qtw.QApplication([])
window = MainWindow()
app.exec_()