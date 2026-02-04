from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_placeholder("Zip/Postal Code").fill(postal_code)

    def click_continue(self) -> None:
        self.page.get_by_role("button", name="Continue").click()

    def click_finish(self) -> None:
        self.page.get_by_role("button", name="Finish").click()

    def get_complete_message(self) -> str:
        return self.page.locator(".complete-header").inner_text()
