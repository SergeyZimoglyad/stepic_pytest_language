import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or es")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")
    if language != " ":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Error input language")
    yield browser
    print("\nquit browser..")
    browser.quit()
