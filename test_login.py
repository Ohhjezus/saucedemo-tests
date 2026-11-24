from selenium.webdriver.common.by import By
def login(driver, username):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def test_valid_login(driver):
    login(driver, "standard_user")
    assert "inventory" in driver.current_url

def test_locked_out_user(driver):
    login(driver, "locked_out_user")
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    assert error_text == "Epic sadface: Sorry, this user has been locked out."

def test_checkout(driver):
    login(driver, "standard_user")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("ursula")
    driver.find_element(By.ID, "last-name").send_keys("jezu")
    driver.find_element(By.ID, "postal-code").send_keys(20240)
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    complete_text = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]').text
    assert complete_text == "Thank you for your order!"