from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class LoginAutomation:
   """
   This class is used to login into the https://www.saucedemo.com/ webpage using the username and password


   url = https://www.saucedemo.com/
   username = standard_user
   password = secret_sauce
   """


   def __init__(self, url="https://www.cowin.gov.in/"):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


   def boot(self):
       """
       This method is to open up the chrome browser with the URL and makes the browser to go fullscreen. Then waits for 3 seconds
       :return:
       """
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()




   def quit(self):
       """
       This method is used to close the webbrowser
       :return:
       """
       self.driver.quit()


   def login(self):
       self.boot()

       self.driver.get("https://www.cowin.gov.in/")

       # Open a new tab
       self.driver.execute_script("window.open('about:blank', '_blank')")
       sleep(3)
       # window_handles = ["guvi.in", "about:blank", ... ]
       self.driver.switch_to.window(self.driver.window_handles[1])
       sleep(3)
       self.driver.get("https://www.cowin.gov.in/faq")
       print("FAQ")
       print(self.driver.current_window_handle)
       sleep(3)
       self.driver.execute_script("window.open('about:blank', '_blank')")
       sleep(3)
       self.driver.switch_to.window(self.driver.window_handles[2])
       sleep(3)
       print("Partner")
       self.driver.get("https://www.cowin.gov.in/our-partner")
       print(self.driver.current_window_handle)
       sleep(3)
       self.driver.close()
       sleep(3)
       self.quit()


obj = LoginAutomation()
obj.login()


