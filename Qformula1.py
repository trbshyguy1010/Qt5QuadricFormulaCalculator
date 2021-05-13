from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import math

class Ui_QuadricFormulaCalculator(object):
    def setupUi(self, QuadricFormulaCalculator):
        QuadricFormulaCalculator.setObjectName("QuadricFormulaCalculator")
        QuadricFormulaCalculator.resize(360, 480)
        self.lineEdit_2 = QtWidgets.QLineEdit(QuadricFormulaCalculator)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 100, 341, 21))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(QuadricFormulaCalculator)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 170, 341, 21))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(QuadricFormulaCalculator)
        self.pushButton.setGeometry(QtCore.QRect(270, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(QuadricFormulaCalculator)
        self.pushButton2.setGeometry(QtCore.QRect(260, 205, 85, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.label = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(QuadricFormulaCalculator)
        self.lineEdit_4.setGeometry(QtCore.QRect(112, 340, 231, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5 = QtWidgets.QLineEdit(QuadricFormulaCalculator)
        self.lineEdit_5.setGeometry(QtCore.QRect(112, 390, 231, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.label_4 = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 47, 13))
        self.label_6.setObjectName("label_6")
        self.eq = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.eq.setGeometry(QtCore.QRect(10, 230, 350, 16))
        self.eq.setObjectName("eq")
        self.status = QtWidgets.QLabel(QuadricFormulaCalculator)
        self.status.setGeometry(QtCore.QRect(30, 440, 150, 13))
        self.status.setObjectName("status")
        self.lineEdit_6 = QtWidgets.QLineEdit(QuadricFormulaCalculator)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 30, 341, 21))
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(QuadricFormulaCalculator)
        QtCore.QMetaObject.connectSlotsByName(QuadricFormulaCalculator)


    def retranslateUi(self, QuadricFormulaCalculator):
        _translate = QtCore.QCoreApplication.translate
        QuadricFormulaCalculator.setWindowTitle(_translate("QuadricFormulaCalculator", "Quadric Formula Calculator"))
        self.pushButton.setText(_translate("QuadricFormulaCalculator", "Calculate"))
        self.pushButton2.setText(_translate("QuadricFormulaCalculator", "Show Equation"))
        self.label.setText(_translate("QuadricFormulaCalculator", "a Value :"))
        self.label_2.setText(_translate("QuadricFormulaCalculator", "b Value :"))
        self.label_3.setText(_translate("QuadricFormulaCalculator", "c Value :"))
        self.label_4.setText(_translate("QuadricFormulaCalculator", "Solution 1 :"))
        self.label_5.setText(_translate("QuadricFormulaCalculator", "Solution 2 :"))
        self.label_6.setText(_translate("QuadricFormulaCalculator", "Equation :"))
        self.eq.setText(_translate("QuadricFormulaCalculator", "ax²+bx+c=0"))
        self.status.setText(_translate("QuadricFormulaCalculator", "..."))
        self.pushButton2.clicked.connect(self.equationbtnevent)
        self.pushButton.clicked.connect(self.calculatebtnevent)

    def equationbtnevent(self):
        try:
            num1 = int(self.lineEdit_6.text())
            num2 = int(self.lineEdit_2.text())
            num3 = int(self.lineEdit_3.text())
            self.eq.setText("(" + str(num1) + ")x² +(" + str(num2) + ")x +(" + str(num3) + ")=0")
        except (NameError, AttributeError, ValueError):
            self.status.setText("values not specified")
            pass
    def calculatebtnevent(self):
        try:
            num1 = int(self.lineEdit_6.text())
            num2 = int(self.lineEdit_2.text())
            num3 = int(self.lineEdit_3.text())
            deltA = num2 ** 2 - 4 * num1 * num3
            if deltA > 0:
                global x
                x = 2 * num1
                Qfxp = round(((-num2) - math.sqrt(deltA)) / x)
                Qfxs = round(((-num2) + math.sqrt(deltA)) / x)
                self.lineEdit_4.setText(str(Qfxp))
                self.lineEdit_5.setText(str(Qfxs))
                self.status.setText("2 solutions")
            elif deltA == 0:
                Qfx = round((-num2) / x)
                self.lineEdit_4.setText(str(Qfx))
                self.status.setText("1 solution")
            elif deltA < 0:
                self.status.setText("No solutions")
        except (NameError, AttributeError, ValueError):
            self.status.setText("values not specified")
            pass
#on-execute
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_QuadricFormulaCalculator()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
