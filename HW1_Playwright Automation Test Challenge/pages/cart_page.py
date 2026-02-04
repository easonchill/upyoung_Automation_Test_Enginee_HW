from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def get_cart_item_names(self) -> list[str]:
        return [el.inner_text() for el in self.page.locator(".inventory_item_name").all()]

    def get_subtotal_from_items(self) -> float:
        """從品項價格加總計算 subtotal（不含稅）。"""
        total = 0.0
        for el in self.page.locator(".inventory_item_price").all():
            total += float(el.inner_text().replace("$", ""))
        return total

    def click_checkout(self) -> None:
        self.page.get_by_role("button", name="Checkout").click()
