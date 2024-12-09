# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.savebox = QtWidgets.QGroupBox(Widget)
        self.savebox.setGeometry(QtCore.QRect(620, 10, 151, 131))
        self.savebox.setObjectName("savebox")
        self.save_button = QtWidgets.QPushButton(self.savebox)
        self.save_button.setGeometry(QtCore.QRect(30, 50, 91, 24))
        self.save_button.setObjectName("save_button")
        self.checkBox = QtWidgets.QCheckBox(self.savebox)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 121, 20))
        self.checkBox.setObjectName("checkBox")
        self.extractmedia = QtWidgets.QPushButton(self.savebox)
        self.extractmedia.setGeometry(QtCore.QRect(30, 100, 91, 24))
        self.extractmedia.setObjectName("extractmedia")
        self.label = QtWidgets.QLabel(self.savebox)
        self.label.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label.setObjectName("label")
        self.inputbox = QtWidgets.QGroupBox(Widget)
        self.inputbox.setGeometry(QtCore.QRect(10, 10, 600, 131))
        self.inputbox.setObjectName("inputbox")
        self.drop_area = QtWidgets.QLabel(self.inputbox)
        self.drop_area.setGeometry(QtCore.QRect(40, 20, 521, 71))
        self.drop_area.setFocusPolicy(QtCore.Qt.NoFocus)
        self.drop_area.setAcceptDrops(True)
        self.drop_area.setFrameShape(QtWidgets.QFrame.Box)
        self.drop_area.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.drop_area.setAlignment(QtCore.Qt.AlignCenter)
        self.drop_area.setObjectName("drop_area")
        self.pushButton = QtWidgets.QPushButton(self.inputbox)
        self.pushButton.setGeometry(QtCore.QRect(260, 100, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.output_area_1 = QtWidgets.QListWidget(Widget)
        self.output_area_1.setGeometry(QtCore.QRect(10, 150, 380, 400))
        self.output_area_1.setObjectName("output_area_1")
        self.output_area_2 = QtWidgets.QListWidget(Widget)
        self.output_area_2.setGeometry(QtCore.QRect(410, 150, 380, 400))
        self.output_area_2.setObjectName("output_area_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "IgExtractor"))
        self.savebox.setTitle(_translate("Widget", "Result"))
        self.save_button.setText(_translate("Widget", "Save As..."))
        self.checkBox.setText(_translate("Widget", "Autosave results"))
        self.extractmedia.setText(_translate("Widget", "Extract media"))
        self.label.setText(_translate("Widget", "Pictures, videos"))
        self.inputbox.setTitle(_translate("Widget", "Input"))
        self.drop_area.setText(_translate("Widget", "Drag and drop ZIP file here or click to browse"))
        self.pushButton.setText(_translate("Widget", "Process ZIP"))