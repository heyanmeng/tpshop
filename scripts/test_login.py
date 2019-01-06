import os,sys

import allure
import pytest

sys.path.append(os.getcwd())
from page.page_login import PageLogin
from base.base_driver import init_driver
from base.base_yml import yml_data_with_filename_and_key


def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page_login = PageLogin(self.driver)

    # @pytest.mark.parametrize(("username", "password", "toast"), data_with_key("test_login"))
    # def test_login(self, username, password, toast):
    #     # 输入账号
    #     self.page_login.input_username(username)
    #     # 输入密码
    #     self.page_login.input_password(password)
    #     # 点击登录
    #     self.page_login.click_login()
    #     # 判断是否登录成功
    #     assert self.page_login.is_toast_exsit(toast)

    @allure.step(title = "登录功能测试")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        screenshot_name = args["screenshot_name"]
        # 输入账号
        allure.attach('输入账号:' + username,'')
        self.page_login.input_username(username)
        # 输入密码
        allure.attach('输入密码:' + password, '')
        self.page_login.input_password(password)
        # 点击登录
        allure.attach('点击登录按钮', '')
        self.page_login.click_login()
        # 判断是否登录成功并截图
        allure.attach('判断是否存在对应的toast:' + toast, '')
        ast = self.page_login.is_toast_exsit(toast, True, screenshot_name)
        # 上传截图到allure报告
        allure.attach('截图', open('./screen/' + screenshot_name + '.png','rb').read(), allure.attach_type.PNG)
        assert ast
