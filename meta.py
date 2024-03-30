from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = webdriver.ChromeService(executable_path="chromedriver-win64\\chromedriver.exe")#Your path
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--start-maximized")

chrome_options.add_extension('MetaMask_Chrome.crx')

meta_value = ['YOUR MNEMONIK ON 24 WORDS !!'.split()]

driver = webdriver.Chrome(chrome_options, service)

def metamask(meta_value, driver):
        try:
            #your site
            driver.get("https://www.google.com/")
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
            i_accept = driver.find_element(by=By.TAG_NAME, value='input').click()

            import_wallet = driver.find_elements(by=By.TAG_NAME, value='button')
            import_wallet[4].click()
            
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
            dont_need = driver.find_elements(by=By.TAG_NAME, value='button')[1].click()

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dropdown__select')))
            select = driver.find_elements(by=By.CLASS_NAME, value='dropdown__select')[1]
            phrase_24 = select.find_elements(by=By.TAG_NAME, value='option')[4].click()

            for j in range(24):
                for word in meta_value:
                    input_case = driver.find_element(by=By.XPATH, value=f'//*[@id="import-srp__srp-word-{j}"]')
                    input_case.send_keys(word[j])
            time.sleep(2)

            confirm = driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
            
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-field__input')))
            password = driver.find_elements(by=By.CLASS_NAME, value='form-field__input')
            password[0].send_keys('password')
            password[1].send_keys('password')
            
            check_mark = driver.find_elements(by=By.TAG_NAME, value='input')[2].click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
            import_my_wallet_button = driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
            time.sleep(0.5)

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
            got_it = driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'li')))
            nxt = driver.find_elements(by=By.TAG_NAME, value='li')[1].click()
            
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
            compleate = driver.find_elements(by=By.TAG_NAME, value='button')[3].click()
            time.sleep(1)

            driver.switch_to.window(driver.window_handles[0])
            time.sleep(999)

        except Exception as ex:
            print("ploblem in metamask", ex)

metamask(meta_value, driver)