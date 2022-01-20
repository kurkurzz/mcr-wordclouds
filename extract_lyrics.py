import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='./chromedriver',options=op)
driver.get('https://www.azlyrics.com/m/mychemicalromance.html')

elements = driver.find_elements_by_class_name('album')

for element in elements:
	print(element.text)j