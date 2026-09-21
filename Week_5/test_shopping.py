from Shopping import ShoppingCart

class TestShoppingCart:
    def test_new_empty_cart(self):
        cart = ShoppingCart()
        assert cart.count() == 0

    def test_new_zero_total(self):
        cart = ShoppingCart()
        assert cart.total() == 0

    def test_add_item_count(self):
        cart = ShoppingCart()
        cart.add("Book", 20)
        assert cart.count() == 1

    def test_add_item_total(self):
        cart = ShoppingCart()
        cart.add("Book", 20)
        cart.add("Pen", 5)
        assert cart.total() == 25