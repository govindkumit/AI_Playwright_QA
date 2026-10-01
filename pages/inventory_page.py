class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.title = page.locator(".title")
        self.cart = page.locator(".shopping_cart_link")

    def get_title(self):
        return self.title.inner_text()

    def open_cart(self):
        self.cart.click()