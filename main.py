import requests
import random
import json
import threading
import uuid
import os
import time

clear = lambda: os.system('cls')

def createAccount():
  
  t = threading.Thread(target=createAccount)
  t.start
   
  url = "https://spclient.wg.spotify.com/signup/public/v2/account/create"

  name = "daniel" + str(random.randint(100, 999))
  email = "mark" + str(random.randint(100, 9999)) + "@gmail.com"
  password = "dinosaur" + str(random.randint(100, 999))
  gender = random.randint(1,2)
  installID = str(uuid.uuid4())


  payload = {
    "account_details": {
      "birthdate": "2000-05-01",
      "consent_flags": {
        "eula_agreed": True,
        "send_email": False,
        "third_party_email": False
      },
      "display_name": name,
      "email_and_password_identifier": {
        "email": email,
        "password": password
      },
      "gender": gender
    },
    "callback_uri": "",
    "client_info": {
      "api_key": "a1e486e2729f46d6bb368d6b2bcda326",
      "app_version": "v2",
      "capabilities": [
        1
      ],
      "installation_id": installID,
      "platform": "www"
    },
    "tracking": {
      "creation_flow": "",
      "creation_point": "",
      "referrer": ""
    }
  }

  headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": str(len(json.dumps(payload))),
    "Content-Type": "application/json",
    "Host": "spclient.wg.music.apple.com",
    "Origin": "https://www.music.apple.com",
    "Referer": "https://www.music.apple.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
  }

  session = requests.Session()
  r = session.post(url=url, headers=headers, json=payload, timeout=15)

  if r.status_code == 200:
    with open("accounts.txt", "a") as file:
      file.write(str(email) + " : " + str(password) + "\n")
      print("Success: " + str(email) + ", " + str(password))
  else:
    print("Failed  : " + str(email) + ", " + str(password))
    return

def send():
  
  print("Tool created by savage dinosaur#8984")
  count = int(input("How many accounts will be created?" + "\n" + "[?] ---> "))
  clear()
  print("Sending started...")

  for i in range(count):
    createAccount()

  print("""Sending completed! Check your "accounts.txt" file.""")
  
  restart()

def restart():
  
  a = input("\n" + "Do you want to continue?" + "\n" + "[Y/N] : ")
  if a == "Y":
    clear()
    send()
  elif a == "y":
    clear()
    send()
  elif a == "N":
    quit()
  elif a == "n":
    quit()
  else:
    clear()
    print("Wrong key pressed!")
    restart()
    
send()
