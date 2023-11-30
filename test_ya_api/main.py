import requests

class YaFolder:
    def __init__(self, token: str):
        self.token = token

    def make_folder(self, name_folder: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/"
        params = {
             "path": name_folder
        }
        headers = {
            "Authorization": self.token
        }
        response = requests.put(url, headers=headers, params=params)
        return response.status_code

    def inf_folder(self, name_folder: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/"
        params = {
             "path": name_folder
        }
        headers = {
            "Authorization": self.token
        }
        response = requests.get(url, headers=headers, params=params)
        return response.status_code

if __name__ == '__main__':
    token = ""
    new_folder = YaFolder(token)
    result = new_folder.make_folder('test_folder')
    print(result)