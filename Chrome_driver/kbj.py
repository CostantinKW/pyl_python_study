"""
    本代码在功能上实现对kbj嘉慧环境登录操作
"""

from selenium import webdriver
import time

# 设置使用的浏览器为chrome浏览器
browser = webdriver.Chrome()
# 打开对应的网址
browser.get('http://kthrp.karrytech.com:1603')
# 选定数据库 "jiahui-0126"
element = browser.find_element_by_partial_link_text('jiahui-0126')
# 相当于点击动作
element.click()

# 此时已进入登陆页面

# 选中 用户名 输入框
user_name = browser.find_element_by_id('login')
# 清空 用户名 输入框
user_name.clear()
# 在 用户名 输入框输入 "admin"
user_name.send_keys('admin')

# 选中 密码 输入框
pass_word = browser.find_element_by_id('password')
# 清空 密码 输入款
pass_word.clear()
# 在 密码 输入框输入 1
pass_word.send_keys(1)
# 在 密码 输入款 模拟回车动作，实现登录
pass_word.submit()

"""
# 这段代码没有生效，登录的步骤利用在密码输入款输入 "回车" 来提代
# 选中 登录  按钮
login_button = browser.find_element_by_partial_link_text("登录")
# 模拟点击  登录 按钮的动作
login_button.click()
"""

"""
    具体的功能代码可在本段注释与 time.sleep(60)语句之间加入
"""
# 等待15秒，使页面刷新出来
time.sleep(30)
# 菜单 按钮
menu_button = browser.find_element_by_partial_link_text('Toggle App Drawer')
menu_button.click()
time.sleep(10)
# 人力资源 按钮
hr_button = browser.find_element_by_partial_link_text('人力资源')
hr_button.click()
# 此时已进入 人力资源 页面
# 人力资源页面的 设置 按钮
hr_setting_button = browser.find_element_by_partial_link_text('配置')
hr_setting_button.click()
time.sleep(3)
# 人力资源-设置-部门组织， 部门组织按钮
department_button = browser.find_element_by_partial_link_text('部门组织')
department_button.click()
time.sleep(3)
"""
    此时浏览器已经打开了 “部门组织” 菜单项的tree视图界面，但是 人力资源-配置 按钮点开的菜单下拉框还未收起，
    需要将菜单下拉框收起，使浏览器能正确获取tree视图的行信息.(可以理解为 配置 按钮点开的菜单下拉框覆盖了trees视图的窗口，为了消除
    覆盖的影响，需要将下拉框收起.)
    这里我解决这个问题的思路是精确定位到tree视图某一行的某一列上面进行点击动作，selenium查找元素的时候也是根据坐标查找.
"""

# 选中form视图的某一行记录
# 元素定位到部门组织tree视图的第一行(行id是2826)的第一列
record = browser.find_element_by_xpath("//tr[@data-id='2826']/td[@data-field='organization']")
record.click()

# 此时浏览器打开了部门组织tree视图第一条记录的form视图

# 展示页面 60 秒
time.sleep(60)
# 退出浏览器
browser.quit()