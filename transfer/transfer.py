from PyQt5 import uic,QtWidgets
from balance.balance import *
app=QtWidgets.QApplication([])


screen_transfer=uic.loadUi('transfer/transfer-screen.ui')

def enable_screen_transfer():
    screen_transfer.show()
    
def desable_screen_transfer():
    screen_transfer.hide()
    
def enable_screen_balance_transfer():
    desable_screen_transfer()
 
    
screen_transfer.page_transfer.clicked.connect(enable_screen_balance_transfer)
    