from PyQt5 import uic,QtWidgets
from balance.balance import *
app=QtWidgets.QApplication([])


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
    