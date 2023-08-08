import os
from time import sleep

import pyotp
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()
email = os.getenv('email')
password = os.getenv('password')
otp_secret = os.getenv('otp_secret')


def get_otp() -> str:
    return pyotp.TOTP(otp_secret).now()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://accounts.google.com/ServiceLogin')  # URL.

    # Enter email and password.
    driver.implicitly_wait(20)
    driver.find_element(
        'xpath',
        '//*[@id="identifierId"]',
    ).send_keys(email)
    driver.find_element(
        'xpath',
        '//*[@id="identifierNext"]/div/button/span',
    ).click()
    sleep(1)
    driver.implicitly_wait(20)
    driver.find_element(
        'xpath',
        '//*[@id="password"]/div[1]/div/div[1]/input',
    ).send_keys(password)
    driver.find_element(
        'xpath',
        '//*[@id="passwordNext"]/div/button/span',
    ).click()

    # Choose Google Authenticator.
    sleep(3)
    driver.implicitly_wait(20)
    driver.find_element(
        'xpath',
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/button/span',
    ).click()
    sleep(1)
    driver.implicitly_wait(20)
    driver.find_element(
        'xpath',
        '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/div/ul/li[1]/div/div[2]',
    ).click()

    # Enter OTP.
    sleep(1)
    driver.implicitly_wait(20)
    driver.find_element(
        'xpath',
        '//*[@id="totpPin"]',
    ).send_keys(get_otp())
    sleep(1)
    driver.find_element(
        'xpath',
        '//*[@id="totpNext"]/div/button/span',
    ).click()

    sleep(10)  # For showing the result.
