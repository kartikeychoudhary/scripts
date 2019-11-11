import requests
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import os
class zippy:

    def __init__(self, url):
        self.url = url
    
    def getUrl(self):
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source)
        a = soup.find_all("a", id="dlbutton")
        link = a[0]['href']
        driver.quit()
        return "https://www98.zippyshare.com" + link 
    
    def downloadUrl(self):
        d_url = self.getUrl()
        name = d_url.split('/')[-1]
        os.system("wget " + d_url  + " -O " + name)

def helpPrint():
    msg = "Welcome to ZippyShare Downlaoder \n\n " \
          "Use -l 'link' : To download from sinle link \n " \
          "Use -f 'file' : To download from links saved in a file \n " \
          "Use -fs 'file' : To save links to a result.txt \n "

    print(msg)


if __name__ ==  "__main__":
    argumentList = sys.argv
    if len(argumentList) == 1:
        print("Welcome to Zippyshare Downloader \nUse -help to get details\n")
        #uploadImage("testocr.png")
    elif argumentList[1] in ['-l','-f', '-fs', '-help']:
        if argumentList[1] == '-help':
            helpPrint()
        elif argumentList[1] == '-l':
            if len(argumentList) > 1:
                url = argumentList[2]
                obj = zippy(url)
                obj.downloadUrl()
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
        elif argumentList[1] == '-f':
            
            if len(argumentList) > 1:
                path = argumentList[2]
                if os.path.exists(path):
                    i = os.path.basename(path)
                elif os.path.exists(os.getcwd() + "/" + path):
                    i = path
                    path = os.getcwd() + "/" + path
                with open(path, 'r') as f:
                    links = f.readlines()
                f.close()
                for i in links:
                    obj = zippy(i)
                    obj.downloadUrl()
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
        elif argumentList[1] == '-f':

            if len(argumentList) > 1:
                path = argumentList[2]
                if os.path.exists(path):
                    i = os.path.basename(path)
                elif os.path.exists(os.getcwd() + "/" + path):
                    i = path
                    path = os.getcwd() + "/" + path
                with open(path, 'r') as f:
                    links = f.readlines()
                f.close()
                for i in f:
                    obj = zippy(i)
                    obj.downloadUrl()
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
        elif argumentList[1] == '-fs':

            result = []
            if len(argumentList) > 1:
                path = argumentList[2]
                if os.path.exists(path):
                    i = os.path.basename(path)
                elif os.path.exists(os.getcwd() + "/" + path):
                    i = path
                    path = os.getcwd() + "/" + path
                with open(path, 'r') as f:
                    links = f.readlines()
                f.close()
                for i in links:
                    print(i)
                    if(len(i)>5):
                        obj = zippy(i)
                        try:
                            r = obj.getUrl()
                            print(r)
                            result.append(r)
                        except:
                            print(str(i) + " did not get processed")
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
            string = ""
            for i in result:
                string += i+"\n"
            
            with open("result.txt", "w+") as f:
                f.write(string)

            f.close()
            print("DONE")


