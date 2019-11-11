import sys
import os
import configparser

def helpPrint():
    msg = "Welcome to Google OCR \n\n " \
          "Use -f 'path' : To convert Image to txt from path \n " \
          "Use -d 'directory' : To convert all Images to txt from directory \n "
    print(msg)

if __name__ == "__main__":
 
    argumentList = sys.argv
    #print(sys.argv)
    if len(argumentList) == 1:
        print("Welcome to Google OCR\nUse -help to get details\n")
        #uploadImage("testocr.png")
    elif argumentList[1] in ['-f', '-d', '-help']:
        if argumentList[1] == '-help':
            helpPrint()
        elif argumentList[1] == '-f':
            if len(argumentList) > 1:
                path = argumentList[2]
                config = configparser.ConfigParser()
                config['system'] = {'path':path}
                with open('system.ini', 'w') as configfile:
                    config.write(configfile)
                configfile.close()

                os.system("python uploadImage.py")
                
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
        elif argumentList[1] == '-d':
            
            if len(argumentList) > 1:
                path = argumentList[2]
                config = configparser.ConfigParser()
                config['system'] = {'path':path}
                with open('system.ini', 'w') as configfile:
                    config.write(configfile)
                configfile.close()

                os.system("python uploadImages.py")
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()