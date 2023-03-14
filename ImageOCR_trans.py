import os
from google.cloud import vision
import cv2
import numpy as np
from PIL import Image
from googletrans import Translator

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/vision API key/polyglot-379405-1cb386f1dbbd.json"

def extract_text_from_image(image_path):
    # Load the image
    try:
        image = cv2.imread(image_path)
    except Exception as e:
        print(f"Error: {e}")
        return None

    # Convert image from numpy to bytes for submission to Google Cloud Vision
    _, encoded_image = cv2.imencode('.png', image)
    content = encoded_image.tobytes()
    vision_image = vision.Image(content=content)

    # Feed image to the Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    try:
        response = client.document_text_detection(image=vision_image)
    except Exception as e:
        print(f"Error: {e}")
        return None

    # Extract the text from the response
    texts = []
    for page in response.full_text_annotation.pages:
        for i, block in enumerate(page.blocks):
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    texts.append(word_text)

    output = ' '.join(texts)
    return output


def translate_text(text, target_language):
    # Translate the text to the target language
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
    except Exception as e:
        print(f"Error: {e}")
        return None

    return translation.text



def get_language_code(language):
    # Get the language code for a given language name
    language_codes = {"english": "en", "hindi": "hi", "gujarati": "gu", "spanish": "es", "arabic": "ar"}
    try:
        return language_codes[language]
    except KeyError:
        print(f"Error: Language {language} not supported.")
        return None


if __name__ == "__main__":
    # Define the image path and target language
    image_path = "C:\\Users\\kshit\\Downloads\\ssss.jpg"
    target_language = "arabic"

    # Extract the text from the image
    ocr_text = extract_text_from_image(image_path)
    if not ocr_text:
        print("Error: Text extraction failed.")
        exit()

    # Translate the text to the target language
    language_code = get_language_code(target_language)
    if not language_code:
        exit()
    translation = translate_text(ocr_text, language_code)
    if not translation:
        print("Error: Translation failed.")
        exit()

    # Print the original text and translated text
    # print("Original text:")
    print(ocr_text)
    # print("Translated text:")
    print(translation)
