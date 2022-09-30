#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('task.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)
        self.lineEdit_d.setVisible(False)
        self.label_d.setVisible(False)
        self.lineEdit_x.textChanged.connect(lambda text, obj = self.lineEdit_x: self.text_changed(text, obj))

    def text_changed(self, text, obj):
        try:
            k = int(text)
            if k < 6:
                self.lineEdit_d.setVisible(False)
                self.label_d.setVisible(False)
            else:
                self.lineEdit_d.setVisible(True)
                self.label_d.setVisible(True)
        except:
            self.lineEdit_d.setVisible(False)
            self.label_d.setVisible(False)


    # Процедура решения примера
    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x < 6:
                answer = ((a + b) ** 2) / (x - 2)
            else:
                d = float(self.lineEdit_d.text())
                answer = (x * (d ** 3)) + (b ** 2)
            self.label_answer.setText('Ответ: ' + str(format(answer, '.2f')))
            self.label_answer.setStyleSheet("color: green")
        except:
            self.label_answer.setText('Ошибка!')
            self.label_answer.setStyleSheet("color: red")


    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_d.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')


# Основная часть программы
app = QApplication(sys.argv)
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
