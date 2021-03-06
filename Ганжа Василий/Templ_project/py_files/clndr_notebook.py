# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clndr_notebook.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMainWindow
from widgets import CalendarWidget, ListView, DateTimeEdit, LineEdit, PushButton


class Ui_MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = CalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 541, 641))
        self.calendarWidget.setObjectName("calendarWidget")
        self.listView = ListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(540, 0, 501, 721))
        self.listView.setObjectName("listView")
        self.dateTimeEdit = DateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(0, 640, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit = LineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 670, 541, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = PushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 640, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menufile.addAction(self.actionSave)
        self.menubar.addAction(self.menufile.menuAction())
        self.actionSave.triggered.connect(self.save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add Note"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save "))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def save(self):
        pushButton_coords = str(self.pushButton.x()), str(self.pushButton.y())
        clndr_coords = str(self.calendarWidget.x()), str(self.calendarWidget.y())
        view_coords = str(self.listView.x()), str(self.listView.y())
        line_coords = str(self.lineEdit.x()), str(self.lineEdit.y())
        dt_edit_coords = str(self.dateTimeEdit.x()), str(self.dateTimeEdit.y())
        import xml.etree.ElementTree as ET

        tree = ET.parse('yi_files\\clndr_notebook.ui')
        root = tree.getroot()
        for child in root.iter('widget'):

            for i in child.iter('widget'):
                if i.attrib['name'] == 'pushButton':
                    for j in i.iter('property'):
                        for k in j.iter('rect'):
                            for h in k.iter('x'):
                                h.text = pushButton_coords[0]
                            for g in k.iter('y'):
                                g.text = pushButton_coords[1]
                elif i.attrib['name'] == 'calendarWidget':
                    for j in i.iter('property'):
                        for k in j.iter('rect'):
                            for h in k.iter('x'):
                                h.text = clndr_coords[0]
                            for g in k.iter('y'):
                                g.text = clndr_coords[1]
                elif i.attrib['name'] == 'dateTimeEdit':
                    for j in i.iter('property'):
                        for k in j.iter('rect'):
                            for h in k.iter('x'):
                                h.text = dt_edit_coords[0]
                            for g in k.iter('y'):
                                g.text = dt_edit_coords[1]
                elif i.attrib['name'] == 'listView':
                    for j in i.iter('property'):
                        for k in j.iter('rect'):
                            for h in k.iter('x'):
                                h.text = view_coords[0]
                            for g in k.iter('y'):
                                g.text = view_coords[1]
                elif i.attrib['name'] == 'lineEdit':
                    for j in i.iter('property'):
                        for k in j.iter('rect'):
                            for h in k.iter('x'):
                                h.text = line_coords[0]
                            for g in k.iter('y'):
                                g.text = line_coords[1]
        self.file_path, ok_pressed = QInputDialog.getText(self, "Enter the path to the file directory",
            "What the path?                                                                              ")
        if ok_pressed and self.file_path != '':
            tree.write(self.file_path + '\\' + 'clndr_notebook.ui')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
