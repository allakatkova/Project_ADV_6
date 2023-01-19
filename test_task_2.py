import create_folder_ydisk as cfyd
from unittest.case import TestCase

FOLDER_NAME = 'folder_test'


class TestYandexFolder(TestCase):

    def test_folder_check(self):
        self.assertTrue(cfyd.check_folder(FOLDER_NAME) == 404,
                        f'Папка {FOLDER_NAME} создана на Я.Диске')

    def test_folder_create(self):
        self.assertTrue(cfyd.create_folder(FOLDER_NAME) == 201,
                        f'Папка {FOLDER_NAME} не найдена на Я.Диске')
