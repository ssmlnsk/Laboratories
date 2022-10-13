# from facade import Facade
from PyQt5 import QtWidgets
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QDialog
import sys
import logging
from PyQt5.QtWidgets import QMessageBox

logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.facade = Facade()
        self.ui = uic.loadUi("forms/main.ui", self)

        self.ui.btn_exit.clicked.connect(self.exit)

    def exit(self):
        self.hide()
        self.open_auth()

    def open_auth(self):
        dialog = DialogLog(self)
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()


class DialogLog(QDialog):
    def __init__(self, parent=None):
        super(DialogLog, self).__init__(parent)
        self.ui = uic.loadUi("forms/logWindow.ui", self)
        # self.facade = Facade()

    def open_auth(self):
        auth_log = self.ui.auth_log.text()
        auth_pas = self.ui.auth_pas.text()

        if auth_log == '' or auth_pas == '':
            logging.log(logging.INFO, 'Ошибка. Заполните все поля!')
            self.mes_box('Заполните все поля!')

        else:
            login = "ф"
            password = "ф"
            #login, password = self.parent().facade.get_for_authorization(auth_log)

            if auth_log != login:
                self.mes_box('Такого пользователя нет')

            elif auth_log == login:
                if auth_pas != password:
                    logging.log(logging.INFO, 'Ошибка. Неправильно введены данные.')
                    self.mes_box('Неправильно введены данные.')

                elif password == auth_pas:
                    #self.parent().updateTableHistory()
                    logging.log(logging.INFO, 'Вход выполнен')
                    self.parent().hide()
                    self.parent().show()
                    self.close()


# class DialogReg(QDialog):
#     def __init__(self, parent=None):
#         super(DialogReg, self).__init__(parent)
#         self.ui = uic.loadUi("regWindow.ui", self)
#         self.facade = Facade()

class Builder:
    """
    Паттерн строитель.
    Это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
    """
    def __init__(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()
        self.auth()

    def auth(self):
        self.window.open_auth()
        self.qapp.exec()


if __name__ == '__main__':
    B = Builder()
