import urllib.request
import json
import requests
from selenium import webdriver
import logging

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.81 Safari/537.36'
}

tasks = open("tasks/taskNiroo.json")
orders = json.loads(tasks.read())["login"]

driver = webdriver.Chrome()

# def login(email, password):
#     url = "https://www.nakedcph.com/auth/view"
#     driver.get(url)
#     emailBox = driver.find_element_by_xpath('//*[@id="emailInput"]')
#     passwordBox = driver.find_element_by_xpath('//*[@id="passwordInput"]')
#     signIn = driver.find_element_by_xpath('//*[@id="auth"]/form/span/button')
#
#     emailBox.send_keys(email)
#     passwordBox.send_keys(password)
#     signIn.click()
#
# login("nirooz@rocketmail.com", "Niroo100996")

def addToCart():
    productUrl = "https://www.nakedcph.com/adidas-originals-overkill-x-fruition-x-adidas-consortium-tubular-elastic-cm8003/p/5552"
    driver.get(productUrl)
    commodityDiv = driver.find_element_by_xpath('//*[@id="product-form"]')
    sizeSelection = commodityDiv.find_element_by_xpath('//*[@id="product-form"]/div[2]/div/select/option[8]')
    sizeSelection.click()
    addButton = commodityDiv.find_element_by_xpath('//*[@id="product-form"]/div[2]/span/button')
    addButton.click()
    checkoutButton = commodityDiv.find_element_by_xpath('//*[@id="product-form"]/div[2]/a')
    checkoutButton.click()
addToCart()
