from page.base_page import BasePage
from playwright.sync_api import expect
from page.locators.design_locators import DesignLocators as loc


class DesignPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'


    def btn_add_to_cart(self):
        # Товар добавить в корзину → проверить что внутри корзины +1 товар
        self.page.locator(loc.ADD).click()
        expect(self.page.locator(loc.QUANTITY).first).to_have_text('1')


    def btn_plus_click(self):
        # Найти + добавить в корзину → проверить что внутри корзины +2 товар
        self.page.locator(loc.PLUS).click()
        self.page.locator(loc.ADD).click()
        expect(self.page.locator(loc.QUANTITY).first).to_have_text('2')


    def btn_plus_and_minus_click(self):
        self.page.locator(loc.PLUS).click()
        self.page.locator(loc.MINUS).click()
        self.page.locator(loc.ADD).click()
        expect(self.page.locator(loc.QUANTITY).first).to_have_text('1')
