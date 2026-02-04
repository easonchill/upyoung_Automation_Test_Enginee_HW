"""Pytest fixtures for Playwright."""
import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # 優先使用系統 Chrome，沙箱環境下 bundled chromium 可能 SEGV
        try:
            browser = p.chromium.launch(channel="chrome", headless=False)
        except Exception:
            browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(page: Page):
    """Page 已登入並在產品列表頁。"""
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/inventory.html")
    return page
