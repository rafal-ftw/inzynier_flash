import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class interpreter():
    
    driver = webdriver.Chrome()

    def readStep(self, args):
        self.args = args

        id = args[0]

            # WEB OPERATIONS
        
        if id == "resolution":
            x = (args[1].split("x"))[0]
            y = (args[1].split("x"))[1]
            self.driver.set_window_size(x, y)
        
        elif id == "maximize":
            self.driver.maximize_window()

        elif type(id) == int:
            self.driver.implicitly_wait(id)
            print("***** IMPLICITLY WAIT " + args[0] +  " SECONDS *****")
        
        elif id == "goto":
            if args[1].startswith("https"):
                self.driver.get(str(args[1]))
                print("***** GO TO " + args[1] +  " ADDRESS *****")
            else:
                print("The link is not valid")

        elif id == "click":
            self.driver.find_element(By.XPATH, args[1]).click()
            print("***** CLICK ON " + args[1] +  " ELEMENT *****")

        elif id == "sendkeys":
            self.driver.find_element(By.XPATH, args[2]).send_keys(args[1])
            print("***** PROVIDED " + args[1] +  " VALUE TO " + args[2] + " ELEMENT *****")            
            print("\n\n\n\***** PROVIDED %s VALUE TO %s ELEMENT *****\n\n\n" % (args[1], args[2]))

        elif id == "ss":
            self.driver.save_screenshot(str(os.getcwd()) + "\\app\\screenshots\\")

        
            # ASSERTION
            
        elif id == "source":
            if args[1] in self.driver.page_source:
                print("JEST W SOSIE")
            else:
                print("NIE MA W SOSIE")

        elif id == "link":
            actualUrl = self.driver.current_url()
            if actualUrl == args[1]:
                print("JEST GICIK")
            else:
                print("LIPA")
        elif id == "title":
            actualTitle = self.driver.title()
            if actualTitle == args[1]:
                print("JEST GICIK")
            else:
                print("LIPA")


        print(self.args)