from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com/"):
        self.page = page
        self.base_url = base_url

    def goto(self) -> "LoginPage":
        self.page.goto(self.base_url)
        return self

    def login(self, username: str, password: str) -> None:
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
