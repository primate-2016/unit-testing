class Phonebook():
    
    def __init__(self):
        self.phonebook_entries = {}

    def add(self, name, phone_number):
        self.phonebook_entries[name] = phone_number
    
    def lookup(self, name):
        return self.phonebook_entries[name]