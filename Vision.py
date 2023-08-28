import os, io
from google.cloud import vision
import pandas as pd

def read_image(guid, base_url):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"
    url = base_url+guid + "/" #Construct the URL of the captcha image
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = url


    # annotate Image Response
    response = client.text_detection(image=image)  # returns TextAnnotation
    df = pd.DataFrame(columns=['locale', 'description'])

    texts = response.text_annotations
    for text in texts:
        #Function to extract from Image the Captcha Code.
        df = df._append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )
    try:
        if df['description'][0][0:4].isalpha():
            return df['description'][0][0:4]
        return 'FAIL'
    except:
        return 'FAIL'