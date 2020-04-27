import time
from datetime import datetime as dt
host_temporary="hosts"
hosts="C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
websiteList=["www.facebook.com","facebook.com","proxyof.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours!!")
        with open(hosts,"r+") as file:
            content=file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hosts,"r+") as file:

            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
        print("Fun hours")
    time.sleep(5)


