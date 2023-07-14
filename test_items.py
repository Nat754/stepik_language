import time
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(2)
    assert es.visibility_of_element_located(button), "Button is not visible"
