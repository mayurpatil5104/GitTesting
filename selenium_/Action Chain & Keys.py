# import time
#
# ###############################         Mouse Actions               #############################
#
# from selenium.webdriver.common.action_chains import ActionChains      #From common ActionChains class imported
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
# driver1 = webdriver.Chrome(path)
# driver1.get("https://www.meesho.com/")
# driver1.maximize_window()
# time.sleep(1)
#
# women_ethnic = driver1.find_element("xpath", "//span[text()='Women Ethnic']")
# ac_obj = ActionChains(driver1)
# time.sleep(2)
#
# ac_obj.move_to_element(women_ethnic).perform()


###################################################################################################################

###########################################################################################################

import time
# from selenium.webdriver.common.action_chains import ActionChains      #From common ActionChains class imported
# from selenium.webdriver.common.keys import Keys
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
# driver1 = webdriver.Chrome(path)
# driver1.get("file:///C:/Users/Lenovo/Desktop/Selenium%20files/demo%20(1).html")
# driver1.maximize_window()
#
# ele_d_click = driver1.find_element("xpath", "//button[text()='Double-click me']")
#
# ac_obj = ActionChains(driver1)
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
# ac_obj.double_click(ele_d_click).perform()
#
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ## simulating keys
# ac_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()


#################################################################################################

####                                 MOnster india

from selenium.webdriver.common.action_chains import ActionChains      #From common ActionChains class imported
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
driver1 = webdriver.Chrome(path)
driver1.get("https://www.monsterindia.com/")
driver1.maximize_window()
time.sleep(3)

job_ser = driver1.find_element("xpath","//a[@data-check='menutab']")

ac_obj = ActionChains(driver1)
time.sleep(2)

ac_obj.move_to_element(job_ser).perform()
time.sleep(2)

job_skills = driver1.find_element("xpath", "//a[text()='Jobs by Skills']")
ac_obj.move_to_element(job_skills).perform()
time.sleep(2)

pyt_jobs = driver1.find_element("xpath", "//a[@href='https://www.monsterindia.com/search/python-jobs']")
ac_obj.move_to_element(pyt_jobs).perform()

ac_obj.click(pyt_jobs).perform()




###############################################################################################################


####                                DRAG and Drop on Gitbhub link

# from selenium.webdriver.common.action_chains import ActionChains      #From common ActionChains class imported
# from selenium.webdriver.common.keys import Keys
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
# driver1 = webdriver.Chrome(path)
#
# driver1.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
# driver1.maximize_window()
#
# source = driver1.find_element("xpath","//div[@id='draggable']")
# target = driver1.find_element("xpath", "//div[@id='droppable']")
#
# ac_obj = ActionChains(driver1)
# ac_obj.drag_and_drop(source,target).perform()


#################################################################################################



##                                  Context Click on DemoWebShop

# from selenium.webdriver.common.action_chains import ActionChains      #From common ActionChains class imported
# from selenium.webdriver.common.keys import Keys
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
#
# path = r"D:\Chrome and Brave downloads\chromedriver_win32\chromedriver.exe"
# driver1 = webdriver.Chrome(path)
#
# driver1.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver1.maximize_window()
#
#
# register = driver1.find_element_by_xpath("//a[text()='Register']")
#
# ac_obj = ActionChains(driver1)
# time.sleep(2)
#
# ac_obj.context_click(register).perform()
# time.sleep(1)
#
# ac_obj.send_keys(Keys.TAB).perform()
# time.sleep(1)
#
# ac_obj.send_keys(Keys.ENTER).perform()