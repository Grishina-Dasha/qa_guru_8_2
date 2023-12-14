from selene.support.shared import browser
from selene import be, have


def test_search_1(setting_browser, browser_open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_search_2(setting_browser, browser_open_google):
    browser.element('[name="q"]').should(be.blank).type('ghdfgdfhfgfherwtetteryery').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("Нет результатов поиска")
