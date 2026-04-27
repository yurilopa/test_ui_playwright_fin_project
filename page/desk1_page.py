from playwright.sync_api import expect
from page.locators.desk_locators import DeskLocators as loc
from page.base_page import BasePage


# Константы URL-путей
DESKS_1 = "/shop/category/desks-1"
SHOP = "/shop"
FILTER_STEEL = "/shop/category/desks-1?category=1&search=&order=&attrib=1-1"
FILTER_NEWEST = "/shop?order=create_date+desc&category=1"
FILTER_NAME_AZ = "/shop?order=name+asc&category=1"
FILTER_PRICE_LOW = "/shop?order=list_price+asc&category=1"
FILTER_PRICE_HIGH = "/shop?order=list_price+desc&category=1"
FIRST_PRODUCT = "/shop/customizable-desk-9?category=1#attr=1,3"
LAST_PRODUCT = "/shop/furn-7888-desk-stand-with-screen-21?category=1"


class Desk1Page(BasePage):
    page_url = '/shop/category/desks-1'


    def count_all_product_in_page(self):
        products = self.page.locator(loc.CART)  # Сохраняем локатор и используем
        print("=" * 70 + "\n")
        print(f"Всего товаров: {products.count()}")


    def checkbox_steel(self):
        # Цепочка 1: кликнуть на чекбокс
        self.page.locator(loc.CHECKBOXSTEEL).first.click()

        # Проверяем видимость - ЦЕПОЧКА ПРОВЕРОК
        expect(self.page.locator(loc.CHECKBOXSTEEL).first).to_be_visible()
        expect(self.page.locator(loc.CHECKBOXSTEEL).first).not_to_be_empty()
        print("   → Проверки пройдены")

        # 5. Проверяем что открылась страница товара Customizable Desk
        expect(self.page).to_have_url(f"{self.base_url}{FILTER_STEEL}")
        print(" Кликнули на чекбокс steel - открыли страницу товара Customizable Desk")
        print("=" * 70 + "\n")


    def filter_products_chainge_page(self):
        button = self.page.locator(loc.CARTBTN).first.click()
        # Проверяем что открылась страница товара
        expect(self.page).to_have_url(f"{self.base_url}{SHOP}")
        print("По клику на products выполнен переход на стр")


    """Тест перехода на другую стр с выбором фильтра Newest Arrivals для перехода"""
    def filter_newest(self):
        self.page.get_by_role(loc.ROLEBTN, name=loc.FEATURED).click()
        self.page.wait_for_timeout(500)

        # Выбираем фильтр
        self.page.get_by_text(loc.ARRIVALS).first.click()

        # Ждём обновления
        self.page.wait_for_timeout(2000)

        # ПОСЛЕ клика по фильтру
        name_filter_after = self.page.locator(loc.PRODNAME).last.inner_text()
        print(f"Название выбранного фильтра: {name_filter_after}")

        # Проверяем что открылась новая страница
        expect(self.page).to_have_url(f"{self.base_url}{FILTER_NEWEST}")
        print(f"✅ УСПЕХ, открылась новая стр по клику на фильтр {name_filter_after} \n")


    def page_name_az(self):
        self.page.get_by_role(loc.ROLEBTN, name=loc.FEATURED).click()
        self.page.wait_for_timeout(500)

        # Выбираем фильтр
        self.page.get_by_text(loc.NAMEAZ).first.click()

        # Ждём обновления
        self.page.wait_for_timeout(2000)

        # ПОСЛЕ клика по фильтру
        name_filter_after = self.page.locator(loc.PRODNAME).last.inner_text()
        print(f"Название выбранного фильтра: {name_filter_after}")

        # Проверяем что открылась новая страница
        expect(self.page).to_have_url(f"{self.base_url}{FILTER_NAME_AZ}")
        print(f"✅ УСПЕХ, открылась новая стр по клику на фильтр {name_filter_after}\n")


    def page_price_low(self):
        self.page.get_by_role(loc.ROLEBTN, name=loc.FEATURED).click()
        self.page.wait_for_timeout(500)

        # Выбираем фильтр
        self.page.get_by_text(loc.LOWTOHIGHT).first.click()

        # Ждём обновления
        self.page.wait_for_timeout(2000)

        # ПОСЛЕ клика по фильтру
        name_filter_after = self.page.locator(loc.FILTERTEXT).last.inner_text()
        print(f"Название выбранного фильтра: {name_filter_after}")

        # Проверяем что открылась новая страница
        expect(self.page).to_have_url(f"{self.base_url}{FILTER_PRICE_LOW}")
        print(f"✅ УСПЕХ, открылась новая стр по клику на фильтр {name_filter_after}\n")


    def page_price_high(self):
        self.page.get_by_role(loc.ROLEBTN, name=loc.FEATURED).click()
        self.page.wait_for_timeout(500)

        # Выбираем фильтр
        self.page.get_by_text(loc.HIGHTTOLOW).first.click()

        # Ждём обновления
        self.page.wait_for_timeout(2000)

        # ПОСЛЕ клика по фильтру
        name_filter_after = self.page.locator(loc.FILTERTEXT).last.inner_text()
        print(f"Название выбранного фильтра: {name_filter_after}")

        # Проверяем что открылась новая страница
        expect(self.page).to_have_url(f"{self.base_url}{FILTER_PRICE_HIGH}")
        print("✅ УСПЕХ, открылась новая стр по клику на фильтр!\n")


    def view_shopping_cart_on_product_cart(self):
        self.page.wait_for_selector(loc.PODUCTNAME, state=loc.VISIBLE)

        # Наводим на первый товар
        first_product = self.page.locator(loc.CART).first
        first_product.hover()

        # Проверяем что-то появилось кнопка quick_view_button
        quick_view_button = first_product.locator(loc.SHOPPINGCART)
        assert quick_view_button.is_visible()
        self.page.wait_for_timeout(500)  # Даём время на анимацию
        print("✅ Навели на товар")


    def click_shopping_cart_on_product_car(self):
        # Цепочка: найти элемент → кликнуть
        self.page.locator(loc.CART).first.click()


    """Тест перехода на страницу заказа первого продукта"""
    def page_first_product(self):
        self.page.wait_for_selector(loc.CART, state=loc.VISIBLE)

        # 2. Находим контейнер товаров
        products_container = self.page.locator(loc.PODUCTSGRID)

        # 3. Внутри находим первый товар
        first_product = products_container.locator(loc.CART).first

        # 4. Наводим на товар
        first_product.hover()
        self.page.wait_for_timeout(500)

        # 5. Внутри товара ищем название
        product_name = first_product.locator(loc.PODUCTNAME)
        name_text = product_name.inner_text()
        print(f"Товар: {name_text}")

        # 6. Кликаем на товар
        product_name.click()
        # 7. Проверяем что открылась страница товара
        expect(self.page).to_have_url(f"{self.base_url}{FIRST_PRODUCT}")
        print("✅ Цепочка действий выполнена!")


    """Полный тест продукта с hover и цепочками"""
    def page_last_product(self):
        print("\n" + "=" * 70)
        print("ТЕСТ: Наведение и цепочки действий")
        print("=" * 70)

        self.page.wait_for_selector(loc.CART, state=loc.VISIBLE)
        print("✅ Страница загружена")

        # 2. Получаем все товары
        products = self.page.locator(loc.CART)
        total = products.count()
        print(f"📦 Найдено товаров: {total}")

        # 3. Работаем с последним товаром - ЦЕПОЧКА ДЕЙСТВИЙ
        last_product = products.last

        # Прокручиваем до товара
        last_product.scroll_into_view_if_needed()
        print("   → Прокрутили к товару")

        # Наводим курсор
        last_product.hover()
        print("   → Навели курсор")
        self.page.wait_for_timeout(500)

        # Получаем название - ЦЕПОЧКА ЛОКАТОРОВ
        product_name_element = last_product.locator(loc.PODUCTNAME)
        product_name = product_name_element.inner_text()
        print(f"   → Название: {product_name}")

        # Проверяем видимость - ЦЕПОЧКА ПРОВЕРОК
        expect(product_name_element).to_be_visible()
        expect(product_name_element).not_to_be_empty()
        print("   → Проверки пройдены")

        # 4. Кликаем на товар
        product_name_element.click()

        # 5. Проверяем что открылась страница товара
        expect(self.page).to_have_url(f"{self.base_url}{LAST_PRODUCT}")
        print("✅ Цепочка действий выполнена!")
        print("✅ Открыли страницу товара")
        print("=" * 70 + "\n")


    def nested_locators(self):
        # Найти блок товаров → внутри найти первый товар → внутри найти кнопку
        shop_section = self.page.locator(loc.PODUCTSGRID)
        last_product = shop_section.locator(loc.CART).last
        buy_button = last_product.locator(loc.BTNPRIMARY)
        buy_button.click()


    def nested_locators_string(self):
        # Цепочка: найти элемент → кликнуть
        self.page.locator(loc.PODUCTSGRID).locator(loc.CART).first.locator(loc.BTNPRIMARY).click()
