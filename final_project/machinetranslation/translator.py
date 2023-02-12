"""Testing IBM Language Translator Service"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)


def english_to_french(english_text):
    """Translate English text to French"""
    if english_text is None:
        return ""
    translation = LANGUAGE_TRANSLATOR.translate(
        english_text, source="en", target="fr")
    french_text = ""
    if len(translation.result['translations']) > 0:
        french_text = translation.result['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """Translate French text to English"""
    if french_text is None:
        return ""
    translation = LANGUAGE_TRANSLATOR.translate(
        french_text, source="fr", target="en")
    english_text = ""
    if len(translation.result['translations']) > 0:
        english_text = translation.result['translations'][0]['translation']
    return english_text
