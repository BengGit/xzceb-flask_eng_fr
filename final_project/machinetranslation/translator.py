import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version='2023-04-29',
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(english_text):
    french_text = None
    if(english_text != None):
        translation = translator.translate(
            text=english_text,
            source='en',
            target='fr'
        ).get_result()

        french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    english_text = None
    if(french_text != None):
        translation = translator.translate(
            text=french_text,
            source='fr',
            target='en'
        ).get_result()

        english_text = translation['translations'][0]['translation']

    return english_text
