# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 任选语言完成测试脚本，实现淘宝网站登录、商品搜索，下单，付款的购物全流程接口自动化（仅按流程编写，无需调试）
browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")
# 1、登录
# browser.find_element_by_partial_link_text("亲，请登录").click()
# browser.find_element_by_partial_link_text("会员名/邮箱/手机号").send_keys('zhanghao')
# time.sleep(3)
# browser.find_element_by_partial_link_text("请输入登录密码").send_keys('mima')
# time.sleep(3)
# 2、商品搜索
element1 = browser.find_element_by_id("q")
element1.click()
element1.clear()
element1.send_keys("医用口罩")
search_button_element = browser.find_element_by_xpath("//button[@class='btn-search tb-bg']")
search_button_element.click()


