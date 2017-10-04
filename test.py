import urllib.request
import json
import requests
from selenium import webdriver
import logging

tasks = open("tasks/taskNiroo.json")
orders = json.loads(tasks.read())["login"]

def login():
    with requests.Session() as c:
        loginUrl = ("https://www.nakedcph.com/auth/view")
        email = "nirooz@rocketmail.com"
        password = "Nirooshan96"
        c.get(loginUrl)
        csrftoken = c.cookies['_AntiCsrfToken']
        login_data = dict(_AntiCsrfToken=csrftoken, email=email, password=password, next='/')
        c.post(loginUrl, data=login_data, headers={
            'Referer': 'https://www.nakedcph.com/auth/view','User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/61.0.3163.100Safari / 537.36'})
        page = c.get('https://www.nakedcph.com/')
        print(page.content)


# def addToCart():
#     driver = webdriver.Chrome()
#     productUrl = "https://www.nakedcph.com/adidas-originals-overkill-x-fruition-x-adidas-consortium-tubular-elastic-cm8003/p/5552"
#     driver.get(productUrl)
#     commodityDiv = driver.find_element_by_xpath('//*[@id="product-form"]')
#     sizeSelection = commodityDiv.find_element_by_xpath('//*[@id="product-form"]/div[2]/div/select/option[8]')
#     sizeSelection.click()
#     addButton = commodityDiv.find_element_by_xpath('//*[@id="product-form"]/div[2]/span/button')
#     addButton.click()
#     checkoutButton = commodityDiv.find_element_by_xpath('//*[@id="product-form"]/div[2]/a')
#     checkoutButton.click()
# addToCart()