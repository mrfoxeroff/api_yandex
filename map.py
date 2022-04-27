from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
import sys
import requests
from py_files.api_yandex import Ui_ApiYandex
from PyQt5.QtCore import Qt


class ApiYandex(QWidget, Ui_ApiYandex):
    def __init__(self, coords):
        super().__init__()
        self.setupUi(self)
        self.coords = coords.split(', ')
        self.coords = [float(item) for item in self.coords]
        print(self.coords)
        self.z = 14
        self.l = 'sat'
        self.response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll='
                                     f'{str(self.coords[0])},{str(self.coords[1])}'
                                     f'&size=450,450&z={self.z}&l={self.l}')
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(self.response.content)
        self.pixmap = QPixmap(self.map_file)
        self.map.setPixmap(self.pixmap)
        self.do_map_type.clicked.connect(self.check_l)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageDown:
            self.z -= 1
            self.do_picture()
        if event.key() == Qt.Key_PageUp:
            self.z += 1
            self.do_picture()
        if event.key() == Qt.Key_Up:
            self.move_picture(event.key())
        if event.key() == Qt.Key_Down:
            self.move_picture(event.key())
        if event.key() == Qt.Key_Left:
            self.move_picture(event.key())
        if event.key() == Qt.Key_Right:
            self.move_picture(event.key())

    def do_picture(self):
        self.response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll='
                                     f'{str(self.coords[0])},{str(self.coords[1])}'
                                     f'&size=450,450&z={self.z}&l={self.l}')
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(self.response.content)
        self.pixmap = QPixmap(self.map_file)
        self.map.setPixmap(self.pixmap)

    def move_picture(self, button):
        if button == Qt.Key_Up:
            self.coords[1] += 0.0005 * (20 - self.z)
            self.do_picture()
        if button == Qt.Key_Down:
            self.coords[1] -= 0.0005 * (20 - self.z)
            self.do_picture()
        if button == Qt.Key_Right:
            self.coords[0] += 0.0005 * (20 - self.z)
            self.do_picture()
        if button == Qt.Key_Left:
            self.coords[0] -= 0.0005 * (20 - self.z)
            self.do_picture()

    def check_l(self):
        if self.map_type.currentText() == 'Спутник':
            self.l = 'sat'
            self.do_picture()
        if self.map_type.currentText() == 'Гибрид':
            self.l = 'skl'
            self.do_picture()
        if self.map_type.currentText() == 'Схема':
            self.l = 'map'
            self.do_picture()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    api = ApiYandex(input())
    api.show()
    sys.exit(app.exec())

