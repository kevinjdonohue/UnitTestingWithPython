class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        if name not in self.entries and number not in self.entries.values() and not self.is_a_prefix(number):
            self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True

    def get_all_names(self):
        return self.entries.keys()

    def get_all_numbers(self):
        return self.entries.values()

    def is_a_prefix(self, potential_prefix):
        is_prefix = False
        for number in self.entries.values():
            if potential_prefix in number or number in potential_prefix:
                is_prefix = True
                break

        return is_prefix
