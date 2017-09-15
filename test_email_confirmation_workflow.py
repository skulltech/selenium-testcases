import time
import random

import requests
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from lxml import html


class TestSelenium(unittest.TestCase):
    #test case!!!!
    def skip_test_browse_google(self):
        driver = webdriver.Chrome()
        driver.get('https://dev.worldunited.com/signup/register')
        assert driver.title == 'World United'

    def test_email_confirmation_flow(self):
        #first_email_xpath = '//*[@id="mr_132702533"]/td[2]'

        DISPOSABLE_WEBMAIL_ADURL = 'https://grr.la'
        password = 'Password123'
        
        '''
        We will be using 2 webdrivers (i.e., equivalent to 2 tabs in a user's browser)
        -- SIGNUP
        '''
        
        disposable_email_driver = webdriver.Chrome()
        # Go to disposable email provider
        disposable_email_driver.get(DISPOSABLE_WEBMAIL_ADURL)
        # Get new disposable_email_address
        new_disposable_email_id = disposable_email_driver.find_element_by_id('inbox-id').text
        new_disposable_email = new_disposable_email_id + '@grr.la'
        print('Email Address: ' + new_disposable_email)

        signup_form_driver = webdriver.Chrome()
        signup_form_driver.get('https://dev.worldunited.com/signup/register')
        # Use new disposable_email_address for Signup
        signup_form_driver.find_element_by_xpath('//input[@name="emailAddress"]').send_keys(new_disposable_email)
        signup_form_driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        signup_form_driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(password)

        confirm_conditions_checkbox_xpath = '//div[@class="CheckboxWithValidation"]/div/label/span'
        signup_form_driver.find_element_by_xpath(confirm_conditions_checkbox_xpath).click()
        
        SUBMIT_FORM_SELECTOR = 'button.primary'
        signup_form_driver.find_element_by_css_selector(SUBMIT_FORM_SELECTOR).click()
        
        '''
        --- EMAIL VERIFICATION
        '''

        # Go back to disposable email provider
        # Wait for ~10 seconds
        time.sleep(40)
        FIRST_EMAIL_SELECTOR = 'tr.mail_row:nth-child(1)'
        # Click on the first email in list
        disposable_email_driver.find_element_by_css_selector(FIRST_EMAIL_SELECTOR).click()
        time.sleep(10)
        CONTINUE_SIGNUP_LINK_SELECTOR = '//a[@title="VERIFY EMAIL ADDRESS"]'
        # continue_signup_url = disposable_email_driver.find_element_by_xpath(CONTINUE_SIGNUP_LINK_SELECTOR).href

        html_source = disposable_email_driver.page_source
        tree = html.fromstring(str(html_source))
        try:
            continue_signup_url = tree.xpath(CONTINUE_SIGNUP_LINK_SELECTOR)[0].get('href')
        except:
            print('Email not recieved!')
            raise
        print('Continue Signup URL: ' + continue_signup_url)

        disposable_email_driver.get(continue_signup_url)
        time.sleep(10)

''''
    def skip_test_browse_firefox(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
        

        driver = webdriver.Firefox()
        driver.get('https://dev.worldunited.com/signup/register')
        assert driver.title == 'World United'

    def skip_test_signup_failure(self):
        email = 'TESTING_' + unique_identifier + '@test.com'
        password = 'L2a4qnbL2'

        display = Display(visible=0, size=(1920, 1080))
        display.start()

        driver = webdriver.Chrome()
        driver.get('https://dev.worldunited.com/signup/register')
        driver.find_element_by_xpath('//input[@name="emailAddress"]').send_keys(email)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(password)
        driver.find_element_by_xpath('//input[@type="checkbox"]').click()
        driver.find_element_by_css_selector('button.ui.fluid.primary.button').click()
        
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'div.ui.error.message')))
        finally:
            assert element.text == 'Signup failed, please try again later'
'''

if __name__=='__main__':
    unittest.main()
