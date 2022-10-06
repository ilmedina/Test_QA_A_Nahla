from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from time import time
from turtle import clear
from xml.dom.minidom import Element
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    def login (self, username, password):
        self.wait
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.click()
        username_polje.clear()
        username_polje.send_keys(username)

        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.click()
        password_polje.clear()
        password_polje.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
    def get_title_of_page (self):
        welcome_element= self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return welcome_element.text
    def add_items_to_cart (self):
        self.wait
        add_to_cart=self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_to_cart.click()
        add_to_cart=self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_to_cart.click()
    def open_cart(self):
        open_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        open_cart.click()
    def get_item_name_from_cart(self,xpath):
        cart_page_title= self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return cart_page_title.text
    def get_checkout(self):
        checkout_button=self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

    def fill_your_information_page(self, name, surname, zip):
        self.wait
        name_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        name_polje.click()
        name_polje.clear()
        name_polje.send_keys(name)

        surname_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        surname_polje.click()
        surname_polje.clear()
        surname_polje.send_keys(surname)

        zip_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        zip_polje.click()
        zip_polje.clear()
        zip_polje.send_keys(zip)

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
    def get_finish(self):
        finish_button = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finish_button.click()
    def get_menu_logout (self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_button.click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_button.click()
    def get_verify_logout (self):
        welcome_element= self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        #nisam znala kako da izvucem value iz buttona, a nisam imala vremena da trazim, pa sam isla logikom da ako nadje to dugme da sam na log in page :)

