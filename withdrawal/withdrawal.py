from PyQt5 import uic,QtWidgets


withdrawal=uic.loadUi('withdrawal/withdrawal-screen.ui')

def enable_screen_withdrawal():
    withdrawal.show()
    
def desable_screen_withdrawal():
    withdrawal.hide()