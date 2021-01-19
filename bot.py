from selenium import webdriver
import time 
import os,time 

driver = webdriver.Chrome(executable_path=r"C:\chromedriver/chromedriver.exe")

driver.get("https://web.whatsapp.com/")
time.sleep(10)

celular = "Numero de celular a eleccion"
mensaje = "1 2 3 probando funciona el bot"

driver.get("https://wa.me/"+celular+"?text="+mensaje)

time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)
btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(30)

btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(5)

print("--bot terminado--")

time.sleep(40)


driver.close()

