#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value=value

    def get_value(self):
        return self._value

    def set_value(self,value):
        if isinstance(value,str):
            self._value=value
        else:
            print("The value must be a string.") 

    value = property(get_value,set_value)                       
    def is_sentence(self):
        if self._value and self._value[-1] == '.':
           return True
        else:
            return False

    def is_question(self):
        if self._value and self._value[-1] == '?':
           return True
        else:
            return False

    def is_exclamation(self):
        if self._value and self._value[-1] == '!':
            return True
        else:
            return False
    def count_sentences(self):
        initial_string = self._value.replace('!', '.')
        new_string = initial_string.replace('?', '.')

        sentence_list = new_string.split('.')
        sentence_list = [n for n in sentence_list if n]

        return len(sentence_list)                

             
  
