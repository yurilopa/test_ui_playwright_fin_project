from page.design_page import DesignPage
from playwright.sync_api import Page
import time


# Товар добавить в корзину → проверить что внутри корзины +1 товар
def test_btn_add_to_cart(page: Page):
    contactus_form = DesignPage(page)
    contactus_form.open()
    time.sleep(3)
    contactus_form.btn_add_to_cart()
    time.sleep(3)


# Найти и кликнуть на кнопку + -> добавить в корзину → проверить что внутри корзины 2 товар
def test_btn_plus_click(page: Page):
    contactus_form = DesignPage(page)
    contactus_form.open()
    time.sleep(3)
    contactus_form.btn_plus_click()
    time.sleep(3)


# Найти и кликнуть на кнопку (+) -> найти и кликнуть на кнопку (-) -> добавить в корзину → проверить что в корзине 1
def test_btn_plus_and_minus_click(page: Page):
    contactus_form = DesignPage(page)
    contactus_form.open()
    time.sleep(3)
    contactus_form.btn_plus_and_minus_click()
    time.sleep(3)
