import unittest
from main import  get_all_mentors, mentors, get_unique_names

class TestMentorFunctions(unittest.TestCase):

    def test_get_all_mentors(self):
        expected_count = 42  # Если к примеру 42 значение меньше чем в списке 
        all_mentors = get_all_mentors(mentors)
        self.assertEqual(len(all_mentors), expected_count)

    def test_get_unique_names(self):
        all_mentors = get_all_mentors(mentors)
        unique_names = get_unique_names(all_mentors)
        expected_names = sorted(set([name.split()[0] for name in all_mentors]))
        self.assertEqual(unique_names, expected_names)

    def test_unique_names_order(self):
        all_mentors = get_all_mentors(mentors)
        sorted_unique_names = get_unique_names(all_mentors)
        self.assertEqual(sorted_unique_names, sorted(set(sorted_unique_names)))  # Проверяем, что имена отсортированы

if __name__ == '__main__':
    unittest.main()