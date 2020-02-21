import requests


class MapAPI():
    def __init__(self):
        self.cords = ['140.232', '40.214']
        self.zoom = '15'
        self.mod = 'sat'
        self.api_server = "http://static-maps.yandex.ru/1.x/"

    def draw(self):  # обновляет файл с картой
        params = {
            "ll": ",".join([self.cords[0], self.cords[1]]),
            "z": self.zoom,
            "l": self.mod
        }
        response = requests.get(self.api_server, params=params)
        # Запишем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
