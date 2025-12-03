import pytest
import allure
from allure_commons.types import AttachmentType
from selector.main_page import MainPage
from playwright.sync_api import Browser


@pytest.fixture(scope="function")
def main_page(page):
    return MainPage(page)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    page = item.funcargs.get("page")
    if not page:
        return

    if report.failed:
        try:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="page_screenshot",
                attachment_type=AttachmentType.PNG,
            )
        except Exception:
            pass

        try:
            allure.attach(
                page.content(),
                name="page_source",
                attachment_type=AttachmentType.HTML,
            )
        except Exception:
            pass

@pytest.fixture
def make_auth_page(browser: Browser):
    def _make_auth_page(username="", password=""):
        creds = {'username': username, 'password': password} if username or password else None
        context = browser.new_context(http_credentials=creds)
        page = context.new_page()
        return page, context
    return _make_auth_page