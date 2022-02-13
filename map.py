from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
import sys
import requests
from py_files.api_yandex import Ui_ApiYandex
from PyQt5.QtCore import Qt


class ApiYandex(QWidget, Ui_ApiYandex):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coords = '40.692077,55.614980'
        self.z = 14
        self.response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={self.coords}'
                                     f'&size=450,450&z={self.z}&l=sat')
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(self.response.content)
        self.pixmap = QPixmap(self.map_file)
        self.map.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.z -= 1
            self.do_picture()
        if event.key() == Qt.Key_Up:
            self.z += 1
            self.do_picture()

    def do_picture(self):
        self.response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={self.coords}'
                                     f'&size=450,450&z={self.z}&l=sat')
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(self.response.content)
        self.pixmap = QPixmap(self.map_file)
        self.map.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    api = ApiYandex()
    api.show()
    sys.exit(app.exec())

