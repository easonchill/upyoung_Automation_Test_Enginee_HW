"""
Saucedemo E2E 測試。
主流程 + Bonus：購物車小計、排序 Price low to high。
"""
import pytest
from playwright.sync_api import Page

from pages import LoginPage, ProductsPage, CartPage, CheckoutPage


def test_full_checkout_flow(page: Page):
    """Tasks 1–8: 登入 → 加購 → 購物車 → Checkout → 確認 THANK YOU."""
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    page.wait_for_url("**/inventory.html")
    products = ProductsPage(page)
    assert products.get_title_text() == "Products"

    products.add_product_by_name("Sauce Labs Backpack")
    assert products.get_cart_badge_count() == 1

    products.open_cart()
    page.wait_for_url("**/cart.html")
    cart = CartPage(page)
    names = cart.get_cart_item_names()
    assert "Sauce Labs Backpack" in names

    cart.click_checkout()
    page.wait_for_url("**/checkout-step-one.html")
    checkout = CheckoutPage(page)
    checkout.fill_info("Alice", "Chen", "10001")
    checkout.click_continue()

    page.wait_for_url("**/checkout-step-two.html")
    checkout.click_finish()

    page.wait_for_url("**/checkout-complete.html")
    assert checkout.get_complete_message() == "THANK YOU FOR YOUR ORDER"


def test_cart_subtotal(logged_in_page: Page):
    """Bonus: 購物車內品項加總與顯示的 subtotal 一致。"""
    page = logged_in_page
    products = ProductsPage(page)
    products.add_product_by_name("Sauce Labs Backpack")
    products.open_cart()

    page.wait_for_url("**/cart.html")
    cart = CartPage(page)
    expected_subtotal = cart.get_subtotal_from_items()

    # 購物車頁只有品項價格，沒有單獨的 subtotal 區塊；在 checkout-step-two 才有
    cart.click_checkout()
    checkout = CheckoutPage(page)
    checkout.fill_info("Alice", "Chen", "10001")
    checkout.click_continue()

    page.wait_for_url("**/checkout-step-two.html")
    # 頁面上的 subtotal 在 .summary_subtotal_label，格式 "Item total: $29.99"
    summary = page.locator(".summary_subtotal_label").inner_text()
    import re
    match = re.search(r"\$([\d.]+)", summary)
    assert match
    actual_subtotal = float(match.group(1))
    assert actual_subtotal == expected_subtotal


def test_sort_price_low_to_high(logged_in_page: Page):
    """Bonus: 選擇 Price (low to high) 後，產品依價格由低到高排序。"""
    products = ProductsPage(logged_in_page)
    prices_before = products.get_product_prices()

    products.set_sort("Price (low to high)")
    # 等 URL 或列表更新（sort 會反映在 DOM）
    logged_in_page.locator(".inventory_item_price").first.wait_for(state="visible")
    prices_after = products.get_product_prices()

    assert prices_after == sorted(prices_before)
