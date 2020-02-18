import requests


class MapAPI():
    def __init__(self, coords, zoom, mod):
        api_server = "http://static-maps.yandex.ru/1.x/"
        params = {
            "ll": ",".join([coords[0], coords[1]]),
            "z": zoom,
            "l": mod
        }
        self.response = requests.get(api_server, params=params)

    def draw(self):
        # Запишем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(self.response.content)



