from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from githubgirisbilgisi import e_mail , psw
from selenium.webdriver.common.by import By
import time

url = "https://github.com/login"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(2)

inp1 = driver.find_element("id","login_field")
inp1.send_keys(e_mail)

inp2 = driver.find_element("id","password")
inp2.send_keys(psw)

submit = driver.find_element("name","commit")
submit.send_keys(Keys.ENTER)

url_2 = "https://github.com/{username}?tab=followers"
driver.get(url_2)
follower = driver.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
for i in follower:
    f1 = i.find_element(By.CSS_SELECTOR,".f4.Link--primary").text
    print(f1)
time.sleep(3)

driver.close()


