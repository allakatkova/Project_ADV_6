import requests

TOKEN = 'y0_AgAAAAACEB5lAADLWwAAAADVOwmof3Hnr59kQIKqqaFV0AmPgB22Kro'
HEADERS = {'Content-Type': 'application/json',
           'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
URL = 'https://cloud-api.yandex.net/v1/disk/resources'


def check_folder(folder_name):
    result = requests.get(f'{URL}?path={folder_name}', headers=HEADERS)
    return result.status_code


def create_folder(folder_name):
    result = requests.put(f'{URL}?path={folder_name}', headers=HEADERS)
    return result.status_code
