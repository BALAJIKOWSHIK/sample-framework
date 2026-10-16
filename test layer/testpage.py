import re
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login_e2e(login_page: LoginPage):
    # 1. Perform action using the Page Object
    login_page.login("tomsmith", "SuperSecretPassword!")

    # 2. Assert outcome in the test file
    expect(login_page.page).to_have_url(re.compile(r".*/secure"))
    expect(login_page.flash_message).to_contain_text("You logged into a secure area!")
    expect(login_page.logout_button).to_be_visible()

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("wronguser", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "wrongpassword", "Your password is invalid!"),
    ],
)
def test_invalid_login_shows_error(login_page: LoginPage, username: str, password: str, expected_error: str):
    # Reuses the exact same Page Object method with different test data
    login_page.login(username, password)

    expect(login_page.flash_message).to_contain_text(expected_error)
    expect(login_page.page).to_have_url(re.compile(r".*/login"))