from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


# PASSED
def test_logout():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    time.sleep(3)

    logout_button = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout_button.click()

    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()


# PASSED
def test_about_button():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    time.sleep(3)

    about_button = driver.find_element(By.CSS_SELECTOR, '#about_sidebar_link')
    about_button.click()

    assert driver.current_url == "https://saucelabs.com/"

    driver.quit()


# INCOMPLETE
# кнопка работает, бейдж корзины очищается, корзина очищается, кнопки добавления товара не отжаты
def test_reset_app():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(3)

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()

    time.sleep(3)

    about_button = driver.find_element(By.CSS_SELECTOR, '#reset_sidebar_link')
    about_button.click()

    # assert driver.current_url == "https://saucelabs.com/"

    driver.quit()
