import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
	def __init__(self):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Critical)
		msg.setText("**WARNING: POTENTIALLY MALICIOUS TARGET IP**")
		msg.setWindowTitle("Warning")
		msg.exec_()

