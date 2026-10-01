from pages.login_page import LoginPage


def test_valid_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    assert page.url.endswith("/inventory.html")


def test_invalid_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "standard_user",
        "wrong_password"
    )

    assert "Username and password do not match" in login.get_error()