from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import time
import config
import datetime

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(30)

def get_page():
    while True:
        try:
            print('getting login page...')
            driver.get('http://cp.cs.cityu.edu.hk:16978/loginform.html')
        except WebDriverException:
            print('failed. retrying...')
            time.sleep(1)
            pass
        else:
            print('got it!')
            break

def login(max_trials):
    trial = 0
    while True:
        get_page()

        try:
            driver.find_element_by_name('username').send_keys(config.username)
            driver.find_element_by_name('ctx_pass').send_keys(config.password)
            print('submitng form...')
            driver.find_element_by_name('modify').click()
        except WebDriverException:
            print('form submission failed. retrying...')
            continue

        print('waiting 5s...')
        time.sleep(5)

        curl = driver.current_url

        if curl != 'https://cp.cs.cityu.edu.hk:16979/loginform.html?':
            print('success!')
            break
        else:
            trial += 1
            if trial < max_trials:
                print('retrying...')
            else:
                print('failed')
                break

print(datetime.datetime.now())
print('=' * 20)
login(5)
driver.quit()
print()
