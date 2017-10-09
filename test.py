import json
import requests
from bs4 import BeautifulSoup
from twocaptcha.wrapper import TwoCaptcha
from selenium import webdriver

with open('tasks/taskNiroo.json') as tsk:
    t = json.load(tsk)

headers = {'Referer': 'https://www.nakedcph.com/auth/view',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko)'
                         'Chrome/61.0.3163.100Safari / 537.36'
           }

site_key = "6LeNqBUUAAAAAFbhC-CS22rwzkZjr_g4vMmqD_qo"

with requests.Session() as c:
    product_url = c.get(t['products']['url'])
    product_url2 = product_url.text
    soup = BeautifulSoup(product_url2, 'html.parser')

global csrftoken
global g_recaptcha_token
global sizeid
global checkout

def login():
    try:
        loginurl = "https://www.nakedcph.com/auth/view"
        c.get(loginurl)
        csrftoken = c.cookies['AntiCsrfToken']
        loginpayload = dict(_AntiCsrfToken=csrftoken, email=t['loginpayload']['email'],
                            password=t['loginpayload']['password'], next='login')
        c.post(loginurl, data=loginpayload, headers=headers)
        print("Login Successful!")
        print("Your csrftoken is " + csrftoken)
        return csrftoken
    except Exception:
        print("Unable to login")
csr = login()

# def captcha():
#         twoCaptcha = TwoCaptcha("bcbc99259be4a66e069b8648a5550bc3")
#         g_recaptcha_token = twoCaptcha.solve_captcha(site_key=site_key, page_url=product_url)
#         print(g_recaptcha_token)
# token = captcha()

def checkoutlink(csrftoken):
    # if 'div class="recaptcha' in product_url2:
    #     print("Captcha found!")
    #     captcha()
    # else:
        print("No Captcha found")
        try:
            size = soup.find_all("option")
            for i in range(len(size)):
                if t['products']['size'] == str(size[i].text.strip()):
                    sizeid = (size[i]['value'])
                    print("Your size id is " + sizeid)

        except Exception:
            print("Product isn't live yet, trying again")
            checkoutlink(csr)

        payload = {
            "action": "add",
            "_AntiCsrfToken": csrftoken,
            # "g - recaptcha": g_recaptcha_token,
            "id": sizeid
        }

        c.post('http://www.nakedcph.com/cart', data=payload)

        checkout = ("https://www.nakedcph.com/cart/add?_AntiCsrfToken=" + csrftoken + "&id=" + sizeid)
        print("Checkout link successfully created!")
        print("Your checkout link is " + checkout)
        return checkout
checkoutlink(csr)
