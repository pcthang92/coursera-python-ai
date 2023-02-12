import unittest
from translator import english_to_french, french_to_english


class TestLanguageTranslator(unittest.TestCase):
    def test_englishToFrench_null_input(self):
        result = english_to_french(None)
        self.assertEqual(result, "")

    def test_englishToFrench_hello_bonjour(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

    def test_englishToFrench_hello_not_merci(self):
        result = english_to_french("Hello")
        self.assertNotEqual(result, "Merci")

    def test_frenchToEnglish_null_input(self):
        result = french_to_english(None)
        self.assertEqual(result, "")

    def test_frenchToEnglish_bonjour_hello(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

    def test_frenchToEnglish_bonjour_not_hi(self):
        result = french_to_english("Bonjour")
        self.assertNotEqual(result, "Hi")


if __name__ == '__main__':
    unittest.main()
