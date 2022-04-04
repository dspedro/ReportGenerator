# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadprod.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from PyQt5.QtWidgets import QMessageBox


class Ui_CadProd(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 604)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 240, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 240, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 240, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 221))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelNome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelNome.setFont(font)
        self.labelNome.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelNome.setObjectName("labelNome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelNome)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.labelFormulacao = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelFormulacao.setFont(font)
        self.labelFormulacao.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelFormulacao.setObjectName("labelFormulacao")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelFormulacao)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.labelDoseMin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelDoseMin.setFont(font)
        self.labelDoseMin.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelDoseMin.setObjectName("labelDoseMin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelDoseMin)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.labelDoseMax = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelDoseMax.setFont(font)
        self.labelDoseMax.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelDoseMax.setObjectName("labelDoseMax")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelDoseMax)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.labelCalMin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCalMin.setFont(font)
        self.labelCalMin.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelCalMin.setObjectName("labelCalMin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelCalMin)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.labelClasse = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelClasse.setFont(font)
        self.labelClasse.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelClasse.setObjectName("labelClasse")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelClasse)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.labelTempMin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTempMin.setFont(font)
        self.labelTempMin.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelTempMin.setObjectName("labelTempMin")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelTempMin)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.labelTempMax = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTempMax.setFont(font)
        self.labelTempMax.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelTempMax.setObjectName("labelTempMax")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelTempMax)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.labelUmiMin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelUmiMin.setFont(font)
        self.labelUmiMin.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelUmiMin.setObjectName("labelUmiMin")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelUmiMin)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.labelUmiMax = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelUmiMax.setFont(font)
        self.labelUmiMax.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelUmiMax.setObjectName("labelUmiMax")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.labelUmiMax)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.labelVentoMin = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelVentoMin.setFont(font)
        self.labelVentoMin.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelVentoMin.setObjectName("labelVentoMin")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.labelVentoMin)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.labelVenMax = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelVenMax.setFont(font)
        self.labelVenMax.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelVenMax.setObjectName("labelVenMax")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.labelVenMax)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.labelCalMax = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCalMax.setFont(font)
        self.labelCalMax.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelCalMax.setObjectName("labelCalMax")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelCalMax)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushSave.clicked.connect(self.salvaBD)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushSave.sizePolicy().hasHeightForWidth())
        self.pushSave.setSizePolicy(sizePolicy)
        self.pushSave.setMinimumSize(QtCore.QSize(0, 50))
        self.pushSave.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushSave.setFont(font)
        self.pushSave.setObjectName("pushSave")
        self.verticalLayout.addWidget(self.pushSave)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de produtos"))
        self.label.setText(_translate("MainWindow", "Cadastro de produtos"))
        self.labelNome.setText(_translate("MainWindow", "Nome"))
        self.labelFormulacao.setText(_translate("MainWindow", "Formulação"))
        self.labelDoseMin.setText(_translate("MainWindow", "Dose Mínima"))
        self.labelDoseMax.setText(_translate("MainWindow", "Dose Máxima"))
        self.labelCalMin.setText(_translate("MainWindow", "Calda Mínima"))
        self.labelClasse.setText(_translate("MainWindow", "Classe"))
        self.labelTempMin.setText(_translate("MainWindow", "Temperatura Mínima"))
        self.labelTempMax.setText(_translate("MainWindow", "Temperatura Máxima"))
        self.labelUmiMin.setText(_translate("MainWindow", "Umidade Mínima"))
        self.labelUmiMax.setText(_translate("MainWindow", "Umidade Máxima"))
        self.labelVentoMin.setText(_translate("MainWindow", "Vento Mínimo"))
        self.labelVenMax.setText(_translate("MainWindow", "Vento Máximo"))
        self.labelCalMax.setText(_translate("MainWindow", "Calda Máxima"))
        self.pushSave.setText(_translate("MainWindow", "Salvar"))

    def salvaBD (self):
        d={}
        #produto="Moddus Maturador"
        nome=self.lineEdit.displayText()
        formulacao=self.lineEdit_2.displayText()
        dosemax=self.lineEdit_4.displayText()
        dosemin=self.lineEdit_3.displayText()
        caldamax=self.lineEdit_6.displayText()
        caldamin=self.lineEdit_5.displayText()
        classe=self.lineEdit_7.displayText()
        tempmax=self.lineEdit_9.displayText()
        tempmin=self.lineEdit_8.displayText()
        umidmin=self.lineEdit_10.displayText()
        umidmax=self.lineEdit_11.displayText()
        ventomax=self.lineEdit_13.displayText()
        ventomin=self.lineEdit_12.displayText()

        d[nome]={
            "nome":nome,
            "formulacao":formulacao,
            "dosemax":dosemax,
            "dosemin":dosemin,
            "caldamax":caldamax,
            "caldamin":caldamin,
            "classe":classe,
            "tempmax":tempmax,
            "tempmin":tempmin,
            "umidmin":umidmin,
            "umidmax":umidmax,
            "ventomax":ventomax,
            "ventomin":ventomin
        } 

        with open("db/produto.json") as f:
            data=json.load(f)

        data.update(d)

        with open("db/produto.json","w") as a:
            a.write(json.dumps(data))
        self.limpa()
        self.mbox()
    	

    def limpa (self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_13.setText("")
        self.lineEdit_12.setText("")

    def mbox(self):
    	box = QMessageBox()
    	box.setWindowTitle("Salvo!")
    	box.setText("Cadastro realizado com sucesso.")
    	box.setIcon(QMessageBox.Information)
    	box.setStandardButtons(QMessageBox.Ok)

    	x = box.exec_()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CadProd()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())