import unittest
from main import most_frequent 

class TestMostFrequent(unittest.TestCase):

    def test_most_frequent_with_common_elements(self):
        self.assertEqual(most_frequent([1, 2, 3, 1, 2, 1]), 1)
        self.assertEqual(most_frequent([2, 2, 3, 2, 3, 1]), 2)

    def test_most_frequent_single_element(self):
        self.assertEqual(most_frequent([5]), 5)

    def test_most_frequent_with_negative_numbers(self):
        self.assertEqual(most_frequent([-1, -1, 2, 2, -1]), -1)

    def test_most_frequent_with_multiple_max(self):
        # Если есть несколько элементов с одинаковой максимальной частотой, 
        # будет возвращен первый найденный
        self.assertEqual(most_frequent([1, 2, 3, 1, 2]), 1)

    def test_most_frequent_empty_list(self):
        # Тест для пустого списка
        with self.assertRaises(ValueError):
            most_frequent([])

if __name__ == '__main__':
    unittest.main()