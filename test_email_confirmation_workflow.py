import time
import random

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display


class TestSelenium(unittest.TestCase):
    #test case!!!!
    def skip_test_browse_google(self):
        driver = webdriver.Chrome()
        driver.get('https://dev.worldunited.com/signup/register')
        assert driver.title == 'World United'

    def test_email_confirmation_flow(self):
        #first_email_xpath = '//*[@id="mr_132702533"]/td[2]'

        DISPOSABLE_WEBMAIL_ADURL = 'https://grr.la'
        password = 'Password1'

        # TODO: We may need 2 webdrivers (i.e., equivalent to 2 tabs in a user's browser) (if we can't then we need to save the email address and come back to it after the login flow)
        # -- SIGNUP
        
        disposable_email_driver = webdriver.Chrome()
        # go to disposable email provider
        disposable_email_driver.get(DISPOSABLE_WEBMAIL_ADURL)
        # get new disposable_email_address
        new_disposable_email_id = disposable_email_driver.find_element_by_css_selector('#inbox-id').text
        new_disposable_email = new_disposable_email_id + '@grr.la'
        

        
        #new_disposable_email = "test" + str(random.randint(1, 100000)) + "@test.com"
        print('email_address: ' + new_disposable_email)

        signup_form_driver = webdriver.Chrome()
        signup_form_driver.get('https://dev.worldunited.com/signup/register')
        # use new disposable_email_address for signup
        signup_form_driver.find_element_by_xpath('//input[@name="emailAddress"]').send_keys(new_disposable_email)
        signup_form_driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        signup_form_driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(password)
        #time.sleep(10)
        # TODO: Debug this later
        #signup_form_driver.find_element_by_xpath('//input[@type="checkbox"]').click()

        confirm_conditions_checkbox_xpath = '//*[@id="root"]/div/div/div/div/form/div/div/div[5]/div/label/span'
        confirm_conditions_checkbox_selector = "#root > div > div > div > div > form > div > div > div.CheckboxWithValidation > div > label > span"
        #signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[4]/button[1]').click()
        signup_form_driver.find_element_by_xpath(confirm_conditions_checkbox_xpath).click()
        
        SUBMIT_FORM_SELECTOR = 'button.primary'
        # TODO: This is an error currently
        time.sleep(60)
        time.sleep(2)
        signup_form_driver.find_element_by_css_selector(SUBMIT_FORM_SELECTOR).click()

        # api.wait_for_next_email
        # api.get_html_of_next_email
        # get_link_from_text
        # go to link

        # submit signup form

        # --- EMAIL VERIFICATION
        # go back to disposable email provider
        # wait for ~10 seconds
        time.sleep(20)
        FIRST_EMAIL_SELECTOR = 'tr.mail_row:nth-child(1)'
        # Click on the first email in list
        disposable_email_driver.find_element_by_css_selector(FIRST_EMAIL_SELECTOR).click()
        time.sleep(5)
        CONTINUE_SIGNUP_LINK_SELECTOR = '#display_email > div > div.email > div > center > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > table:nth-child(6) > tbody > tr > td > table > tbody > tr > td > a'
        # Note: The selector/xpath for the link in the html email is brittle and liable to break on any change to the content/structure of the confirmation email
        continue_signup_url = disposable_email_driver.find_element_by_css_selector(CONTINUE_SIGNUP_LINK_SELECTOR).href
        print('continue_signup_url: ' + continue_signup_url)

        disposable_email_driver.get(continue_signup_url)

        time.sleep(10)

        driver.find_element_by_css_selector('button.ui.fluid.primary.button').click()
        # wait for it to load
        # pick out the confirm link
        # go to the confirm link
        '''
        email = 'TESTING_' + random.randint(1, 100000) + '@test.com'
        password = 'Password1'

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

    # def skip_test_browse_firefox(self):
    #     display = Display(visible=0, size=(800, 600))
    #     display.start()
        

    #     driver = webdriver.Firefox()
    #     driver.get('https://dev.worldunited.com/signup/register')
    #     assert driver.title == 'World United'

    # def skip_test_signup_failure(self):
    #     email = 'TESTING_' + unique_identifier + '@test.com'
    #     password = 'L2a4qnbL2'

    #     display = Display(visible=0, size=(1920, 1080))
    #     display.start()

    #     driver = webdriver.Chrome()
    #     driver.get('https://dev.worldunited.com/signup/register')
    #     driver.find_element_by_xpath('//input[@name="emailAddress"]').send_keys(email)
    #     driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    #     driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys(password)
    #     driver.find_element_by_xpath('//input[@type="checkbox"]').click()
    #     driver.find_element_by_css_selector('button.ui.fluid.primary.button').click()
        
    #     try:
    #         element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , 'div.ui.error.message')))
    #     finally:
    #         assert element.text == 'Signup failed, please try again later'


if __name__=='__main__':
    unittest.main()
