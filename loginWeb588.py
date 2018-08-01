# !/usr/bin/python
# coding:utf-8

from selenium import webdriver
# import chrome driver
driver = webdriver.Chrome()

driver.get("https://www.588v1.info/")
driver.find_element_by_link_text("会员中心").click();
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/input").send_keys("adtest06")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]/input").send_keys("1234qwer")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/form/div[4]/div/div/div[1]/button").click()
