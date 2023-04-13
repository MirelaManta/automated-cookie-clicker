from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
# get cookie to click on
cookie = driver.find_element(By.ID, "cookie")
# get upgrade item ids
upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrade_ids = [upgrade.get_attribute("id") for upgrade in upgrades[:-1]]

timeout = time.time() + 5
five_min = time.time() + 300


while True:
    cookie.click()
    # Every 5 seconds
    if time.time() > timeout:

        # convert b text into integer and create a list with all prices
        store_prices_tags = driver.find_elements(By.CSS_SELECTOR, "#store b")
        store_prices = [int((price.text.split("-")[1].strip().replace(",", ""))) for price in store_prices_tags[:-1]]

        # get current cookie amount aka money and turn into int
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        money = int(money_element)

        # create dictionary with upgrades and prices
        cookie_upgrades = {}
        for n in range(len(store_prices)):
            cookie_upgrades[store_prices[n]] = upgrade_ids[n]

        # find upgrades that we can currently afford
        affordable_upgrades = {}
        for price, id in cookie_upgrades.items():
            if money > price:
                affordable_upgrades[price] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upg = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upg]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookies_per_s = driver.find_element(By.ID, "cps").text
        print(cookies_per_s)
        break


