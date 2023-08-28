# OCR Bypass

This is a script that uses the Google VisionAI API to bypass the OCR on a website. It is intended to be used for educational purposes only.

## Prequisites

Before you can use this script, you will need to install the following:
Google Cloud SDK
Python 3.7
Google Cloud Vision API
Get a ServiceAccountToken.json

## Usage

```python
mail = "{{victim@victim.com}}" # Change this to the email address of the victim
base_url = "{{Base_URL}}"  # Change this to the URL of the password reset page
refresh_url = '{{Catpcha Refresh Page}}' # Change this to the URL of the captcha refresh page

headers = {
    'Host': '{{Host}}', # Change this to the host of the password reset page
    #Add any other headers that are required to send the password reset request
    'Connection': 'close'
}

```

## Contributing

Thanks to Tal Argoni for the opprotunity to work on this project.



## License

Copyright © 2023 David Smolovich.
Feel free to use this code for educational purposes only.