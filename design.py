# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User2\Documents\DimaProject\FSImg\Disain\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 317)
        MainWindow.setMinimumSize(QtCore.QSize(300, 266))
        MainWindow.setMaximumSize(QtCore.QSize(582, 317))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 13, 62, 19))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 13, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(8, 43, 171, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 73, 62, 19))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(7, 73, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 43, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(7, 103, 181, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 103, 62, 19))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(7, 133, 281, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 16, 141, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 46, 141, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 100, 62, 19))
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(214, 12, 61, 22))
        self.spinBox.setMaximum(255)
        self.spinBox.setProperty("value", 150)
        self.spinBox.setObjectName("spinBox")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 72, 141, 16))
        self.label_8.setObjectName("label_8")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(215, 67, 60, 22))
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setProperty("value", 20)
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 100, 81, 19))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 100, 81, 19))
        self.pushButton_6.setObjectName("pushButton_6")
        self.spinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(214, 39, 62, 22))
        self.spinBox_2.setSingleStep(0.01)
        self.spinBox_2.setProperty("value", 1.0)
        self.spinBox_2.setObjectName("spinBox_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(7, 270, 571, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 13, 281, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(9, 15, 261, 231))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск пожаров"))
        self.pushButton.setText(_translate("MainWindow", "Выбор"))
        self.label.setText(_translate("MainWindow", "Выберете папку с фотографиями"))
        self.label_2.setText(_translate("MainWindow", "Количество фотографий для обработки"))
        self.pushButton_2.setText(_translate("MainWindow", "Выбор"))
        self.label_3.setText(_translate("MainWindow", "Выберете вапку для пожаров"))
        self.label_4.setText(_translate("MainWindow", "Выберете папку"))
        self.label_5.setText(_translate("MainWindow", "Выберете папку для возможных пожаров"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбор"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры"))
        self.label_6.setText(_translate("MainWindow", "Укажите интенсивность пожара"))
        self.label_7.setText(_translate("MainWindow", "Укажите площадь пожара"))
        self.pushButton_4.setText(_translate("MainWindow", "Пуск"))
        self.label_8.setText(_translate("MainWindow", "Метр квардратный на пиксель"))
        self.pushButton_5.setText(_translate("MainWindow", "Отчистить LOG"))
        self.pushButton_6.setText(_translate("MainWindow", "Сохранить LOG"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

