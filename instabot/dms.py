from selenium.common.exceptions import NoSuchElementException     
import os

class dms:
    def __init__(self, browser):
        self.browser = browser
    

    def check_if_exists(self, xpath):
        try:
            self.browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    def check_for_notifs(self):
        i = 0
        while True: 
            i += 1
            if self.check_if_exists(f'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{i}]') is True:
                if self.check_if_exists(f'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{i}]/a/div/div[3]/div') is True:
                    self.browser.find_element_by_xpath(f'//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{i}]').click()
                    self.get_all_messages()
            else:
                self.browser.get("https://www.instagram.com/")
                break

    def get_all_messages(self):
        text_list = []
        i = 0
        n = 0
        username = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div[1]/div').text
        while True:
            i += 1
            xpath = f'//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[{i}]/div[2]/div/div/div/div/div/div/div/div/span'
            if self.check_if_exists(xpath):
                n = 0
                text = self.browser.find_element_by_xpath(xpath).text
                text_list.append(text)
            else:
                n += 1
            if n == 2:
                self.annotate_user_messages(text_list, username)
                break

    
    def annotate_user_messages(self, list, username):
        username_in_use = False
        added_arguments = []
        with open("annotations.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            if username in line:
                username_in_use = True
                index = line.index(username)
                break
        print(username_in_use)
        if username_in_use is True:
            split = line.split()
            number = int(split[1].rstrip("\n"))
            print(number)
            print(list)
            for i in list:
                list.index(i)
                
                if list.index(i) + 1 >= number:
                    added_arguments.append(i)
                print(added_arguments)
            for arguments in added_arguments:
                with open("sample.txt", "a") as f:
                    f.write(f"{arguments}\n")
            lines[index] = f"{username} {len(list)}\n"
            with open("annotations.txt", "w") as f:
                f.writelines(lines)

        else:
            with open("annotations.txt", "a") as f:
                f.write(f"{username} {len(list)}\n")
            print(list)
            for i in list:
                with open("sample.txt", "a") as f:
                    f.write(f"{i}\n")




