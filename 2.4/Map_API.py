import requests


class MapAPI():
    def __init__(self):
        self.cords = ['135.232', '45.214']
        self.zoom = '15'
        self.mod = 0  # вид карты
        self.api_server = "http://static-maps.yandex.ru/1.x/"

    def draw(self):  # обновляет файл с картой
        if self.mod % 3 == 0:
            map_kind = 'sat'
        elif self.mod % 3 == 1:
            map_kind = 'map'
        elif self.mod % 3 == 2:
            map_kind = 'skl'
        params = {
            "ll": ",".join([self.cords[0], self.cords[1]]),
            "z": self.zoom,
            "l": map_kind
        }
        response = requests.get(self.api_server, params=params)
        # Запишем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
