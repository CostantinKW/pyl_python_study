"""
    这段代码功能上依次实现：打开百度首页，自动输入"python"关键字并查询，页面展示30秒，最后关闭浏览器窗口
"""
from selenium import webdriver
import time

browser = webdriver.Chrome()
# 打开浏览器
browser.get('http://www.baidu.com/')
# 定位到搜索框
element = browser.find_element_by_id("kw")
# 在搜索框内输入 "python"
element.send_keys("python")
# 相当于回车，即点击确认
element.submit()
# 页面展示30秒
time.sleep(30)
# 关闭浏览器
browser.quit()