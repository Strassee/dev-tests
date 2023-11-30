from unittest import TestCase

from main import YaFolder

class TestYaFolder(TestCase):
    
    def test_ya_folder(self):
        token = ""
        name_folder = 'test_folder'
        new_folder = YaFolder(token)
        result_make = new_folder.make_folder(name_folder)
        result_inf = new_folder.inf_folder(name_folder)
        # self.assertEqual(result_make, 201)
        self.assertGreaterEqual(result_make, 400)
        self.assertEqual(result_inf, 200)

