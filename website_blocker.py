from datetime import datetime as dt
import time

file_path = "C:\Windows\System32\drivers\etc"
website_list = ["www.facebook.com", "www.youtube.com"]
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Business time...")
        with open(file_path, 'r+') as file:
            data = file.read()
            for website in website_list:
                if website in data:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(file_path, 'r+') as file:
            readLines = file.readlines()           # creates a list of string
            file.seek(0)                           # the file line pointer sets to the beginning
            for line in readLines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()                    # delete the old data

        print("Fun time...")
    time.sleep(5)

