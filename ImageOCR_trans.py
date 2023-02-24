import os
from google.cloud import vision
import cv2
import numpy as np
from PIL import Image
from googletrans import Translator


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/vision API key/basic-thinker-365113-0522ec8ca559.json"
print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

def CloudVisionTextExtractor(handwritings):
    # convert image from numpy to bytes for submission to Google Cloud Vision
    _, encoded_image = cv2.imencode('.png', handwritings)
    content = encoded_image.tobytes()
    image = vision.Image(content=content)

    # feed handwriting image segment to the Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    response = client.document_text_detection(image=image)

    return response


def getTextFromVisionResponse(response):
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
    #translations for the OCR text
    translator = Translator()
    return translator.translate(text, dest=target_language).text


def temp_selection(lang):
    result = ""
    if lang == "english":
        result = "en"

    elif lang == "hindi":
        result = "hi"

    elif lang == "gujarati":
        result = "gu"

    return result


images = np.array(Image.open("6. sample.png"))
response = CloudVisionTextExtractor(images)
ocr = getTextFromVisionResponse(response)
    
lang = temp_selection("english")
trans = translate_text(ocr, lang)

# print(ocr)
# print(trans)

if __name__ == "__main__":
    main()
