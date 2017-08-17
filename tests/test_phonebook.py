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
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertTrue(phonebook_is_consistent)

    def test_phonebook_with_duplicate_numbers_is_consistent(self):
        # arrange
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertEqual(1, len(self.phonebook.entries), "Should be len of 1 because duplicate phone number rejected")
        self.assertEqual("Bob", list(self.phonebook.entries.keys())[0], "Should be Bob because Mary was rejected")
        self.assertTrue(phonebook_is_consistent, "Should be True because phonebook add rejects duplicate phone numbers")

    def test_phonebook_with_duplicate_names_is_consistent(self):
        # arrange
        self.phonebook.add("Mary", "12345")
        self.phonebook.add("Mary", "678900")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertEqual(1, len(self.phonebook.entries), "Should be len of 1 because duplicate name rejected")
        self.assertEqual("Mary", list(self.phonebook.entries.keys())[0],
                         "Should be Mary because second Mary was rejected")
        self.assertTrue(phonebook_is_consistent, "Should be True because phonebook add rejects duplicate names")

    def test_phonebook_with_numbers_that_prefix_one_another_is_consistent(self):
        # arrange
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertEqual(1, len(self.phonebook.entries), "Should be len of 1 because duplicate name rejected")
        self.assertEqual("Bob", list(self.phonebook.entries.keys())[0],
                         "Should be Bob because second entry Mary was rejected")
        self.assertTrue(phonebook_is_consistent, "Should be True because phonebook add rejects number prefixes")

    def test_phonebook_with_numbers_that_contain_one_another_is_consistent(self):
        # arrange
        self.phonebook.add("Mary", "123")
        self.phonebook.add("Bob", "12345")

        # act
        phonebook_is_consistent = self.phonebook.is_consistent()

        # assert
        self.assertEqual(1, len(self.phonebook.entries), "Should be len of 1 because duplicate name rejected")
        self.assertEqual("Mary", list(self.phonebook.entries.keys())[0],
                         "Should be Mary because Bob was rejected")
        self.assertTrue(phonebook_is_consistent, "Should be True because phonebook add rejects number contained in others")

    def test_phonebook_adds_names_and_numbers(self):
        # arrange
        self.phonebook.add("Sue", "12345")

        # act
        names = self.phonebook.get_all_names()
        numbers = self.phonebook.get_all_numbers()

        # assert
        self.assertIn("Sue", names, "Should contain the name Sue because we just added it")
        self.assertIn("12345", numbers, "Should contain the number 12345 because we just added it")
