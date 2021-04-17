import sys
from PyQt5 import  QtGui,QtCore,QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import  QApplication,QMainWindow,QPushButton,QAction,QMessageBox,QCheckBox,QComboBox,QLineEdit , QPlainTextEdit
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import DES_Mod as des

#mode 64,32,16,-1
class Window(QMainWindow):

    def __init__(self,mode):
        super(Window, self).__init__()
        loadUi('uii.ui', self)  ## load file .ui
        self.setWindowTitle("DES APP")  ## set the tile
        self.setWindowIcon(QIcon('./NS.png'))
        self.mode=64
        # slot :
        self.action64bit_Block_Size.triggered.connect(self.on_action64bit_Block_Size_clicked)
        self.action32bit_Block_Size.triggered.connect(self.on_action32bit_Block_Size_clicked)
        self.action16bit_Block_Size.triggered.connect(self.on_action16bit_Block_Size_clicked)

        self.generateBtn.clicked.connect(self.on_generateBtn_clicked)
        self.encryptBtn.clicked.connect(self.on_encryptBtn_clicked)
        self.decryptBtn.clicked.connect(self.on_decryptBtn_clicked)

    @pyqtSlot()
    def on_action64bit_Block_Size_clicked(self):
    	self.mode=64
    	self.label.setText('Key 64 Bits :')
    	self.label_5.setText('Key 64 Bits :')
    def on_action32bit_Block_Size_clicked(self):
    	# print(self.mode)
    	self.mode=32
    	# print(self.mode)
    	self.label.setText('Key 32 Bits :')
    	self.label_5.setText('Key 32 Bits :')
    def on_action16bit_Block_Size_clicked(self):
    	self.mode=16
    	self.label.setText('Key 16 Bits :')
    	self.label_5.setText('Key 16 Bits :')
    def on_generateBtn_clicked(self):
        # print(self.mode)
        if self.mode==64:
            Key_str = des.Generate_Key_64()
        elif self.mode==32:
            Key_str = des.Generate_Key_32()
        elif self.mode==16:
            Key_str = des.Generate_Key_16()
        # print(len(Key_str))
        self.keyLine.setText(Key_str)
        self.keyLine2.setText(Key_str)
    def on_encryptBtn_clicked(self):
        Key_str = self.keyLine.text()
        rounds=16
        seed=1707
        mask=0
        des_o  = des.DES_M(self.mode,rounds,Key_str,seed,0)
        # print('plain',self.plaintextLine.text())
        Ciphertext , cypher_dash = des_o.encrypt(self.plaintextLine.text())
        # print("Encrypt : %r" %Ciphertext)
        # print('x')
        self.encryptedLine.setText(Ciphertext)
        self.ciphertextLine.setText(Ciphertext)
    def on_decryptBtn_clicked(self):
        Key_str  = self.keyLine2.text()
        rounds=16
        seed=1707
        mask=0
        des_o = des.DES_M(self.mode,rounds,Key_str,seed,1&mask)
        Plaintext , cypher_dash2 = des_o.decrypt(self.encryptedLine.text())
        # Plaintext = des.DES_Decrypt(self.ciphertextLine.text(),Key_str)
        # print(Plaintext)
        self.plaintextLine2.setText(Plaintext)


app = QApplication(sys.argv)
GUI = Window(64)
GUI.show()
sys.exit(app.exec_())
#