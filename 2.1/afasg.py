def keyPressEvent(self, event):
    if event.key() == Qt.Key_PageUp and int(self.map_api.zoom) < 20:
        self.map_api.zoom = str(int(self.map_api.zoom) + 1)
        self.map_api.draw()
    elif event.key() == Qt.Key_PageDown and int(self.map_api.zoom) > 0:
        self.map_api.zoom = str(int(self.map_api.zoom) - 1)
        self.map_api.draw()
    elif event.key() == Qt.Key_Left:
        pass
    elif event.key() == Qt.Key_Right:
        pass
    elif event.key() == Qt.Key_Up:
        pass
    elif event.key() == Qt.Key_Down:
        pass
