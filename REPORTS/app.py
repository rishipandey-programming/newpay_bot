from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
import time

chrome_driver = r"C:\Program Files\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get("https://newpay.co.in/login.php")
user_name = driver.find_element_by_xpath('//*[@id="userid"]')
user_name.send_keys("RT1760")


password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Sridhar1973#")

login_btn = driver.find_element_by_xpath('//*[@id="loginSubmit"]/button')
login_btn.click()

time.sleep(1)

pin = driver.find_element_by_xpath('/html/body/div[3]/fieldset/input')
pin.send_keys("1234")

ok_btn = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div/button')
ok_btn.click()

time.sleep(0.7)

report_dropdown = driver.find_element_by_xpath('/html/body/div/aside/div/nav/ul/li[3]/a')
report_dropdown.click()

driver.maximize_window()

ledger_btn = driver.find_element_by_xpath('/html/body/div/aside/div/nav/ul/li[3]/ul/li[1]/a')
ledger_btn.click()

date_to = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/div/div[2]/form/div[2]/input').get_attribute("value")


date_from = driver.find_element_by_xpath('//*[@id="example1_filter"]/label/input')
date_from.send_keys(date_to)


# excel_btn = driver.find_element_by_xpath('//*[@id="example1_wrapper"]/div[1]/div[1]/div/button[2]')
# excel_btn.click()