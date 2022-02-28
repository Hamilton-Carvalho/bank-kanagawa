from PyQt5 import uic,QtWidgets
from login.login import *
from withdrawal.withdrawal import *
from deposit.deposit import *
#  
#  ta trolando
#   



# transfer

screen_transfer=uic.loadUi('transfer/transfer-screen.ui')

def enable_screen_transfer():
    screen_transfer.show()
    
def desable_screen_transfer():
    screen_transfer.hide()
    
def enable_screen_balance_transfer():
    desable_screen_transfer()
    enable_screen_balance()
 
    
screen_transfer.page_transfer.clicked.connect(enable_screen_balance_transfer)
    

# transfer

#withdrawal
withdrawal=uic.loadUi('withdrawal/withdrawal-screen.ui')

def enable_screen_withdrawal():
    withdrawal.show()
    
def desable_screen_withdrawal():
    withdrawal.hide()
    
def enable_screen_balance_desable_screen_withdrawal():
    desable_screen_withdrawal()
    enable_screen_balance()
    
    
withdrawal.Button_withdrawal1_screen.clicked.connect(enable_screen_balance_desable_screen_withdrawal)
#withdrawal


#deposit

screen_deposit=uic.loadUi('deposit/deposit.ui')

def enable_screen_deposit():
    screen_deposit.show()
    
def desable_screen_deposit():
    screen_deposit.hide()
    
def enable_screen_balance_desable_screen_deposit():
    desable_screen_deposit()
    enable_screen_balance()
    
    
screen_deposit.Button_screen_deposit1.clicked.connect(enable_screen_balance_desable_screen_deposit)
    
    
#deposit

# balance
tela_balance=uic.loadUi('balance/account-balance-screen.ui')


def enable_screen_balance():
    tela_balance.show()
    
    
def desable_screen_balance():
    tela_balance.hide()
    
def screen_transfer_balance():
    tela_balance.hide()
    enable_screen_transfer()
    
def screen_withdraw():
    tela_balance.hide()
    enable_screen_withdrawal()

    
def screen_deposit1():
    tela_balance.hide()
    enable_screen_deposit()
    

    
    



tela_balance.Button_transfer_balance.clicked.connect(screen_transfer_balance)
tela_balance.Button_withdraw_balance.clicked.connect(screen_withdraw)
tela_balance.Button_deposit_balance.clicked.connect(screen_deposit1)


# balance


#login


screen_login=uic.loadUi('login/login-screen.ui')


def enable_screen_login():
    screen_login.show()
    app.exec()
    
def desable_screen_login():
    screen_login.hide()
    
def disable_login_enable_balance():
    enable_screen_balance()
    desable_screen_login()
    
screen_login.Button_Login.clicked.connect(disable_login_enable_balance)
enable_screen_login()

#login

