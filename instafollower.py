from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SITE= 'https://www.instagram.com/accounts/login/'

class Instafollower:

    def __init__(self):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(SITE)

    def login(self, uname, passw):

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name('username').send_keys(uname)
        self.driver.find_element_by_name('password').send_keys(passw)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
        time.sleep(3)


    def kill_pop_up(self):
        self.driver.find_element_by_css_selector('.mt3GC .HoLwm').click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps')
        self.driver.implicitly_wait(3)
        follow_button = self.driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]')
        follow_button.click()

    def follow(self):
        ''' Gets the pop up and selects the div with all the names and runs a javascript to
        select all the follow'''
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(0, 10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def quit_web(self):
        self.driver.quit()