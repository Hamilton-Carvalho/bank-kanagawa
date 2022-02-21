from PyQt5 import uic,QtWidgets
from transfer.transfer import *
from withdrawal.withdrawal import *
from deposit.deposit import *

app=QtWidgets.QApplication([])

tela_balance=uic.loadUi('balance/account-balance-screen.ui')



def enable_screen_balance():
    tela_balance.show()
    
    
def desable_screen_balance():
    tela_balance.hide()
    
def screen_transfer():
    tela_balance.hide()
    enable_screen_transfer()
    
def screen_withdraw():
    tela_balance.hide()
    enable_screen_withdrawal()

tela_balance.Button_transfer_balance.clicked.connect(screen_transfer)
tela_balance.Button_withdraw_balance.clicked.connect(screen_withdraw)



    