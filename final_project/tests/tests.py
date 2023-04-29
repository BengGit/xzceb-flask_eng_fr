
import sys
import os
import unittest

# Get the absolute path to the directory containing this file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the directory containing translator.py to the Python path
translator_dir = os.path.join(current_dir, '../machinetranslation')
sys.path.append(translator_dir)

# This is a false negative please ignore this error
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def test_english_to_french_null_input(self):
        self.assertEqual(english_to_french(None), None)
    
    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_french_to_english_null_input(self):
        self.assertEqual(french_to_english(None), None)
    
    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
if __name__ == '__main__':
    unittest.main()
