from PyQt5 import uic,QtWidgets


screen_deposit=uic.loadUi('deposit/deposit.ui')

def enable_screen_deposit():
    screen_deposit.show()
    
def desable_screen_deposit():
    screen_deposit.hide()
    