""" AnalysisSettingsManager.py
    Last Modified: 5/6/2020
    Taha Arshad, Tennessee Bonner, Devin Mensah, Khalid Shaik, Collin Vaille
    
    This program handles all of the user interaction with AnalysisSettingsWindow.py
    (All of the events that happen once Analyze -> Re-Analyze Session is pressed in the menu bar) 
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QMessageBox
import AnalysisSettingsWindow as asw
import json
import JSONConverter as jsCon
import DataAnalysis as da
import InputManager as im
import TheSession as ts


#Set up and open the window for re-analyzing the currently open session
def openAnalysisSettingsWindow():
    global windowWrapper, dialogWindow

    # Set up the window
    dialogWindow = QDialog()
    windowWrapper = asw.Ui_AnalysisSettingsWindow()
    windowWrapper.setupUi(dialogWindow)

    #Set connections for the buttons
    windowWrapper.pushButton_ReAnalyze.released.connect(reAnalyze)
    windowWrapper.radioButton_GenerateNew.toggled.connect(setFilenameEditorEnabled)

    #Set default settings to current session values
    windowWrapper.spinBox_StdDev.setValue(ts.currentSession.thresholdSD)
    windowWrapper.spinBox_MinDuration.setValue(ts.currentSession.thresholdMinDuration)
    windowWrapper.spinBox_MinVoltage.setValue(ts.currentSession.minVoltage)

    #Properly set the text in the line editor
    windowWrapper.lineEdit_customSaveName.setText(jsCon.getCurrentFilename())

    #Shows the window
    dialogWindow.exec()


#This function takes the user's changes and creates a new JSON file or edits the existing one
def reAnalyze():

    #Save the values that the user entered in the analysis settings window
    overwrite = windowWrapper.radioButton_Overwrite.isChecked()
    newFile = windowWrapper.radioButton_GenerateNew.isChecked()
    customName = windowWrapper.lineEdit_customSaveName.text()
    stdDevNumber = windowWrapper.spinBox_StdDev.value()
    minDuration = windowWrapper.spinBox_MinDuration.value()
    minVoltage = windowWrapper.spinBox_MinVoltage.value()

    nameError = False
    
    #Check to see if the user is saving with a valid file name
    if not overwrite or newFile:
        if ("\\" in customName or "/" in customName or ":" in customName or "<" in customName or ">" in customName or "*" in customName or "?" in customName or "\"" in customName or "|" in customName):
            nameError = True
            invalidSettingsNotice = QMessageBox()
            invalidSettingsNotice.setText("Filename may not contain any of the following characters: \\ / : * ? \" < > |\n")
            invalidSettingsNotice.setWindowTitle("Invalid Filename")
            invalidSettingsNotice.setStandardButtons(QMessageBox.Ok)
            invalidSettingsNotice.setIcon(QMessageBox.Warning)
            invalidSettingsNotice.setFont(im.popUpFont)
            invalidSettingsNotice.exec()
            return

    #Remember current trial that is open
    currentTrial = ts.currentSession.currentTrial

    #Remove '.json' if the user put it in the custom name
    if ".json" in customName:
        customName = customName.replace(".json", "")

    #Create JSON object
    fileCopy = jsCon.jsonObject

    #Update the threshold parameters
    fileCopy["header"]["thresholdSD"] = stdDevNumber
    fileCopy["header"]["thresholdMinDuration"] = minDuration
    fileCopy["header"]["minVoltage"] = minVoltage

    #Go through all of the trials, calculate the new stats, and store the newly generated data 
    numTrials = int(fileCopy["header"]["trialCount"])
    for x in range(numTrials):
        fileCopy["trials"][x]["stats"] = da.getTrialStats(minVoltage, stdDevNumber, minDuration, fileCopy["trials"][x]["samples"])

    #Convert the saved data to a JSON readable format
    fileString = json.dumps(fileCopy)

    #Open the old file
    oldFileName = jsCon.getCurrentFilename()

    #Replace oldFilename with customName (should be the same if 'Overwrite Current File' is enabled)
    newFilename = jsCon.saveFilename.replace(oldFileName, customName)

    #Open the file, write the json data, then close the file
    saveFile = open(newFilename, "w")
    saveFile.write(fileString)
    saveFile.close()

    #Open the newly created session
    im.openSession(newFilename)
    im.loadTrial(currentTrial)
    if not nameError:
        closeWindow()


#Sets the line editor to be enabled/disabled depending on the 'Save as Custom Name' option
def setFilenameEditorEnabled():
    windowWrapper.lineEdit_customSaveName.setEnabled(windowWrapper.radioButton_GenerateNew.isChecked())

#Close the dialog window
def closeWindow():
    dialogWindow.close()
