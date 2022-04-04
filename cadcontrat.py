# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadcontrat.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from PyQt5.QtWidgets import QMessageBox


class Ui_CadContratante(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 344)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/factory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.lineNome = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineNome.setFont(font)
        self.lineNome.setObjectName("lineNome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineNome)
        self.labelPrefixo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelPrefixo.setFont(font)
        self.labelPrefixo.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelPrefixo.setObjectName("labelPrefixo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPrefixo)
        self.linePrefixo = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linePrefixo.setFont(font)
        self.linePrefixo.setObjectName("linePrefixo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linePrefixo)
        self.labelModelo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelModelo.setFont(font)
        self.labelModelo.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.labelModelo.setObjectName("labelModelo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelModelo)
        self.lineModelo = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineModelo.setFont(font)
        self.lineModelo.setObjectName("lineModelo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineModelo)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushSave = QtWidgets.QPushButton(self.centralwidget)
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
        self.pushSave.clicked.connect(self.salvaBD)
        self.verticalLayout.addWidget(self.pushSave)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Contratantes"))
        self.label.setText(_translate("MainWindow", "Cadastro de contratantes"))
        self.labelNome.setText(_translate("MainWindow", "Nome (sem espaços)"))
        self.labelPrefixo.setText(_translate("MainWindow", "Nome a imprimir"))
        self.labelModelo.setText(_translate("MainWindow", "CPF / CNPJ"))
        self.pushSave.setText(_translate("MainWindow", "Salvar"))

    def salvaBD (self):
        d={}
        #produto="Moddus Maturador"
        nome=self.lineNome.displayText()
        nimprime=self.linePrefixo.displayText()
        cpf=self.lineModelo.displayText()

        d[nome]={
            "nome":nome,
            "imprime":nimprime,
            "cpf":cpf
        } 

        with open("db/contratante.json") as f:
            data=json.load(f)
        data.update(d)

        with open("db/contratante.json","w") as a:
            a.write(json.dumps(data))
        self.limpa()
        self.mbox()
        

    def limpa (self):
        self.lineNome.setText("")
        self.linePrefixo.setText("")
        self.lineModelo.setText("")
        

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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
