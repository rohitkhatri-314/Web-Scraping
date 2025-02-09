from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

service= Service(r'C:\Users\rohit\Downloads\chromedriver.exe')

def get_driver(text):
  
  options= webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_argument("--disable-gpu")
  options.add_experimental_option('excludeSwitches', ['enable-logging'])

  driver=webdriver.Chrome(service= service,options=options)
  driver.get(text)
  return driver
  
def clean_text(text):
   clean=float(text.split(": ")[1])
   return clean

def append_to_file(data,filename="temperatures.txt"):
   with open(filename ,"a") as file:
     file.write(data+"\n")

def get_time():
  driver_time=get_driver("https://www.rapidtables.com/tools/current-time.html")
  current_time=driver_time.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[1]/form/div[1]/div[1]")
  date=driver_time.find_element(by="xpath", value="/html/body/div[2]/div[2]/div[1]/form/div[1]/div[3]")
  return (date.text + " : " + current_time.text)

def main():
  driver=get_driver("https://automated.pythonanywhere.com/")
  time.sleep(2)
  element=driver.find_element(by="xpath",value="html/body/div[1]/div/h1[2]")
  
  try:
    while True:
      current_time=get_time()
      append_to_file(get_time()+ " : " + element.text)
      time.sleep(2)
  except KeyboardInterrupt:
    print(f"Process Stopped by the user")

      
  
  # the below lines of code are for automation of login that are commented:
  
  # driver.find_element(by="id", value="id_username").send_keys("automated")
  # time.sleep(2)
  # driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  # time.sleep(2)
  # driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
  
 

print(main())


