import unittest
from translator import english_to_french, french_to_english


class TestLanguageTranslator(unittest.TestCase):
    def test_englishToFrench_null_input(self):
        result = english_to_french(None)
        self.assertEqual(result, "")

    def test_englishToFrench(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

    def test_frenchToEnglish_null_input(self):
        result = french_to_english(None)
        self.assertEqual(result, "")

    def test_frenchToEnglish(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")


if __name__ == '__main__':
    unittest.main()
