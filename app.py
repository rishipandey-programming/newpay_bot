from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
import time

chrome_driver = "chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get("https://newpay.co.in/login.php")
user_name = driver.find_element_by_xpath('//*[@id="userid"]')
user_name.send_keys("RT1760")


password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Sridhar1973#")

login_btn = driver.find_element_by_xpath('//*[@id="loginSubmit"]/button')
login_btn.click()

time.sleep(0.7)

pin = driver.find_element_by_xpath('/html/body/div[3]/fieldset/input')
pin.send_keys("1234")

ok_btn = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div/button')
ok_btn.click()

time.sleep(0.7)

dmt_btn = driver.find_element_by_xpath('//*[@id="dashboardArea"]/div/div[1]/div[4]/a/div/div/span[1]')
dmt_btn.click()

driver.maximize_window()

click_mobile_input = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/div/form/div[1]/div/div/input')
click_mobile_input.click()