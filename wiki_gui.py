# -*- coding: utf-8 -*-

import sys

# Form implementation generated from reading ui file '.\app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import wikipedia
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 362)
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(1)
        MainWindow.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.mainwindow = QtWidgets.QWidget(MainWindow)
        self.mainwindow.setObjectName("mainwindow")
        self.output = QtWidgets.QTextEdit(self.mainwindow)
        self.output.setGeometry(QtCore.QRect(260, 80, 341, 261))
        self.output.setObjectName("output")
        self.input = QtWidgets.QLineEdit(self.mainwindow)
        self.input.setGeometry(QtCore.QRect(260, 40, 331, 21))
        self.input.setObjectName("input")
        self.search_bt = QtWidgets.QPushButton(self.mainwindow)
        self.search_bt.setGeometry(QtCore.QRect(20, 20, 221, 41))
        self.search_bt.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.search_bt.setToolTipDuration(1)
        self.search_bt.setObjectName("search_bt")
        self.summary = QtWidgets.QCheckBox(self.mainwindow)
        self.summary.setGeometry(QtCore.QRect(20, 100, 70, 31))
        self.summary.setObjectName("summary")
        self.content = QtWidgets.QCheckBox(self.mainwindow)
        self.content.setGeometry(QtCore.QRect(120, 100, 81, 31))
        self.content.setObjectName("content")
        self.save = QtWidgets.QCheckBox(self.mainwindow)
        self.save.setGeometry(QtCore.QRect(20, 220, 101, 17))
        self.save.setObjectName("save")
        self.save_content = QtWidgets.QCheckBox(self.mainwindow)
        self.save_content.setGeometry(QtCore.QRect(130, 220, 91, 17))
        self.save_content.setObjectName("save_content")
        self.clear_bt = QtWidgets.QPushButton(self.mainwindow)
        self.clear_bt.setGeometry(QtCore.QRect(10, 280, 101, 51))
        self.clear_bt.setObjectName("clear_bt")
        self.about_bt = QtWidgets.QPushButton(self.mainwindow)
        self.about_bt.setGeometry(QtCore.QRect(130, 280, 101, 51))
        self.about_bt.setStyleSheet("")
        self.about_bt.setObjectName("about_bt")
        self.label = QtWidgets.QLabel(self.mainwindow)
        self.label.setGeometry(QtCore.QRect(260, 20, 331, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.mainwindow)
        self.label_2.setGeometry(QtCore.QRect(260, 60, 221, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.mainwindow)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.mainwindow)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 191, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.mainwindow)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 421, 16))
        self.label_5.setObjectName("label_5")
        self.save_bt = QtWidgets.QPushButton(self.mainwindow)
        self.save_bt.setGeometry(QtCore.QRect(20, 160, 201, 41))
        self.save_bt.setObjectName("save_bt")
        self.label_6 = QtWidgets.QLabel(self.mainwindow)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 191, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.mainwindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.search_bt.clicked.connect(self.search)
        self.clear_bt.clicked.connect(self.clear)
        self.save_bt.clicked.connect(self.save_b)
        self.about_bt.clicked.connect(self.about)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wiki Gui"))
        self.output.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>Output of what you searched</p></body></html>"))
        self.input.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>Enter somenthing if is empty crash</p></body></html>"))
        self.search_bt.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>Search wiki for an article</p></body></html>"))
        self.search_bt.setText(_translate("MainWindow", "Search"))
        self.summary.setToolTip(_translate("MainWindow", "<html><head/><body><p>Show an summary</p></body></html>"))
        self.summary.setText(_translate("MainWindow", "Summary"))
        self.content.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>Show full page in text</p></body></html>"))
        self.content.setText(_translate("MainWindow", "Content"))
        self.save.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>Save a summary of a page</p></body></html>"))
        self.save.setText(_translate("MainWindow", "Save Summary"))
        self.save_content.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>Save full description of a page </p></body></html>"))
        self.save_content.setText(_translate("MainWindow", "Save Content"))
        self.clear_bt.setToolTip(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-weight:600;\">Clear output of label text!!</span></p></body></html>"))
        self.clear_bt.setText(_translate("MainWindow", "Clear"))
        self.about_bt.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>About Program Version </p></body></html>"))
        self.about_bt.setText(_translate("MainWindow", "About"))
        self.label.setText(_translate("MainWindow", "Enter a title for a wikipedia page"))
        self.label_2.setText(_translate("MainWindow", "Output of search button"))
        self.label_3.setText(_translate("MainWindow", "Check a box"))
        self.label_4.setText(_translate("MainWindow", "Clear and About Buttons"))
        self.label_5.setText(_translate("MainWindow",
                                        "Tap on search  after checked the desired buttons and entered something in input field"))
        self.save_bt.setText(_translate("MainWindow", "Save"))
        self.save_bt.setToolTip(_translate("MainWindow", "Save file"))
        self.label_6.setText(_translate("MainWindow", "Save but check a box"))


    def search(self):
        text = self.input.text()
        se = wikipedia.search(text)
        title = wikipedia.page(se)
        self.summmery = title.summary
        self.con = title.content

        if self.summary.isChecked():
            self.output.setText(str(self.summmery))
        elif self.content.isChecked():
            self.output.setText(str(self.con))

        elif self.save_content or self.save or self.content or self.summary is False:
            self.output.setText("Error: Check a box! Please")

    def save_b(self):
        if self.save.isChecked():
            f1 = open('../summary.txt', 'w', encoding='utf-8')
            f1.write("Generated by Wiki Gui V 1.0\n")
            f1.write("===========================\n")
            f1.write(str(self.summmery))
            f1.close()
        elif self.save_content.isChecked():
            f2 = open('../content.txt', 'w', encoding='utf-8')
            f2.write("Generated by Wiki Gui V 1.0\n")
            f2.write("===========================\n")
            f2.write(str(self.con))
            f2.close()
        elif self.save_content or self.save or self.content or self.summary is False:
            self.output.setText("Error: Check a box! Please")

    def clear(self):
        self.output.clear()

    def about(self):
        self.mess = QMessageBox()
        self.mess.setIcon(QtWidgets.QMessageBox.Information)
        self.mess.setWindowTitle("About")
        self.mess.setText("Gui designed by BloddyRose for lazy people who want to save and content of wikipedia easy\nFind it on github: \nVersion 1 by BloddyRose")
        self.mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tray = QtWidgets.QSystemTrayIcon(QtGui.QIcon("icon.png"), app)
    tray.show()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
