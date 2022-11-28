
# ##  on DemoWebShop click on twitter and after opening twitter window click on Follow
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# import time
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
#
# driver1 = webdriver.Chrome(path)
#
# driver1.get("https://demowebshop.tricentis.com/")
# driver1.maximize_window()
# time.sleep(2)
#
# tw = driver1.find_element("xpath", "//a[text()='Twitter']")
#
# ac_obj = ActionChains(driver1)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
# tw.click()
# handles = driver1.window_handles
# time.sleep(1)
# print(handles)
#
# driver1.switch_to.window(handles[1])
#
# time.sleep(5)
#
#
# follow = driver1.find_element("xpath", "//span[text()='Follow'][1]")
# time.sleep(1)
# follow.click()


###############################################################################################
#############################################################################################

# ##                ####    Alert obj  #######
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# import time
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
#
# driver1 = webdriver.Chrome(path)
#
# driver1.get("https://demowebshop.tricentis.com/")
# driver1.maximize_window()
# time.sleep(2)
#
# driver1.find_element("xpath", "//input[@class='button-1 search-box-button']").click()
#
# ## Switch to alert
# alert_obj = driver1.switch_to.alert
#
# ## alert it or dismiss---> alert_obj.dismiss(), ok, accept
# alert_obj.accept()
# driver1.find_element("xpath", "//a[text()='Log in']").click()




################################################################################################
###########################################################################################




# ##                            dismiss an alert
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# import time
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
#
# driver1 = webdriver.Chrome(path)
#
# driver1.get("file:///C:/Users/Lenovo/Desktop/Selenium%20files/demo%20(1).html")
# driver1.maximize_window()
# time.sleep(3)
#
# driver1.find_element("xpath", "//button[text()='Delete']").click()
# time.sleep(2)
#
# ## Switch to alert
# alert_obj = driver1.switch_to.alert
#
# ## alert it or dismiss---> alert_obj.dismiss(), ok, accept
# alert_obj.dismiss()

###################################################################################################
################################################################################################



# ##                              File upload popups
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# import time
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
#
# driver1 = webdriver.Chrome(path)
#
# driver1.get("file:///C:/Users/Lenovo/Desktop/Selenium%20files/demo%20(1).html")
# driver1.maximize_window()
# time.sleep(3)
#
# driver1.find_element("xpath", "//button[text()='Delete']").click()
# time.sleep(2)
#
# ## Switch to alert
# alert_obj = driver1.switch_to.alert
#
# ## alert it or dismiss---> alert_obj.dismiss(), ok, accept
# alert_obj.dismiss()
# time.sleep(2)
#
# resume_path = r"C:\Users\Lenovo\Desktop\Pointer RESUME JAVA, SQL project RESUME.pdf"
# driver1.find_element("xpath", "//input[@id='resume']").send_keys(resume_path)
#

##################################################################################################
#################################################################################################

## search 'python jobs' on monsterindia and search. then click on first result

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


import time

path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"

driver1 = webdriver.Chrome(path)
driver1.implicitly_wait(10)

driver1.get("https://www.monsterindia.com/")
driver1.maximize_window()
time.sleep(2)

driver1.find_element("xpath", "//input[@id='SE_home_autocomplete']").send_keys("python jobs")
driver1.find_element("xpath", "//input[@value='Search']").click()



# driver1.find_element("xpath", "//div[@class='cardContainer activeCard']").click()

driver1.find_element("xpath", "//p[text()='Apply Now']").click()
time.sleep(5)
handles = driver1.window_handles

time.sleep(2)

driver1.switch_to.window(handles[1])
time.sleep(2)

driver1.find_element("xpath", "//input[@id='signInName']").send_keys("8556967816")
driver1.find_element("xpath", "//input[@id='password']").send_keys("12345")

