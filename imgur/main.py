import os
import json
from imgurpython import ImgurClient
from datetime import datetime
import sys

username = ""
password = ""
client_id = ""
client_secret = ""
authorization_url = ""
client = ImgurClient


def getCredentials():
    global username, password, client_id, client_secret
    if os.path.exists("credential.json"):
        file = open("credential.json", "r")
        contents = file.read()
        js = json.loads(contents)
        username = js['username']
        password = js['password']
        client_id = js['client_id']
        client_secret = js['client_secret']
        file.close()
    else:
        file = open("credential.json", "w+")
        username = input("Username : ")
        password = input("Password : ")
        client_id = input("Client_Id : ")
        client_secret = input("Client_Secret : ")
        dt = {"username": username, "password": password, "client_id": client_id, "client_secret": client_secret}
        text = json.dumps(dt)
        file.write(text)
        file.close()


def initClient():
    if password != "":
        global client, authorization_url
        client = ImgurClient(client_id, client_secret)
        authorization_url = client.get_auth_url('pin')
        print(authorization_url)
        # webbrowser.open(authorization_url)
        # pin = input("Input the pin from the url : ")

    else:
        getCredentials()
        initClient()


def listImage(path):
    return os.listdir(path)


def uploadImages(path):
    dt = {}

    if os.path.exists(os.getcwd() + "/" + path):
        i = path
        path = os.getcwd() + "/" + path
    initClient()
    for i in listImage(path):
        config = {'album': None, 'name': i, 'title': i, 'description': 'dated : {0}'.format(datetime.now())}
        print("Uploading Image : {0}".format(i))
        t = path+"/"+i
        image = client.upload_from_path(t, config=config, anon=False)
        dt[i] = image
    # os.remove(os.getcwd()+"/images/"+i)
    file = open("{0}_result.json".format(datetime.now()), "w+")
    file.write(json.dumps(dt))
    file.close()


def helpPrint():
    msg = "Welcome to Imgur Script \n\n " \
          "Use -f 'path' : To upload image from path \n " \
          "Use -d 'directory' : To upload images from directory \n "
    print(msg)


def uploadImage(path):
    if os.path.exists(path):
        i = os.path.basename(path)
    elif os.path.exists(os.getcwd() + "/" + path):
        i = path
        path = os.getcwd() + "/" + path

    initClient()
    dt = {}
    config = {'album': None, 'name': i, 'title': i, 'description': 'dated : {0}'.format(datetime.now())}
    print("Uploading Image : {0}".format(i))
    image = client.upload_from_path(path, config=config, anon=False)
    dt[i] = image
    # os.remove(os.getcwd()+"/images/"+i)
    file = open("{0}_result.json".format(datetime.now()), "w+")
    file.write(json.dumps(dt))
    file.close()


if __name__ == "__main__":
    # initClient()
    argumentList = sys.argv
    # print(argumentList)
    if len(argumentList) < 1:
        print("Welcome to Imgur Image Uploader\n\nUse -help to get details")
    elif argumentList[1] in ['-f', '-d', '-help']:
        if argumentList[1] == '-help':
            helpPrint()
        elif argumentList[1] == '-f':
            if len(argumentList) > 1:
                path = argumentList[2]
                uploadImage(path)
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
        elif argumentList[1] == '-d':
            if len(argumentList) > 1:
                path = argumentList[2]
                uploadImages(path)
            else:
                print("Invalid Argument passed\n\n")
                helpPrint()
