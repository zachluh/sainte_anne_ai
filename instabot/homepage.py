import dms
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import textgenrnn

class homepage:
    def __init__(self, browser, chat_button, i_list):
        self.browser = browser
        self.chat_button = chat_button
        self.i_list = i_list
        

    def enter_messages(self):
        checker = dms.dms(self.browser)
        self.browser.implicitly_wait(3)
        if checker.check_if_exists('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div'):
            self.browser.find_element_by_xpath(self.chat_button).click()

    def comment(self, new:int, total:int):
        for i in range(new, total-1):
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
            self.browser.implicitly_wait(3)
            self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form').click()
            form = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')))
            form.send_keys('a', Keys.RETURN)
            self.browser.implicitly_wait(2)
            self.browser.execute_script("window.history.go(-1)")
            if i == total:
                break
            else:
                i += 1

            

    def check_for_new_post(self):
        checker = dms.dms(self.browser)
        user = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text
        i = int((self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text).replace(",", "")) #total

        with open("post_id.txt","r") as f:
            lines = f.readlines()
        for n in lines:
            split = n.split()
            if int(split[1].rstrip("\n")) < i-1:
                new = int(split[1].rstrip("\n")) - (i-1)
                self.comment(new, i)

        self.i_list.append(f"{user} {i}\n")

    def add_new_values(self):
        with open("post_id.txt", "w") as f:
            f.truncate(0)
            for i in self.i_list:
                f.write(i)

    def sort(self):
        checker = dms.dms(self.browser)
        self.browser.get("https://www.instagram.com/sainteanne.ai/following/")
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        i = 1
        while True:
           self.browser.implicitly_wait(2)
           if checker.check_if_exists(f'/html/body/div[6]/div/div/div[3]/ul/div/li[{i}]/div/div[1]/div/div/a'): 
                self.browser.find_element_by_xpath(f'/html/body/div[6]/div/div/div[3]/ul/div/li[{i}]/div/div[1]/div/div/a').click()
                self.check_for_new_post()
                i +=1
                self.browser.get("https://www.instagram.com/sainteanne.ai/following/")
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
           elif checker.check_if_exists(f'/html/body/div[6]/div/div/div[3]/ul/div/li[{i}]/div/div[1]/div/div/span'):
                self.browser.find_element_by_xpath(f'/html/body/div[6]/div/div/div[3]/ul/div/li[{i}]/div/div[1]').click()
                self.browser.find_element_by_xpath(f'//*[@id="react-root"]/section/div[1]/div/section/div/header/div[2]/div[1]/div/div/div/div/a').click()
                self.check_for_new_post()
                i +=1
                self.browser.get("https://www.instagram.com/sainteanne.ai/following/")
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
           else:
               break
        self.add_new_values()

            
               


#//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[1]/div[3]/section[3]/div/form/textarea
#//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[2]/div[3]/section[3]/div/form/textarea
#//*[@id="react-root"]/section/main/section/div/div[2]/div/article[1]/div[3]/div[1]/div/div[2]/div[4]/div/span[1]/a
#//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[1]/div[3]/div[1]/div/div[2]/div[1]/a
#/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[1]/div/li/div/div[1]/div[2]/h3/div/span/a
#/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[1]/div/li/div/div[1]/div[2]/h3/div/span/a
#//*[@id="f13502e4ab6f18"]/div/div/span/a
#//*[@id="fef8feffae0898"]/div/div/span/a          
#/html/body/div[6]/div/div/div[3]/ul/div/li[2]/div
#/html/body/div[6]/div/div/div[3]/ul/div/li[1]/div
#/html/body/div[6]/div/div/div[3]/ul/div/li[1]/div/div[1]/div/div/a   
#/html/body/div[6]/div/div/div[3]/ul/div/li[1]/div/div[1]/div/div/a
#/html/body/div[6]/div/div/div[3]/ul/div/li[2]/div/div[1]/div/div/a   
#//*[@id="f36ad91fe85281"]/div
#//*[@id="f36ad91fe85281"]
#//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div/div[1]/a/div[1]/div[2]
#//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div/div[2]/a/div[1]/div[2]
#//*[@id="react-root"]/section/main/div/div[4]/article/div/div/div/div[2]/a/div[1]/div[2]
#//*[@id="react-root"]/section/main/div/header/section/div[1]/h2
#/html/body/div[6]/div/div/div[3]/ul/div/li[2]/div/div[1]/div/div/span/img
#/html/body/div[6]/div/div/div[3]/ul/div/li[2]/div/div[1]/div/div/span
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div/div[2]
#//*[@id="react-root"]/section/main/div/header/section/div[1]/h2
#/html/body/div[6]/div/div/div[3]/ul/div/li[2]/div/div[1]/div/div/span/img
#//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div[1]/div[2]