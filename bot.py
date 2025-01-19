import aiohttp
import asyncio
import random
import string
import json
import requests
from datetime import datetime
from colorama import Fore, Style, init
import time
# تفعيل colorama
init(autoreset=True)

def generate_custom_cookie():
    def random_string(length):
        # توليد سلسلة عشوائية تحتوي على أحرف وأرقام
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    # تقسيم الكوكيز إلى أجزاء بأطوال مختلفة
    parts = [
        random_string(10),  # الجزء الأول
        random_string(20),  # الجزء الثاني
        str(random.randint(1000000000, 9999999999)),  # رقم طويل
        random_string(7),   # الجزء الرابع
        random_string(15),  # الجزء الخامس
        random_string(40),  # الجزء السادس
        random_string(20),  # الجزء السابع
        random_string(30),  # الجزء الثامن
        random_string(25)   # الجزء الأخير
    ]
    
    # دمج الأجزاء باستخدام النقاط
    cookie = '.'.join(parts)
    return cookie

def generate_random_email():
    """Generate a random email address."""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@gmail.com"

def send_task_request(token, task_id):
    """Send the task request for a given token and task ID."""
    url = "https://api.bio-chain.cc/api/user/task_center_receive"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "cookie": f"cf_clearance={generate_custom_cookie()}",
        "origin": "https://bio-chain.cc",
        "priority": "u=1, i",
        "referer": "https://bio-chain.cc/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "st-ctime": "1737204617756",
        "st-lang": "en",
        "st-ttgn": "256988b18568f4689041fb75c662ae0c",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    payload = {"task_id": task_id}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request for token: {token}, task_id: {task_id}")
        print(e)
        return None

async def register_user(session, account_number, ref):
    url = "https://api.bio-chain.cc/api/user/register"
    
    params = {
        'lang': "en"
    }

    payload = {
        "account": generate_random_email(),
        "pwd": "e3dfbe7b1d42bb62c0a3c0608438fa0d",
        "user_type": 1,
        "code": f"{ref}",
        "safety_pwd": "e3dfbe7b1d42bb62c0a3c0608438fa0d",
        "ws": "",
        "te": "",
        "email_code": "",
        "captcha": ""
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'Content-Type': "application/json",
        'st-lang': "en",
        'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        'st-ctime': "1737219767975",
        'sec-ch-ua-mobile': "?1",
        'st-ttgn': "0c9d45a44cac24b3bcdb759a454c1d60",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://bio-chain.cc",
        'sec-fetch-site': "same-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://bio-chain.cc/",
        'accept-language': "en-US,en;q=0.9",
        'Cookie': f"cf_clearance={generate_custom_cookie()}"
    }

    try:
        async with session.post(url, params=params, json=payload, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                token = result.get("data", {}).get("token")
                if token:
                    with open("token.txt", "a") as file:
                        file.write(f"{token}\n")
                    print(f"{Fore.GREEN}Token for Account {account_number} saved successfully!")
                    await asyncio.sleep(6)
                else:
                    print(f"{Fore.RED}Token not found for Account {account_number}.")
            else:
                print(f"{Fore.RED}Error for Account {account_number}: {response.status}")
    except aiohttp.ClientError as e:
        print(f"HTTP request failed for Account {account_number}: {e}")
def start_airdrop_mining(token):
    """Send the start airdrop mining request for a given token."""
    url = "https://api.bio-chain.cc/api/user/start_airdrop_mining"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-length": "0",
        "cookie": f"cf_clearance={generate_custom_cookie()}",
        "origin": "https://bio-chain.cc",
        "priority": "u=1, i",
        "referer": "https://bio-chain.cc/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "st-ctime": "1737203130959",
        "st-lang": "en",
        "st-ttgn": "9f423205aca4a3f08307a98c7bde8d09",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    try:
        response = requests.post(url, headers=headers)
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending request for token: {token}")
        print(e)
        return None
        
        
def send_claim_request(token):
    url = "https://api.bio-chain.cc/api/user/receive_airdrop_mining"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "content-length": "0",
        "cookie": "cf_clearance=lI6Q29QWKwDJUKawaE4Ff8vV8zP0Z6FkRLszGREO.PU-1737203968-1.2.1.1-fjKFjUgFEGtApWSmvLikwI0EKWZdVOtYuiRGOlaWGTjMUxzn_vrINV19s3Zb3yKUfYBfr3AtWx1Ug9WhFqvS2gld.oZpHPjU2DHA2rw35xbzymrkZKjHoNDiBpL0ZbZjndJ7fh74WGzUaZQOdgN_Jv1LK7EN15kq4rFBS5uw5.S07QBdhRPiUuYBfO61YweEMUj.9rMddUfPqsgI3D2pcqkg4O2iVt_CXiafOJdB_HOLkDh.gqNrA6TvKJF41M1MAlhB1Je.9I7sIrJjgxEE6w36MGhkkN3VUPaEj0M9dU8",
        "origin": "https://bio-chain.cc",
        "priority": "u=1, i",
        "referer": "https://bio-chain.cc/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "st-ctime": "1737379316314",
        "st-lang": "en",
        "st-ttgn": "30f3c40a88d0ea21d6d489c89804dc6e",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
           pe = print(f"Success: {response.json()}")
           return pe
        else:
            print(f"Failed for token {token}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending request for token {token}: {e}")        
        
        
        
async def main():
    try:
        num_accounts = int(input("Enter the number of accounts to generate: "))
        ref = int(input("Ref Code Like[7892731]: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, num_accounts + 1):
            tasks.append(register_user(session, i, ref))
        await asyncio.gather(*tasks)
    
    # بعد الانتهاء من الحسابات نقوم بإرسال الطلبات
    tokens_file = "token.txt"

    try:
        with open(tokens_file, "r") as file:
            tokens = file.read().splitlines()  # قراءة جميع التوكنات
    except FileNotFoundError:
        print(f"File {tokens_file} not found.")
        return

    task_ids = [9, 7]  # قائمة الـ task IDs للتنفيذ

    for token in tokens:
        for task_id in task_ids:
            print(f"{Fore.YELLOW}Sending task token: {token}, task_id: {task_id}")
            # الانتظار 3 ثوانٍ لتجنب الحظر
            await asyncio.sleep(6)
            result = send_task_request(token, task_id)
            re = start_airdrop_mining(token)
            auto = send_claim_request(token)

            if result:
                print(f"{Fore.GREEN}Response for token: {token}, task_id: {task_id}: Done")
            else:
                print(f"{Fore.RED}Failed to process token: {token}, task_id: {task_id}")
            if re:
            	print(f"Auto Miner: {re} Done")
            else:
            	print(f"Failed to process token: {token}")
            if auto:            	
            	print(f"{Fore.RED} Start claming in 24 hours wtting...")
            	
            	print(f"Auto Claim:  {auto}")
            
            	
            	

# تشغيل البرنامج
asyncio.run(main())