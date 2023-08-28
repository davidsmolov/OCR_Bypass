Automated Captcha Bypass using Google VisionAI OCR
Welcome to the OCR Bypass project, where we explore an intriguing experiment involving the Google VisionAI API to navigate past website captchas. Please note that this project is intended for educational purposes.

Prerequisites
Before diving into this script, ensure you have the following set up:

Google Cloud SDK
Python 3.7 or higher
Google Cloud Vision API
Obtain a ServiceAccountToken.json from Google Cloud
Getting Started
python
Copy code
victim_email = "{{victim@victim.com}}"  # Replace with the target victim's email address
base_url = "{{Base_URL}}"  # Modify with the URL of the password reset page
captcha_refresh_url = '{{Captcha_Refresh_Page}}'  # Adjust to the URL of the captcha refresh page

headers = {
    'Host': '{{Host}}',  # Set to the host of the password reset page
    # Include any other necessary headers for the password reset request
    'Connection': 'close'
}
Usage Example:
Step 1: Understand the Captcha Mechanism

Step 1
<img width="670" alt="2" src="https://github.com/davidsmolov/OCR_Bypass/assets/122476428/9a97e88e-402e-448e-9d20-ad6b08231598">



Step 2: Configure the Script and Initiate the Attack

Step 2
<img width="669" alt="1" src="https://github.com/davidsmolov/OCR_Bypass/assets/122476428/7bd672e4-6669-44e3-a67a-76dc680a05b6">

Step 3: Witness Automated Captcha Bypass in Action

Step 3
<img width="901" alt="3" src="https://github.com/davidsmolov/OCR_Bypass/assets/122476428/f9af85eb-17c4-495a-a3ed-8ce4f7a9461a">

Contributing
A big shoutout to Tal Argoni for providing the opportunity to contribute to this project.

License
Copyright © 2023 David Smolovich.
This code is made available under the terms of the license. Please use it exclusively for educational purposes. We encourage learning and responsible use of technology.
