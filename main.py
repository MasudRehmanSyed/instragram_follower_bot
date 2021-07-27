import pandas as pd, openpyxl, time
from instafollower import Instafollower

def get_login():
    df = pd.read_excel("C:/Users/rawni/Documents/API_KEYS.xlsx", engine="openpyxl")
    insta_uname = df[df.API_SITE=='instagram'].email.to_string(index=False)
    insta_passw = df[df.API_SITE=='instagram'].password.to_string(index=False)
#     print(insta_passw, insta_uname)
    return insta_passw, insta_uname

passw, username = get_login()

insta = Instafollower()

insta.login(uname=username, passw=passw)
time.sleep(2)
insta.kill_pop_up()
time.sleep(3)
insta.find_followers()
time.sleep(2)
insta.follow()
insta.quit_web()