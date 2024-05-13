from time import sleep,strftime
import pandas as pd
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.multipart import MIMEMultipart

YOU_CHROME_DRIVER_PATH = 'C://Program Files (x86)/Google/Chrome/Application'

CHROME_PATH = YOU_CHROME_DRIVER_PATH + '/chrome.exe'

#driver = webdriver.Chrome(executable_path=CHROME_PATH)

driver=webdriver.Chrome()

driver.get(CHROME_PATH)

chrome_options = Options()

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options.add_experimental_option("detach", True)

kayak = 'https://www.kayak.pt/flights/LIS-SIN/2024-04-24/2024-05-01?sort=bestflight_a'
driver.get(kayak)


driver.find_element("xpath", '//button[contains(@id,"Qxqs-priceAlertToggle") and contains(@class,"AAhf-toggle-input")]')
