import unittest
from main import get_name, get_directory, directories, add

class TestDocumentManagement(unittest.TestCase):

    def test_get_name_existing_document(self):
        self.assertEqual(get_name("10006"), "Аристарх Павлов")
        self.assertEqual(get_name("2207 876234"), "Василий Гупкин")

    def test_get_name_non_existing_document(self):
        self.assertEqual(get_name("99999"), "Документ не найден")
        self.assertEqual(get_name("12345"), "Документ не найден")

    def test_get_directory_existing_document(self):
        self.assertEqual(get_directory("11-2"), '1')
        self.assertEqual(get_directory("10006"), '2')
    
    def test_get_directory_non_existing_document(self):
        self.assertEqual(get_directory("99999"), 'Полки с таким документом не найдено')
        self.assertEqual(get_directory("12345"), 'Полки с таким документом не найдено')

    def test_add_new_document_to_existing_shelf(self):
        add('international passport', '311 020203', 'Александр Пушкин', '3')
        self.assertIn('311 020203', directories['3'])
        self.assertEqual(get_name('311 020203'), 'Александр Пушкин')


    # Пример допущенная ошибка  AssertionError: 'Петя Лисицын' != 'Документ не найден'
    def test_add_new_document_to_new_shelf(self):
        add('birth certificate', '311 020204', 'Петя Лисицын', '4')
        self.assertIn('311 020204', directories['4'])
        self.assertEqual(get_name('311 020204'), 'Документ не найден')  

if __name__ == '__main__':
    unittest.main()