from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import requests


class LineMessage():
    # 修改為你的權杖內容
    # uy2qUyM7OArOVcKDcsxxi0UWNHaWrwohemSxNZ7wzZ2
    token = 'iqcgy1bz7ds4OqWj1yJqPbTK7ROFNl7JGVKGo6RQOfe'
    def __init__(self,token):
        self.token = token
        pass
    def lineNotifyMessage(self, msg):
        headers = {
            "Authorization": "Bearer " + self.token, 
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        
        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code
    pass

driver = webdriver.Chrome()
driver.get("https://sso.nutc.edu.tw/ePortal/Default.aspx")

account = driver.find_element_by_id("ContentPlaceHolder1_Account")
pwd = driver.find_element_by_id("ContentPlaceHolder1_Password")

account.send_keys("s1110602025")
pwd.send_keys("yf20020704")

code = input("code:")
verify = driver.find_element_by_id("ContentPlaceHolder1_ValidationCode")
verify.send_keys(code)
verify.send_keys(Keys.RETURN)

ok = bool(input())
if ok:
    driver.get("https://ais.nutc.edu.tw/student/selection/pre_selection.aspx")
    newsLineMsg = LineMessage('uy2qUyM7OArOVcKDcsxxi0UWNHaWrwohemSxNZ7wzZ2')
    while True:
        try:
            driver.refresh()
            driver.execute_script("$('.ares-icon-googleplus').click()")
            subject = driver.find_element_by_id("subject")
            time.sleep(0.05)
            subject.send_keys("個體經濟學")
            subject.send_keys(Keys.RETURN)
            stu_num = driver.find_element_by_id("course_tab")
            results = stu_num.text.split()
            a,b = int(results[20]),int(results[34])
            print(datetime.now(),a,b)
            if a < 60 | b < 60:
                newsLineMsg.lineNotifyMessage(f"{a} , {b}")
        except:
            print(datetime.now(),"keep running")
            continue