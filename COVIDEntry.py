from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# for pausing between navigation
import time


def save_screening():
    # Using Chrome to access web
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # time.sleep(1)

    # Open the website
    driver.get('https://covid-19.ontario.ca/screening/worker/')

    time.sleep(1)
    try:
        # Start Screening
        screening = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/main/div/div[1]/div/div/button').click()

        # How old are you?
        time.sleep(1)
        age_radio = driver.find_element_by_xpath('//*[@id="18+"]').click()                      # 18+

        time.sleep(1)
        continue_btn = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/main/div/div/div/div[2]/button').click()              # Continue

        # Are you currently experiencing any of these symptoms?
        time.sleep(1)
        none_input_btn = driver.find_element_by_xpath('//*[@id="none_of_the_above"]').click()   # None of the above

        time.sleep(1)
        continue_btn = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button').click()          # Continue

        # Is anyone you live with currently experiencing any new COVID-19 symptoms
        # and/or waiting for test results after experiencing symptoms?
        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        # In the last 14 days, have you or anyone you live with travelled outside of Canada?
        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        # In the last 14 days, have you been identified as a “close contact” of someone who currently has COVID-19?
        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        # Has a doctor, health care provider, or public health unit told you
        # that you should currently be isolating (staying at home)?
        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        # In the last 14 days, have you received a COVID Alert exposure notification on your cell phone?
        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        # You can go, click on save screening result (PDF)
        time.sleep(1)
        save_hyper_link = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div[2]/div[2]/div[1]').click()

        time.sleep(1)
        driver.close()

    except NoSuchElementException:
        time.sleep(2)


if __name__ == "__main__":
    save_screening()
