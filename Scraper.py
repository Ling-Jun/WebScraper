# Download chrome web driver. 
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

path = './chromedriver'

driver = webdriver.Chrome(path)

driver.get("https://www.csc-scc.gc.ca/index-en.shtml")
time.sleep(2)

# source = driver.page_source
# soup = BeautifulSoup(source, "html.parser")
# txt = soup.get_text()
# # find_string = soup.body.findAll(text='COVID')
# if  txt.find('COVID'):
#     try:
#         main = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.role, "main"))
#         )
#         print(main.text)
#     except:
#         driver.quit()


# # the link_text has to be very specific
# link = driver.find_element_by_link_text("Coronavirus disease (COVID-19)")
# link.click()

# # this gives the 1st element with such text, the return is a list object
# # elem.click() doesn't work, need to extract the list element, even if there is only
# # 1 element
# elem = driver.find_elements_by_xpath("//*[contains(text(), 'COVID')]")
# for e in elem:
#     e.click()


elems = driver.find_elements_by_xpath("//*[text()[contains(.,'COVID')]]")
# print(type(elems))
for elem in elems:
    # print(type(elem))
    try:
        elem.click()
        # print(elem)
        # print("clickable")
    except WebDriverException:
        print(elem)
        print("Not clickable")
    time.sleep(3)

# driver.switch_to_window(driver.window_handles[1])

source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
# print(soup)
print(driver.title)

# driver.quit()
