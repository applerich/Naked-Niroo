import json
import requests
from bs4 import BeautifulSoup

with open('tasks/taskNiroo.json') as tsk:
    t = json.load(tsk)

tasks = open("tasks/taskNiroo.json")
orders = t["payload"]
headers = {'Referer': 'https://www.nakedcph.com/auth/view',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko)' 
                         'Chrome/61.0.3163.100Safari / 537.36'
           }

def login():
    with requests.Session() as c:
        try:
            loginurl = "https://www.nakedcph.com/auth/view"
            c.get(loginurl)
            csrftoken = c.cookies['AntiCsrfToken']
            payload = dict(_AntiCsrfToken=csrftoken, email=t['payload']['email'], password=t['payload']['password'], next='login')
            c.post(loginurl, data=payload, headers=headers)
            print("Login Successful!")
            print("Your csrftoken is " + csrftoken)
            return csrftoken
        except Exception:
            print("Unable to login")

csr = login()

def checkoutlink(csrftoken):
    with requests.Session() as c:
        try:
            producturl = t['products']['url']
            product = c.get(producturl)
            product2 = product.text
            soup = BeautifulSoup(product2, 'html.parser')
            size = soup.find_all("option")
            for i in range(len(size)):
                if t['products']['size'] == str(size[i].text.strip()):
                    sizeid = (size[i]['value'])
            print("Your size id is " + sizeid)
            checkout = "https://www.nakedcph.com/cart/add?_AntiCsrfToken=" + csrftoken + "&id=" + sizeid
            print("Your checkout link is " + checkout)
            return checkout
        except Exception:
            print("Unable to create checkout link")
check = checkoutlink(csr)

def checkout(checkout):
    with requests.Session() as c:
        try:
            c.get(checkout)
            payload2 = dict(email=t['payload']['email'])
        except Exception:
            print("Unable to checkout")
checkout(check)