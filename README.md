# SauceDemo Automated Tests

Automated tests for the www.saucedemo.com website using Selenium and pytest.

## Test Cases
1. `test_valid_login` - logs in with 'standard_user' and checks that Products page opens
2. `test_locked_out_user` - logs in with 'locked_out_user' and checks that error message is shown
3. `test_checkout` - adds a backpack to the cart, completes checkout, and checks that "Thank you for your order!" is shown
## Requirements
- python 3.11 or higher
- google chrome browser
## Setup
```
pip install -r requirements.txt
```
## Run Tests
```
pytest -v
```
## Project Structure
-  `conftest.py` - opens and closes Chrome for each test
- `test_login.py` - contains the 3 test cases
- `requirements.txt` - list of packages to install

## Notes
- Chrome shows a "Change your password" popup after logging in with `secret_sauce`, which blocked Selenium's clicks. To fix this, Chrome runs in guest mode.
- `implicitly_wait(10)` makes Selenium wait up to 10 seconds for elements to load, so the tests don't fail randomly.