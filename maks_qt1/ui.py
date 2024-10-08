# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border: 2px double yellow ;\n"
"border-radius: 10px;\n"
"background-color:#b266ff;\n"
"color: white;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_generator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generator.setGeometry(QtCore.QRect(160, 270, 101, 23))
        self.btn_generator.setStyleSheet("border: 2px;\n"
"border-radius: 10px;\n"
"background-color:#44c767;\n"
"color: white;\n"
"")
        self.btn_generator.setObjectName("btn_generator")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(50, 110, 222, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(100, 20, 232, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.cb_alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_alphabet.setGeometry(QtCore.QRect(50, 150, 157, 17))
        self.cb_alphabet.setObjectName("cb_alphabet")
        self.cb_numders = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_numders.setGeometry(QtCore.QRect(50, 180, 144, 17))
        self.cb_numders.setObjectName("cb_numders")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_generator.setText(_translate("MainWindow", "Згенерувати"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))
        self.title.setText(_translate("MainWindow", "Генерар паролів"))
        self.cb_alphabet.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.cb_numders.setText(_translate("MainWindow", "Використовувати числа"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
