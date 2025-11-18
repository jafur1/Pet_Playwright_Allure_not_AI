from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.main_url = "https://the-internet.herokuapp.com/"

    def navigate(self, url: str = None):
        if not url:
            target_url = self.main_url
        elif url and url.startswith("https://"):
            target_url = url
        else:
            target_url = self.main_url + url
        self.page.goto(target_url)
        self.page.wait_for_load_state("networkidle")
        return self.page

