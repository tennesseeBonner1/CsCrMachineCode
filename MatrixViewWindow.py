# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\colli\source\repos\CsCrMachineCode\MatrixViewUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_matrixViewDialog(object):
    def setupUi(self, matrixViewDialog):
        matrixViewDialog.setObjectName("matrixViewDialog")
        matrixViewDialog.resize(505, 203)
        self.verticalLayout = QtWidgets.QVBoxLayout(matrixViewDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.generalButtonsLayout = QtWidgets.QHBoxLayout()
        self.generalButtonsLayout.setObjectName("generalButtonsLayout")
        self.saveButton = QtWidgets.QPushButton(matrixViewDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.generalButtonsLayout.addWidget(self.saveButton)
        self.regenerateButton = QtWidgets.QPushButton(matrixViewDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.regenerateButton.setFont(font)
        self.regenerateButton.setObjectName("regenerateButton")
        self.generalButtonsLayout.addWidget(self.regenerateButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.generalButtonsLayout.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(matrixViewDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.generalButtonsLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.generalButtonsLayout)
        self.generalButtonsLine = QtWidgets.QFrame(matrixViewDialog)
        self.generalButtonsLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.generalButtonsLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.generalButtonsLine.setObjectName("generalButtonsLine")
        self.verticalLayout.addWidget(self.generalButtonsLine)
        self.gridWidget = QtWidgets.QWidget(matrixViewDialog)
        self.gridWidget.setObjectName("gridWidget")
        self.verticalLayoutAroundGrid = QtWidgets.QVBoxLayout(self.gridWidget)
        self.verticalLayoutAroundGrid.setObjectName("verticalLayoutAroundGrid")
        self.gridInfoLabel = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridInfoLabel.sizePolicy().hasHeightForWidth())
        self.gridInfoLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gridInfoLabel.setFont(font)
        self.gridInfoLabel.setObjectName("gridInfoLabel")
        self.verticalLayoutAroundGrid.addWidget(self.gridInfoLabel)
        self.gridInfoLine = QtWidgets.QFrame(self.gridWidget)
        self.gridInfoLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gridInfoLine.setObjectName("gridInfoLine")
        self.verticalLayoutAroundGrid.addWidget(self.gridInfoLine)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutAroundGrid.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.gridWidget)
        self.pageButtonsLine = QtWidgets.QFrame(matrixViewDialog)
        self.pageButtonsLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.pageButtonsLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pageButtonsLine.setObjectName("pageButtonsLine")
        self.verticalLayout.addWidget(self.pageButtonsLine)
        self.horizontalButtonsLayout = QtWidgets.QHBoxLayout()
        self.horizontalButtonsLayout.setObjectName("horizontalButtonsLayout")
        self.previousButton = QtWidgets.QPushButton(matrixViewDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.previousButton.setFont(font)
        self.previousButton.setObjectName("previousButton")
        self.horizontalButtonsLayout.addWidget(self.previousButton)
        self.pageNumberLabel = QtWidgets.QLabel(matrixViewDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pageNumberLabel.setFont(font)
        self.pageNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pageNumberLabel.setObjectName("pageNumberLabel")
        self.horizontalButtonsLayout.addWidget(self.pageNumberLabel)
        self.nextButton = QtWidgets.QPushButton(matrixViewDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName("nextButton")
        self.horizontalButtonsLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalButtonsLayout)

        self.retranslateUi(matrixViewDialog)
        QtCore.QMetaObject.connectSlotsByName(matrixViewDialog)

    def retranslateUi(self, matrixViewDialog):
        _translate = QtCore.QCoreApplication.translate
        matrixViewDialog.setWindowTitle(_translate("matrixViewDialog", "Matrix View of Trials"))
        self.saveButton.setText(_translate("matrixViewDialog", "Save As Image"))
        self.regenerateButton.setText(_translate("matrixViewDialog", "Change Parameters"))
        self.closeButton.setText(_translate("matrixViewDialog", "Close"))
        self.gridInfoLabel.setText(_translate("matrixViewDialog", "Loading..."))
        self.previousButton.setText(_translate("matrixViewDialog", "Previous Page"))
        self.pageNumberLabel.setText(_translate("matrixViewDialog", "Page 1 / 1"))
        self.nextButton.setText(_translate("matrixViewDialog", "Next Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    matrixViewDialog = QtWidgets.QDialog()
    ui = Ui_matrixViewDialog()
    ui.setupUi(matrixViewDialog)
    matrixViewDialog.show()
    sys.exit(app.exec_())