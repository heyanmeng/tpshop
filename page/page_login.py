import os,sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction

mine_button = By.XPATH, "text,我的"
login_button = By.ID, "com.tpshop.malls:id/head_mimgv"
input_username = By.XPATH, "text,请输入账号"
input_password = By.ID, "com.tpshop.malls:id/pwd_et"
click_login_button = By.ID, "com.tpshop.malls:id/login_tv"


class PageLogin(BaseAction):
    def __init__(self,driver):
        super().__init__(driver)
        self.click_mine()
        self.click_button()

    def click_mine(self):
        self.click(mine_button)

    def click_button(self):
        self.click(login_button)

    def input_username(self,username):
        self.input_text(input_username,username)

    def input_password(self,password):
        self.input_text(input_password,password)

    def click_login(self):
        self.click(click_login_button)

    # def is_login(self, username):
    #     try:
    #         self.find_element((By.XPATH,"text," + username))
    #         return True
    #     except Exception:
    #         return False

