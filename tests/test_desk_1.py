from page.desk1_page import Desk1Page
from playwright.sync_api import Page
import time


"""Тест подсчет количества торов на стр"""
def test_count_all_product_in_page(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.count_all_product_in_page()
    time.sleep(3)


"""Тест перехода на другую стр с установкой чекбокса на steel"""
def test_checkbox_steel(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.checkbox_steel()
    time.sleep(3)


"""Тест перехода на страницу по клику на Products"""
def test_filter_products_chainge_page(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.filter_products_chainge_page()
    time.sleep(3)


"""Тест перехода на другую стр с выбором фильтра Newest Arrivals"""
def test_filter_newest(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.filter_newest()
    time.sleep(3)


"""Test перехода по фильтру Name (A-Z)"""
def test_filter_name_az(page: Page):
    page_pages = Desk1Page(page)
    page_pages.open()
    time.sleep(3)
    page_pages.page_name_az()
    time.sleep(3)


"""Test перехода по фильтру price_low"""
def test_filter_price_low_to_high(page: Page):
    page_pages = Desk1Page(page)
    page_pages.open()
    time.sleep(3)
    page_pages.page_price_low()
    time.sleep(3)


"""Test перехода по фильтру price_high"""
def test_filter_price_high_to_low(page: Page):
    page_pages = Desk1Page(page)
    page_pages.open()
    time.sleep(3)
    page_pages.page_price_high()
    time.sleep(3)


"""тест видимости кнопки shopping cart при наведении на карточку товара"""
def test_view_shopping_cart_on_product_cart(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.view_shopping_cart_on_product_cart()
    time.sleep(3)


"""тест функциональности кнопки shopping cart на карточке товара"""
def test_click_shopping_cart_on_product_car(page: Page):
  # Цепочка: найти элемент → кликнуть
  shop_click = Desk1Page(page)
  shop_click.open()
  time.sleep(3)
  shop_click.click_shopping_cart_on_product_car()
  time.sleep(3)


"""Тест перехода на страницу заказа первого продукта"""
def test_page_first_product(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.page_first_product()
    time.sleep(3)


"""Тест перехода на страницу заказа последнего продукта"""
def test_page_last_product(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.page_last_product()
    time.sleep(3)


"""тест поиск элементов внутри других элементов"""
def test_last_product(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.nested_locators()
    time.sleep(3)


"""тест2 поиск элементов внутри других элементов"""
def test_nested_locators_string(page: Page):
    shop_click = Desk1Page(page)
    shop_click.open()
    time.sleep(3)
    shop_click.nested_locators_string()
    time.sleep(3)
