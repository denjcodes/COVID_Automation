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
        screening = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/main/div/div[1]/div/div/button').click()

        time.sleep(1)
        age_radio = driver.find_element_by_xpath('//*[@id="18+"]').click()

        time.sleep(1)
        continue_btn = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div/div/div/div[2]/button').click()

        time.sleep(1)
        none_input_btn = driver.find_element_by_xpath('//*[@id="none_of_the_above"]').click()

        time.sleep(1)
        continue_btn = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/main/div/div/div/div/div[2]/button').click()

        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        time.sleep(1)
        no_btn = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div/div/div/div[2]/button[1]').click()

        time.sleep(1)
        save_hyper_link = driver.find_element_by_xpath('//*[@id="reach-skip-nav"]/div[2]/div[2]/div[1]').click()

        time.sleep(2)
        driver.close()

    except NoSuchElementException:
        time.sleep(2)


if __name__ == "__main__":
    save_screening()
