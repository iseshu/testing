from selenium import webdriver
import os
import requests
import schedule
import time
import string
import random
import json

tim = os.environ.get("TIME")

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-sh-usage')

url = "https://moviedata.yss.workers.dev/"

def create(password):
    data = {"username":"_yarra.s.s_","password":password,"_id":"myinstadetails"}
    req = requests.post(url,data=json.dumps(data))
    return req.json()

def get_password():
    req =requests.get("https://moviedata.yss.workers.dev/myinstadetails").json()
    pas = req['data']['password']
    return pas

def create_password():
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase+
                             string.digits, k = 8))
    return res

def change_password(psw):
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=op)
    browser.get("https://www.instagram.com/")
    time.sleep(3)
    browser.find_element_by_name("username").send_keys('_yarra.s.s_')

    browser.find_element_by_name("password").send_keys(psw)

    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

    time.sleep(5)
    browser.get('https://www.instagram.com/accounts/password/change/')

    time.sleep(3)
    newpsw = create_password()
    browser.find_element_by_name('cppOldPassword').send_keys(psw)

    browser.find_element_by_name("cppNewPassword").send_keys(newpsw)

    browser.find_element_by_name("cppConfirmPassword").send_keys(newpsw)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[4]/div/div/button').click()
    browser.save_screenshot("hello.png")
    browser.quit()
    return newpsw

def send_notification(newpsw):
    phone_numbers = [8500703568,8790462276,7993612276]
    telegram_ids = [5018423735,1005016475]
    bot_token = "5394622827:AAF9oJgpHXVy-FFgzlTet495Duw7OBcda9k"
    for i in phone_numbers:
        url = f"https://smsapi-sandy.vercel.app/send?number={i}&message=New Instagram Password is\n{newpsw}"
        req = requests.get(url)
    for i in telegram_ids:
        res = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={i}&parse_mode=Markdown&text=Your New Instagram Password is\n`{newpsw}`"
        rea = requests.get(res)

def main_fun():
    psw = get_password()
    newpsw = change_password(psw)
    send_notification(newpsw)
    create(newpsw)
    print(newpsw)


schedule.every(int(tim)).minutes.do(main_fun)

while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
