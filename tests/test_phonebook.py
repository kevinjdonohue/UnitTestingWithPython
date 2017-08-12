import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        # arrange
        phonebook = Phonebook()
        expected = "12345"
        phonebook.add("Bob", expected)

        # act
        actual = phonebook.lookup("Bob")

        # assert
        self.assertEqual(expected, actual)
