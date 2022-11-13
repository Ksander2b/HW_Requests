import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.base_host = 'https://cloud-api.yandex.net:443/'
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str, ya_path):
        uri = 'v1/disk/resources/upload'
        request_url = self.base_host + uri
        params = {'path':ya_path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        response_2 = requests.put(response.json()['href'], data=open(file_path, 'rb'), headers=self.get_headers())
        if response_2.status_code == 201:
            print('Загрузка произошла успешно!')


if __name__ == '__main__':
    path_to_file = '/Users/aleksandrbogatyrev/Documents/image_2022-10-07_11-17-31.png'
    name = os.path.basename(path_to_file)
    token = ...
    uploader = YaUploader(token)
    uploader.upload(path_to_file, f'/{name}')

    