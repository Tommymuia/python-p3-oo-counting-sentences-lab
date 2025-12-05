#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use the setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        """Returns True if value ends with a period."""
        return self.value.endswith(".")

    def is_question(self):
        """Returns True if value ends with a question mark."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark."""
        return self.value.endswith("!")

    def count_sentences(self):
        """Returns the number of sentences in the string."""
        # Split string by ., !, ? and filter out empty strings after stripping spaces
        sentences = re.split(r'[.!?]+', self.value)
        # Remove empty strings and strings with only whitespace
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
