import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):
    def setUp(self):
        # arrange
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        # arrange
        expected_number = "12345"
        name = "Bob"
        self.phonebook.add(name, expected_number)

        # act
        actual_number = self.phonebook.lookup(name)

        # assert
        self.assertEqual(expected_number, actual_number)

    def test_missing_entry_raises_KeyError(self):
        # act and assert
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertTrue(phonebook_is_consistent)

    def test_phonebook_with_normal_entries_is_consistent(self):
        # arrange
        self.phonebook.add("Bob", "123435")
        self.phonebook.add("Mary", "012345")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertTrue(phonebook_is_consistent)

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        # arrange
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertFalse(phonebook_is_consistent, "Should be False because phonebook has duplicate phone number")

    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        # arrange
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertFalse(phonebook_is_consistent, "Should be False because phonebook contains prefixed numbers")
