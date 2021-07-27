from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        # self.driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()


    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps')
        self.driver.implicitly_wait(3)
        follow_button = self.driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]')
        follow_button.click()

    def follow(self):
        pass


    def quit_web(self):
        self.driver.quit()