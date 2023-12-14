import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720


@pytest.fixture(autouse=True)
def browser_open_google():
    browser.open('https://google.com')
