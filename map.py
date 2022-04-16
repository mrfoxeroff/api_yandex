from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
import sys
import requests
from py_files.api_yandex import Ui_ApiYandex


class ApiYandex(QWidget, Ui_ApiYandex):
    def __init__(self, coords):
        super().__init__()
        self.setupUi(self)
        self.coords = coords
        response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={self.coords}'
                                f'&size=450,450&z=14&l=sat')
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(map_file)
        self.map.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    api = ApiYandex(input())
    api.show()
    sys.exit(app.exec())

