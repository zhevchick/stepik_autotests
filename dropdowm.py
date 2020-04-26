from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text

    def calc():
        z = str(int(a) + int(b))
        return z

    d = calc()

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(d)

    knopa = browser.find_element_by_css_selector("button.btn")
    knopa.click()

finally:
    time.sleep(10)
    browser.quit()


