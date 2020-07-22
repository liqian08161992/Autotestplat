from selenium import webdriver
from time import sleep


def open_brower():
    # 实例化浏览器
    global driver
    chrome_driver_path = '../tools/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)  # Windows下执行
    driver.maximize_window()


def open_url(url):
    driver.get(url)


def setup_login():
    # 实例化浏览器
    global driver
    chrome_driver_path = '../tools/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)  # Windows下执行
    driver.maximize_window()
    driver.get("https://bbs.huaweicloud.com/forum/forum-672-1.html")
    driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div[1]/div[1]/div/div/ul/li[8]/a').click()
    driver.find_element_by_xpath('//*[@type="text"]').send_keys()
    driver.find_element_by_xpath('//*[@type="password"]').send_keys()
    driver.find_element_by_id("btn_submit").click()


def send_keys(method, value, data):
    if method == 1:  # id
        driver.find_element_by_id(value).send_keys(data)
    if method == 2:  # xpath
        sleep(2)
        driver.find_element_by_xpath(value).send_keys(data)
    if method == 4:  # css
        print(driver.find_element_by_css_selector(value))
        driver.find_element_by_css_selector(value).send_keys(data)
    if method == 7:  # tag_name
        driver.find_element_by_tag_name(value).send_keys(data)


def click(method, value):
    if method == 1:  # id
        driver.find_element_by_id(value).click()
    if method == 2:  # xpath
        driver.find_element_by_xpath(value).click()
    if method == 3:  # link_text
        driver.find_element_by_link_text(value).click()
    if method == 5:  # class_name
        driver.find_element_by_class_name(value).click()


import unittest


class Assert(unittest.TestCase):
    def assert_text(self, method, value, test_data, assert_data):
        if test_data == "发帖":
            if method == 2:  # xpath
                try:
                    actual_data = driver.find_element_by_xpath(value).text
                    self.assertEqual(actual_data, assert_data)
                    print("断言成功")
                except Exception as e:
                    print(e)
                    print("断言失败")
        if test_data == "回帖":
            if method == 2:  # xpath
                try:
                    print(driver.find_elements_by_xpath(value)[1])
                    actual_data = driver.find_elements_by_xpath(value)[1].text
                    self.assertEqual(actual_data, assert_data)
                    print("断言成功")
                except Exception as e:
                    print(e)
                    print("断言失败")


def new_windos():  # 跳转新窗口
    hanldes = driver.window_handles
    [driver.switch_to.window(i) for i in hanldes]


def switch_frame(method, value):
    if method == 6:  # name
        driver.switch_to.frame(value)
    if method == 2:  # xpath
        print("进入switch_frame方法")
        sleep(3)
        ele = driver.find_element_by_xpath(value)
        print(ele)
        driver.switch_to.frame(ele)
        print("切换到frame成功")


def run(steps):
    for step in steps:
        operate_method = step.operate_method
        print(operate_method, step.test_step_name)
        if operate_method == 1:  # 1是打开浏览器
            open_brower()
        if operate_method == 2:  # 2是打开url
            url = step.test_data
            open_url(url)
        if operate_method == 3:  # 3是输入内容
            locate_method = step.locate_method
            ele_vaule = step.element_value
            test_data = step.test_data
            print(ele_vaule, test_data)
            send_keys(locate_method, ele_vaule, test_data)
        if operate_method == 4:  # 4是点击
            locate_method = step.locate_method
            ele_vaule = step.element_value
            print(locate_method, ele_vaule)
            sleep(2)
            click(locate_method, ele_vaule)
        if operate_method == 5:  # 切换到新的窗口
            new_windos()
            print("切换到新的窗口")
        if operate_method == 6:  # 处理弹框
            tq = driver.find_element_by_xpath('//*[@class="popText"]/p').text  # 草稿提示
            if tq == '您有未发表的帖子':
                driver.find_element_by_class_name('cancel').click()
            else:
                pass
        if operate_method == 7:  # 跳入frame
            locate_method = step.locate_method
            ele_vaule = step.element_value
            print(77777777777777, locate_method, ele_vaule)
            switch_frame(locate_method, ele_vaule)
        if operate_method == 8:  # 跳出frame
            sleep(2)
            driver.switch_to.default_content()
        if operate_method == 9:  # 进行断言
            locate_method = step.locate_method
            ele_vaule = step.element_value
            assert_data = step.assert_data
            test_data = step.test_data
            A = Assert()
            A.assert_text(locate_method, ele_vaule, test_data, assert_data)
        if operate_method == 10:  # 刷新页面
            driver.refresh()
        if operate_method == 11:  # 睡眠
            test_data = step.test_data
            sleep(int(test_data))
        if operate_method == 12:  # 登陆操作
            setup_login()


def run2(steps):
    for step in steps:
        operate_method = step.operate_method
        print(operate_method, step.test_step_name)
        if operate_method == 1:  # 1是打开浏览器
            open_brower()
        if operate_method == 2:  # 2是打开url
            url = step.test_data
            open_url(url)
        if operate_method == 3:  # 3是输入内容
            locate_method = step.element_name.locate_method
            ele_vaule = step.element_name.element_value
            test_data = step.test_data
            print(type(step.element_name))
            print(locate_method, ele_vaule, test_data)
            send_keys(locate_method, ele_vaule, test_data)
        if operate_method == 4:  # 4是点击
            locate_method = step.element_name.locate_method
            ele_vaule = step.element_name.element_value
            print(locate_method, ele_vaule)
            sleep(2)
            click(locate_method, ele_vaule)
        if operate_method == 5:  # 切换到新的窗口
            new_windos()
            print("切换到新的窗口")
        if operate_method == 6:  # 处理弹框
            tq = driver.find_element_by_xpath('//*[@class="popText"]/p').text  # 草稿提示
            if tq == '您有未发表的帖子':
                driver.find_element_by_class_name('cancel').click()
            else:
                pass
        if operate_method == 7:  # 跳入frame
            locate_method = step.locate_method
            ele_vaule = step.element_value
            print(77777777777777, locate_method, ele_vaule)
            switch_frame(locate_method, ele_vaule)
        if operate_method == 8:  # 跳出frame
            sleep(2)
            driver.switch_to.default_content()
        if operate_method == 9:  # 进行断言
            locate_method = step.locate_method
            ele_vaule = step.element_value
            assert_data = step.assert_data
            test_data = step.test_data
            A = Assert()
            A.assert_text(locate_method, ele_vaule, test_data, assert_data)
        if operate_method == 10:  # 刷新页面
            driver.refresh()
        if operate_method == 11:  # 睡眠
            test_data = step.test_data
            sleep(int(test_data))
        if operate_method == 12:  # 登陆操作
            import os
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Autotestplat.settings")
            import django

            django.setup()
            from webtest import models

            case_obj = models.WebCaseList.objects.filter(id=5).first()
            steps = case_obj.webcasestep2_set.order_by('order_num')
            print(steps)
            run2(steps)


