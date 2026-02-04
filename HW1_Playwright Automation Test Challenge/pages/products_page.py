from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def get_title_text(self) -> str:
        return self.page.locator(".title").first.inner_text()

    def add_product_by_name(self, product_name: str) -> None:
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def get_cart_badge_count(self) -> int:
        badge = self.page.locator(".shopping_cart_badge")
        if not badge.is_visible():
            return 0
        return int(badge.inner_text())

    def open_cart(self) -> None:
        self.page.locator(".shopping_cart_link").click()

    def get_product_prices(self) -> list[float]:
        """回傳產品列表上的價格 (依 DOM 順序)。"""
        prices = []
        for el in self.page.locator(".inventory_item_price").all():
            text = el.inner_text()
            prices.append(float(text.replace("$", "")))
        return prices

    def set_sort(self, option: str) -> None:
        """option: 'Name (A to Z)' | 'Name (Z to A)' | 'Price (low to high)' | 'Price (high to low)'"""
        self.page.locator(".product_sort_container").select_option(label=option)
