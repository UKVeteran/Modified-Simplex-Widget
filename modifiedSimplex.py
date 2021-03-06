from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.optimize import linprog
from numpy import multiply

class Ui_MainWindow(object):
    def new(self):
        self.msg.setWindowTitle("New")
        self.msg.setText("New Calculation?")
        op = self.msg.exec_()
        if op == QtWidgets.QMessageBox.Ok:
            self.cbObjetivo.setCurrentIndex(0)
            self.txF1.clear()
            self.txF2.clear()
            self.txF3.clear()
            self.txF4.clear()
            self.txR11.clear()
            self.txR12.clear()
            self.txR13.clear()
            self.txR14.clear()
            self.cbS1.setCurrentIndex(0)
            self.txB1.clear()
            self.txResult.clear()
            self.tabWidget.setCurrentIndex(0)
            self.statusbar.clearMessage()

            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(690, 330)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 668, 281))
        self.tabWidget.setObjectName("tabWidget")

#Model Tab (2var2const)
        self.tabModel = QtWidgets.QWidget()
        self.tabModel.setObjectName("tabModel")

        
        self.label_3 = QtWidgets.QLabel(self.tabModel)
        self.label_3.setGeometry(QtCore.QRect(330, 40, 31, 21))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.label_19 = QtWidgets.QLabel(self.tabModel)
        self.label_19.setGeometry(QtCore.QRect(10, 70, 641, 21))
        self.label_19.setAutoFillBackground(False)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label = QtWidgets.QLabel(self.tabModel)
        self.label.setGeometry(QtCore.QRect(220, 10, 141, 21))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tabModel)
        self.label_4.setGeometry(QtCore.QRect(460, 40, 31, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.tabModel)
        self.label_10.setGeometry(QtCore.QRect(500, 100, 21, 21))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tabModel)
        self.label_11.setGeometry(QtCore.QRect(110, 130, 31, 21))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.tabModel)
        self.label_6.setGeometry(QtCore.QRect(50, 40, 41, 21))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.tabModel)
        self.label_5.setGeometry(QtCore.QRect(590, 40, 21, 21))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.tabModel)
        self.label_9.setGeometry(QtCore.QRect(240, 100, 31, 21))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.tabModel)
        self.label_7.setGeometry(QtCore.QRect(370, 100, 31, 21))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.tabModel)
        self.label_12.setGeometry(QtCore.QRect(240, 130, 31, 21))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.tabModel)
        self.label_15.setGeometry(QtCore.QRect(110, 160, 31, 21))
        self.label_15.setAutoFillBackground(False)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.tabModel)
        self.label_18.setGeometry(QtCore.QRect(500, 160, 21, 21))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(self.tabModel)
        self.label_17.setGeometry(QtCore.QRect(370, 160, 31, 21))
        self.label_17.setAutoFillBackground(False)
        self.label_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.tabModel)
        self.label_16.setGeometry(QtCore.QRect(240, 160, 31, 21))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_16.setObjectName("label_16")
        self.label_13 = QtWidgets.QLabel(self.tabModel)
        self.label_13.setGeometry(QtCore.QRect(370, 130, 31, 21))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabModel)
        self.label_14.setGeometry(QtCore.QRect(500, 130, 21, 21))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setObjectName("label_14")
        self.label_2 = QtWidgets.QLabel(self.tabModel)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 31, 21))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.tabModel)
        self.label_8.setGeometry(QtCore.QRect(110, 100, 31, 21))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setObjectName("label_8")

        self.tabWidget.addTab(self.tabModel, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuMain.addAction(self.actionNew)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.action)
        self.menubar.addAction(self.menuMain.menuAction())
        self.msg = QtWidgets.QMessageBox(MainWindow)
        self.msg.setIcon(QtWidgets.QMessageBox.Question)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)



#Result Tab 1
        self.tabResult = QtWidgets.QWidget()
        self.tabResult.setObjectName("tabResult")
        self.txResult = QtWidgets.QTextEdit(self.tabResult)
        self.txResult.setGeometry(QtCore.QRect(0, 0, 661, 251))
        self.txResult.setObjectName("txResult")
        self.txResult.setReadOnly(True)
        self.txResult.setFontPointSize(16)
        self.tabWidget.addTab(self.tabResult, "")


        
#Model Tab (3var3const)
        self.tab33 = QtWidgets.QWidget()
        self.tab33.setObjectName("tab33")
        self.tabWidget.addTab(self.tab33,"")
        

#Result Tab 2
        self.tabResult1 = QtWidgets.QWidget()
        self.tabResult1.setObjectName("tabResult1")
        self.txResult1 = QtWidgets.QTextEdit(self.tabResult1)
        self.txResult1.setGeometry(QtCore.QRect(0, 0, 661, 251))
        self.txResult1.setObjectName("txResult1")
        self.txResult1.setReadOnly(True)
        self.txResult1.setFontPointSize(16)
        self.tabWidget.addTab(self.tabResult1, "")
        
        

        
#Model Tab (4var1const)
        self.tab41 = QtWidgets.QWidget()
        self.tab41.setObjectName("tab41")
        self.tabWidget.addTab(self.tab41,"")
        

#Result Tab 3
        self.tabResult2 = QtWidgets.QWidget()
        self.tabResult2.setObjectName("tabResult2")
        self.txResult2 = QtWidgets.QTextEdit(self.tabResult2)
        self.txResult2.setGeometry(QtCore.QRect(0, 0, 661, 251))
        self.txResult2.setObjectName("txResult2")
        self.txResult2.setReadOnly(True)
        self.txResult2.setFontPointSize(16)
        self.tabWidget.addTab(self.tabResult2, "")
        
        



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.action.triggered.connect(lambda : MainWindow.close())
        self.actionNew.triggered.connect(lambda : self.new())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simplex Solvers"))
#Tab for 2var2cont
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabModel), _translate("MainWindow", "2var2const"))
#Tab Result 1
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResult), _translate("MainWindow", "Result"))
#Tab Result 2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResult1), _translate("MainWindow", "Result"))        
#Tab for 4var1const
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab41), _translate("MainWindow", "4var1const"))        
#Tab Result 3
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResult2), _translate("MainWindow", "Result"))        
#Tab for 3var3const
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab33), _translate("MainWindow", "3var3const"))        


        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action.setText(_translate("MainWindow", ""))
        self.action.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon("python.ico"))

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())