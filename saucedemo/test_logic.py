import pytest
from playwright.sync_api import expect

from saucedemo.constants import LOGIN, PASSWORD


def test_site_accessibility(page):
    response = page.goto("https://www.saucedemo.com/")
    assert response.status == 200, f"Статус ответа: {response.status}"


def test_login(page):
    page.fill("#user-name", LOGIN)
    page.fill("#password", PASSWORD)
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_add_to_cart(page):
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator("#remove-sauce-labs-backpack")).to_be_visible()


def test_cart(page):
    page.click("#shopping_cart_container")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    (expect(page.locator(".inventory_item_name"))
     .to_have_text("Sauce Labs Backpack"))


def test_checkout(page):
    page.click("#checkout")
    (expect(page)
     .to_have_url("https://www.saucedemo.com/checkout-step-one.html"))
    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    (expect(page)
     .to_have_url("https://www.saucedemo.com/checkout-step-two.html"))


def test_complete_purchase(page):
    page.click("#finish")
    (expect(page.locator(".complete-header"))
     .to_have_text("Thank you for your order!"))


@pytest.mark.parametrize("test_function", [
    test_site_accessibility,
    test_login,
    test_add_to_cart,
    test_cart,
    test_checkout,
    test_complete_purchase
])
def test_saucedemo_purchase(page, test_function):
    test_function(page)
