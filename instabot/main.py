import tensorflow
import keras
import keras.backend.tensorflow_backend as tfback
from textgenrnn import textgenrnn
import selenium as sn
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from homepage import homepage
import time
import dms

PATH=r"C:\Users\bruhm\Desktop\chromedriver\chromedriver.exe"

with open("creds.txt", "r") as f:
    creds = f.read().split()



def login(user, password):
    browser.implicitly_wait(2)
    user_prompt = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    pass_prompt = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    user_prompt.send_keys(user)
    pass_prompt.send_keys(password, Keys.ENTER)
    time.sleep(3)
    #browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()


    home = homepage(browser, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a', [])
    return home

#
browser = wb.Chrome(PATH)
insta_dms = dms.dms(browser)

browser.get("https://www.instagram.com/")

home = login(creds[0], creds[1])



home.enter_messages()
insta_dms.check_for_notifs()
home.sort()


#textgen = textgenrnn()

#textgen.train_from_file('sample.txt', num_epochs=5)
#textgen.generate(5, temperature=0.1)
