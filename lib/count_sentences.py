#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace '!', '?' with '.' to standardize sentence endings
        standardized_value = re.sub(r'[!?.]', '.', self.value)
        
        # Split the string on '.'
        sentences = standardized_value.split('.')
        
        # Filter out empty strings
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return len(sentences)

# Example usage
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # Output: 3

string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
print(string.count_sentences())  # Output: 4

# Test the invalid value assignment
string.value = 123  # Should print: The value must be a string.

# Test is_question method
print(MyString("Is anybody there?").is_question())  # Should return True
print(MyString("This is a statement.").is_question())  # Should return False

# Test is_exclamation method
print(MyString("It's me!").is_exclamation())  # Should return True
print(MyString("This is a statement.").is_exclamation())  # Should return False
