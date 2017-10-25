from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def googlesearch(key):
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    assert 'Google' in browser.title
    #send query key
    elem = browser.find_element_by_name('q')  # Find the search box
    elem.send_keys(key)
    elem.submit()

    #retrieve results
    RESULTS_LOCATOR = "//div/h3/a"

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))
    search_results = browser.find_elements(By.XPATH, RESULTS_LOCATOR)

    browser.quit()
    return search_results
