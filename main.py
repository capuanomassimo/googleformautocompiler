# Purpose-built Selenium script to automatically fill YOUR own Google Form for functional testing.
# Not intended for third-party forms, production environments, or unsolicited submissions.
# Use only on forms you own or are explicitly authorized to test.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

url = "https://docs.google.com/forms/d/e/1FAIpQLSenbjP5Pm8HMH5KsvkfGhEG8NqfwV6N9b8JaXyk3BL5XcjFDA/viewform?usp=header"

def answer_questions(driver):
    blocks = driver.find_elements(By.CLASS_NAME, "Qr7Oae")
    for block in blocks:
        radio_options = block.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
        if radio_options:
            found = False
            for option in radio_options:
                try:
                    label = option.get_attribute("aria-label").lower()
                except:
                    label = ""
                if "services" in label:
                    option.click()
                    found = True
                    break
            if not found:
                choice = random.choice(radio_options)
                choice.click()
            time.sleep(0.2)
            continue

        checkbox_options = block.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
        if checkbox_options:
            num = random.randint(1, min(3, len(checkbox_options)))
            to_select = random.sample(checkbox_options, num)
            for box in to_select:
                box.click()
                time.sleep(0.2)
            continue

        try:
            menu = block.find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
            menu.click()
            time.sleep(0.5)
            options = block.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
            found = False
            for option in options:
                if "craftsmanship" in option.text.lower():
                    option.click()
                    found = True
                    break
            if not found and options:
                random.choice(options).click()
            time.sleep(0.2)
        except:
            pass

def click_button(driver, text):
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for button in buttons:
        if text.lower() in button.text.lower():
            button.click()
            return True
    return False

def fill_and_submit():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    for _ in range(10):
        answer_questions(driver)
        time.sleep(1)
        if not click_button(driver, "Next"):
            click_button(driver, "Submit")
            break
        time.sleep(1.5)

    driver.quit()

# time sleep for avoid being flagged as a bot 
# execution loop 400 times

for i in range(400):
    print(f"\n--- Submission number {i+1} ---")
    fill_and_submit()
    time.sleep(random.uniform(1.0, 3.0))
