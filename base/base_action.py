from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self,loc):
        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc, timeout=5.0, poll=1.0):
        by = loc[0]
        value = loc[1]
        # 如果是Xpath的方式，就调用Xpath的处理方法
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)
        # 增加显示等待
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(by, value))

    def find_elements(self, loc, timeout=5.0, poll=1.0):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = self.make_xpath_with_feature(value)

        # 增加显示等待
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_elements(by, value))


    def make_xpath_with_unit_feature(self, loc):
        """
        只处理xpath中间部分的方法，需要被def make_xpath_with_feature(loc)方法调用
        即//*[contains(@text,'设置')]除去 //*[] 剩余的部分
        :param loc: 传入的字符串
        :return: 返回拼接好的字符串
        """
        key_index = 0
        value_index = 1
        option_index = 2
        args = loc.split(",")
        if len(args) == 2:
            loc = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        elif len(args) == 3:
            if args[option_index] == "1":
                loc = "@" + args[key_index] + " = '" + args[value_index] + "'" + "and "
            elif args[option_index] == "0":
                loc = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + "and "
        return loc

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""

        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            # 传入的是单个字符串
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # 此时loc是列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)

        feature = feature.rstrip("and ")
        loc = feature_start + feature + feature_end
        return loc

    # 获取toast全部内容
    def find_toast(self, message,is_screenshot=False, screenshot_file_name=None, timeout=3, poll=0.1):
        message = "//*[contains(@text,'" + message + "')]"
        ele = self.find_element((By.XPATH, message), timeout, poll)
        if is_screenshot:
            self.screenshot(screenshot_file_name)
        print(ele.text)
        return ele.text

    # 判断toast是否存在，调用find_toast
    def is_toast_exsit(self, message, is_screenshot=False, screenshot_file_name=None):
        try:
            self.find_toast(message,is_screenshot, screenshot_file_name)
            return True
        except Exception:
            return False

    # 截图方法
    def screenshot(self,screen_file_name):
        self.driver.get_screenshot_as_file("./screen/" + screen_file_name + ".png")

