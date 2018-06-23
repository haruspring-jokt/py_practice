from selenium import webdriver

driver = webdriver.Chrome("C:/web_driver/chrome/chromedriver.exe")
driver.get("http://www.yahoo.co.jp")

assert "Yahoo! JAPAN" in driver.title

elem_search_word = driver.find_element_by_id("srchtxt")
elem_search_word.send_keys("selenium")
elem_search_btn = driver.find_element_by_id("srchbtn")
elem_search_btn.click()

elements_a = driver.find_elements_by_css_selector("#WS2m .w .hd h3 a")
for elem in elements_a:
    url = elem.get_property("href")
    print(url)

driver.close()