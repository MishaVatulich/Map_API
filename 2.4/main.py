import os
import sys
from Map_API import MapAPI

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 450]


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.map_api = MapAPI()  # сама карта
        self.map_api.draw()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.pixmap = QPixmap('map.png')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp and int(self.map_api.zoom) < 17:
            self.map_api.zoom = str(int(self.map_api.zoom) + 1)
            self.map_api.draw()
            self.image.setPixmap(QPixmap('map.png'))
        elif event.key() == Qt.Key_PageDown and int(self.map_api.zoom) > 0:
            self.map_api.zoom = str(int(self.map_api.zoom) - 1)
            self.map_api.draw()
            self.image.setPixmap(QPixmap('map.png'))
        elif event.key() == Qt.Key_Left:
            pass
        elif event.key() == Qt.Key_Right:
            pass
        elif event.key() == Qt.Key_Up:
            pass
        elif event.key() == Qt.Key_Down:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
