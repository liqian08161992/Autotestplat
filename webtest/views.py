from django.shortcuts import render

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from core import base

if __name__ == '__main__':

    """
    最简单的一个案例
    第一步打开浏览器
    第二步输入地址
    第三步输入内容
    第四步点击搜索
    
    
    第二个案例
    登陆华为云
    发布一个帖子
    
    
    现在的问题
    1，验证的问题----这个最大
    2，输出报告的问题
    3，记录bug的问题

    
    
    """

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Autotestplat.settings")
    import django

    django.setup()
    from webtest import models

    case_obj = models.WebCaseList.objects.filter(id=2).first()
    steps = case_obj.webcasestep2_set.order_by('order_num')
    print(steps)
    base.run2(steps)




