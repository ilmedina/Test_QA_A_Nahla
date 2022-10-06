from multiprocessing.connection import wait
import pytest
import time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
def test_login(driver):
    home_page = HomePage (driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_title_of_page() == "PRODUCTS"
    home_page.add_items_to_cart()
    home_page.open_cart()
    assert home_page.get_title_of_page() == "YOUR CART"
    assert home_page.get_item_name_from_cart('//div[text()="Sauce Labs Backpack"]') =="Sauce Labs Backpack"
    assert home_page.get_item_name_from_cart('//div[text()="Sauce Labs Bike Light"]') =="Sauce Labs Bike Light"
    home_page.get_checkout()
    assert home_page.get_title_of_page() == "CHECKOUT: YOUR INFORMATION"
    home_page.fill_your_information_page("Ilmedina", "Salcin", "387")
    assert home_page.get_title_of_page() == "CHECKOUT: OVERVIEW"
    assert home_page.get_item_name_from_cart('//div[text()="Sauce Labs Backpack"]') =="Sauce Labs Backpack"
    assert home_page.get_item_name_from_cart('//div[text()="Sauce Labs Bike Light"]') =="Sauce Labs Bike Light"
    home_page.get_finish()
    assert home_page.get_title_of_page() == "CHECKOUT: COMPLETE!"
    home_page.get_menu_logout()
    home_page.get_verify_logout()
    time.sleep(10)

   


