from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generator.clicked.connect(self.generate)

    def generate(self):
        signs=""
        if self.ui.cb_alphabet.isChecked():
            signs +="qwertyuiopasdfghjklzxcvbnm"
        if self.ui.cb_numders.isChecked():
            signs +="0123456789"

        result =""
        number = random.randint(7,15)
        for _ in range(number):
            result+=random.choice(signs)
        
        self.ui.result.setText(result)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()