import json
import urllib
from json import load
import requests
import threading
from time import time, sleep
from classes.logger import Logger

logger = Logger()
log = logger.log

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Naked(threading.Thread):
                def __init__(self, thread_id, task_file, proxy_manager):
                threading.Thread.__init__(self)
                self.start_time = time()
                Logger.set_tid(thread_id)
                self.S = requests.Session()
                with open('config.json') as cfg:
                    self.c = load(cfg)
                with open(task_file) as tsk:
                    self.t = load(tsk)
                if self.t['exec_config']['use_proxies']:
                    proxy = proxy_manager.get_next_proxy()
                    log('[{}] adding proxy to task'.format(proxy), color='blue')
                    p = {
                        'http': 'http://{}'.format(proxy),
                        'https': 'https://{}'.format(proxy)
                    }

            self.S.proxies = p
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.81 Safari/537.36',
            'Content-Type': '',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': self.t['site_config']['base_url'].split('//')[1],
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1'
        }
        self.form_headers = self.headers
        self.form_headers['content-type'] = 'application/x-www-form-urlencoded'
        self.json_headers = self.headers
        self.json_headers['content-type'] = 'application/json'

    def login(username, password):
        if (username != '' and password != ''):
            driver.get('https://www.nakedcph.com/auth/view')
            formUl = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div/form/ul')
            usernameBox = formUl.find_element_by_xpath('./li/[@id="emailInput"]/input')
            passwordBox = formUl.find_element_by_xpath('./li/[@id="passwordInput"]/input')
            usernameBox.send_keys(username)
            passwordBox.send_keys(password)
            passwordBox.send_keys(Keys.ENTER)
            return True
        return False

    # def autoCompleteCaptcha():
    #     try:
    #         captchaBox = driver.find_element_by_xpath(
    #             '/html/body/div[@id="main"]/div[@id="main-content"]/div/div[@id="commodity-show-right"]/div/form/ul/li/input[@id="commodity-show-security-code"]')
    #         code = raw_input('A Captcha box has been detected! Please type in the Captcha code displayed: ')
    #         captchaBox.send_keys(code)
    #         captchaBox.send_keys(Keys.ENTER)
    #         print('Attempting to continue with entered Captcha code...')
    #     except Exception as e:
    #         print('No Captcha box detected! Proceeding with the item.')
    #         if (debug):
    #             print('Error Details: ' + str(e))
    #
    # def addToCart(product):
    #     driver.get(product['url'])
    #     autoCompleteCaptcha()
    #     commodityDiv = driver.find_element_by_xpath(
    #         '/html/body/div[@id="main"]/div[@id="main-content"]/div/div[@id="commodity-show-right"]/div')
    #     sizeSelection = commodityDiv.find_element_by_xpath(
    #         './form/select[@id="commodity-show-form-size"]/option[text()="' + product['size'] + '"]')
    #     sizeSelection.click()
    #     addButton = commodityDiv.find_element_by_xpath('./a')
    #     addButton.click()
    #
    # def checkout(card_number, card_expiration, card_crn):
    #     cartButton = driver.find_element_by_xpath('/html/body/div[@id="header-container"]/div/div[@id="main-cart"]/a')
    #     cartButton.click()
    #     mainContentDiv = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div')
    #     proceedButton = mainContentDiv.find_element_by_xpath('./a[2]')
    #     proceedButton.click()
    #     mainContentDiv = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div')
    #
    #     ##########Try this code if the code in the box below doesn't work##########################################
    #     emailBox = mainContentDiv.find_element_by_xpath(
    #         './div[@id="onestepcheckout-details"]/div/form/ul/li[@id="details-form-li-email"]/input')
    #     emailBox2 = mainContentDiv.find_element_by_xpath(
    #         './div[@id="onestepcheckout-details"]/div/form/ul/li[@id="details-form-li-email_repeat"]/input')
    #     checkoutBox = mainContentDiv.find_element_by_xpath(
    #         './div[@id="onestepcheckout-confirm"]/div/form/ul/li[1]/input')
    #     checkoutButton = mainContentDiv.find_element_by_xpath(
    #         './div[@id="onestepcheckout-confirm"]/div/form/ul/li[2]/input')
    #     totalTable = mainContentDiv.find_element_by_xpath('./div[@id="onestepcheckout-confirm"]/div/table')
    #     totalTableBody = totalTable.find_element_by_xpath('./tbody')
    #     tableItems = totalTableBody.find_elements_by_xpath('./tr')
    #     totalTableFooter = totalTable.find_element_by_xpath('./tfoot')
    #     tableTotalsItems = totalTableFooter.find_elements_by_xpath('./tr')
    #
    #     print('Checkout page details: ')
    #     print('')
    #     for item in tableItems:
    #         tableItemDetails = item.find_elements_by_xpath('./td')
    #         printableDetails = ""
    #         print('Item:')
    #         for detail in tableItemDetails:
    #             printableDetails += detail.text + ","
    #         print(printableDetails)
    #         print('')
    #     print('Totals: ')
    #     print('')
    #     for item in tableTotalsItems:
    #         tableTotalsItemName = item.find_element_by_xpath('./td[1]')
    #         tableTotalsItemValue = item.find_element_by_xpath('./td[2]')
    #         print(tableTotalsItemName.text + ':' + tableTotalsItemValue.text)
    #         print('')
    #     # We can take some shortcuts since we're logged in...
    #     emailBox2.send_keys(emailBox.get_attribute('value'))
    #     checkoutBox.click()
    #     checkoutButton.click()
    #     ###########################################################################################################
    #
    #     ##########Default Code#####################################################################################
    #     # emailBox = mainContentDiv.find_element_by_xpath('./form/ul/li[@id="details-form-li-email"]/input')
    #     # emailBox2 = mainContentDiv.find_element_by_xpath('./form/ul/li[@id="details-form-li-email_repeat"]/input')
    #     # checkoutButton = mainContentDiv.find_element_by_xpath('./form/ul/li[15]/input[@id="details-form-submit"]')
    #     # We can take some shortcuts since we're logged in...
    #     # emailBox2.send_keys(emailBox.get_attribute('value'))
    #     # checkoutButton.click()
    #     # mainContentDiv = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div')
    #     # checkoutButton2 = mainContentDiv.find_element_by_xpath('./form/ul/li[3]/input[@id="handling-form-submit"]')
    #     # checkoutButton2.click()
    #     # mainContentDiv = driver.find_element_by_xpath('/html/body/div[@id="main"]/div[@id="main-content"]/div')
    #     # totalTable = mainContentDiv.find_element_by_xpath('./table')
    #     # totalTableBody = totalTable.find_element_by_xpath('./tbody')
    #     # tableItems = totalTableBody.find_elements_by_xpath('./tr')
    #     # totalTableFooter = totalTable.find_element_by_xpath('./tfoot')
    #     # tableTotalsItems = totalTableFooter.find_elements_by_xpath('./tr')
    #     # print 'Checkout page details: '
    #     # print ''
    #     # for item in tableItems:
    #     #	tableItemDetails = item.find_elements_by_xpath('./td')
    #     #	printableDetails = ""
    #     #	print 'Item:'
    #     #	for detail in tableItemDetails:
    #     #		printableDetails += detail.text + ","
    #     #	print printableDetails
    #     #	print ''
    #     # print 'Totals: '
    #     # print ''
    #     # for item in tableTotalsItems:
    #     #	tableTotalsItemName = item.find_element_by_xpath('./td[@class="title"]')
    #     #	tableTotalsItemValue = item.find_element_by_xpath('./td[@class="total"]')
    #     #	print tableTotalsItemName.text + ':' + tableTotalsItemValue.text
    #     #	print ''
    #
    #     # agreeBox = mainContentDiv.find_element_by_xpath('./form/ul/li[@id="confirm-form-li-confirmed"]/input')
    #
    #     # agreeBox.click()
    #
    #     # checkoutButton3 = mainContentDiv.find_element_by_xpath('./form/ul/li[2]/input[2]')
    #
    #     # checkoutButton3.click()
    #
    #     ###########################################################################################################
    #
    #     paymentForm = driver.find_element_by_xpath('/html/body/div/div[@id="content"]/div[@id="payment_details"]/form')
    #     cardBox = paymentForm.find_element_by_xpath('./dl/dd[1]/input')
    #     monthBox = paymentForm.find_element_by_xpath('./dl/dd[2]/input[1]')
    #     yearBox = paymentForm.find_element_by_xpath('./dl/dd[2]/input[2]')
    #     crnBox = paymentForm.find_element_by_xpath('./dl/dd[3]/input')
    #     completeButton = paymentForm.find_element_by_xpath('./input[2]')
    #     cardBox.send_keys(card_number)
    #     monthBox.send_keys(card_expiration[0:2])
    #     yearBox.send_keys(card_expiration[3:])
    #     crnBox.send_keys(card_crn)
    #     wait = WebDriverWait(driver,
    #                          30)  # We keep trying to click the final button for 30 seconds before throwing an error
    #     completeButton = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, '/html/body/div/div[@id="content"]/div[@id="payment_details"]/form/input[2]')))
    #     completeButton.click()
    #     print(
    #         'Successfully clicked the order submit button. Please check the browser window to make sure that the order was checked out.')
    #     print('')
    #
    # orderIndex = 1
    # startTime = time.time()
    # for order in orders:
    #     print('Processing order number ' + str(orderIndex) + '...')
    #     print('')
    #     # driver = webdriver.Chrome() #Non-headless webdriver
    #     driver = webdriver.PhantomJS()  # Headless webdriver
    #
    #     logged_in = login(order['username'], order['password'])
    #     if (logged_in):
    #         for product in order['products']:
    #             try:
    #                 for i in range(product['quantity']):
    #                     addToCart(product)
    #             except Exception as e:
    #                 print("Error adding product to cart! Attempting to proceed anyway. Product URL: " + product["url"])
    #                 if (debug):
    #                     print('Error Details: ' + str(e))
    #         try:
    #             checkout(order['credit_card_number'], order['credit_card_expiration'], order['credit_card_crn'])
    #         except Exception as e:
    #             print(
    #                 "Error occured while checking out the order! Check the browser to see what went wrong. If the checkout page is missing certain credentials, you may have input an incorrect username/password combination. It is also possible that you tried to purchase too many of a particular item.")
    #             if (debug):
    #                 print('Error Details: ' + str(e))
    #     else:
    #         print('No username and/or password provided. The order cannot be processed.')
    #     orderIndex += 1
    # print('Total elapsed script time: ' + str(time.time() - startTime) + ' second(s).')
