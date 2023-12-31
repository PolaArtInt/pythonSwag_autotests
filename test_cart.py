from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


# PASSED
def test_add_item_from_catalog():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    add_to_cart_btn = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_btn.click()

    time.sleep(3)

    shopping_cart_link = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_link.click()

    time.sleep(3)

    remove_item_btn = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')

    time.sleep(3)

    assert remove_item_btn.text == "Remove"

    driver.quit()


# PASSED
def test_remove_item_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    add_to_cart_btn1 = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_btn1.click()
    add_to_cart_btn2 = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]')
    add_to_cart_btn2.click()

    time.sleep(3)

    cart_tag_before = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    time.sleep(3)

    shopping_cart_link = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    shopping_cart_link.click()

    time.sleep(3)

    remove_item_btn = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
    remove_item_btn.click()

    time.sleep(3)

    cart_tag_after = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text

    assert int(cart_tag_before) != int(cart_tag_after)

    driver.quit()
