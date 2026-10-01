from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_page(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(page)

    assert inventory.get_title() == "Products"