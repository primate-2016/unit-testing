import pytest
from SuperMarketCheckout import *

@pytest.fixture() # create a test fixture which instantiates the Checkout() class so we don't have to repeat this in every test case
def checkout_fixture():
    checkout_fixture = Checkout()
    return checkout_fixture

def test_CanCalculateTotal(checkout_fixture):
    checkout_fixture.addItemPrice("apple", 1)
    checkout_fixture.addItem("apple")
    assert checkout_fixture.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout_fixture):
    checkout_fixture.addItemPrice("apple", 1)
    checkout_fixture.addItemPrice("banana", 2)
    checkout_fixture.addItem("apple") # addItem is used to keep a running total of the cost of the items added to the checkout class, so adding an apple increases the total by the price of one apple
    checkout_fixture.addItem("banana")
    assert checkout_fixture.calculateTotal() == 3

def test_CanAddDiscountRule(checkout_fixture):
    checkout_fixture.addDiscount("apple", 3, 2) # the discount price for 3 apples is 2 (rather than 3)

def test_CanApplyDiscountRule(checkout_fixture):
    checkout_fixture.addDiscount("apple", 3, 2) # so the minimum nbr of things we can add the to checkout is 3 to make this test pass
    checkout_fixture.addItem("apple")
    checkout_fixture.addItem("apple")
    checkout_fixture.addItem("apple")
    assert checkout_fixture.calculateTotal() == 2 # we know the total should be 2 based on the discount rule above.
