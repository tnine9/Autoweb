import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 动作链
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 调用谷歌浏览器
driver.maximize_window()  # 最大化浏览器界面
driver.implicitly_wait(10)  # 等待网页加载10秒

# 京东界面
# driver.get('https://www.jd.com/')  # 进入京东首页
# driver.find_element(By.XPATH, '//*[@id="key"]').send_keys('星之卡比')  # 在搜索框输入
# driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()  # 单击搜索按钮
# driver.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[4]/div').click()  # 单击进入商品详情
#
# data = driver.window_handles  # 将所有窗口编组
# driver.switch_to.window(data[1])  # 切换到第二个窗口
#
# driver.find_elemen6By.XPATH, '//*[@id="InitCartUrl"]').click()  # 加入购物车

# 苏宁易购
# driver.get('https://www.suning.com/')  # 进入苏宁首页
# driver.find_element(By.XPATH, '//*[@id="searchKeywords"]').send_keys('星之卡比')  # 在搜索框输入
# driver.find_element(By.XPATH, '//*[@id="searchSubmit"]').click()  # 单击搜索按钮
# driver.find_element(By.XPATH, '//*[@id="0070879179-12339291331"]/div/div').click()  # 单击进入商品详情
#
# data = driver.window_handles  # 将所有窗口编组
# driver.switch_to.window(data[1])  # 切换到第二个窗口
#
# driver.find_element(By.XPATH, '//*[@id="J-TZM"]/dl[1]/dd/ul/li[3]/a').click()  # 选择商品种类
# driver.find_element(By.XPATH, '//*[@id="addCart"]').click()  # 加入购物车
# driver.find_element(By.XPATH, '/html/body/div[38]/div/div[2]/div/div[1]/a').click()  # 去购物车结算
# driver.find_element(By.XPATH, '//*[@id="cart-wrapper"]/div[3]/div/div/div[2]/div[2]/a').click()  # 点击结算

# 哔哩哔哩
driver.get('https://www.bilibili.com/')  # 进入哔哩哔哩首页
driver.find_element(By.XPATH,
                    '//*[@id="internationalHeader"]/div/div/div[3]/div[2]/span[1]/div/span/div').click()  # 点击登录

data = driver.window_handles  # 将所有窗口编组
driver.switch_to.window(data[1])  # 切换到第二个窗口

driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys('17332502091')  # 输入账号
driver.find_element(By.XPATH, '//*[@id="login-passwd"]').send_keys('yijiu19.')  # 输入密码
driver.find_element(By.XPATH, '//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()  # 点击确定
time.sleep(10)  # 等待十秒验证时间

driver.find_element(By.XPATH, '//*[@id="nav_searchform"]/input').send_keys('鬼灭之刃')  # 在搜索框输入
driver.find_element(By.XPATH, '//*[@id="nav_searchform"]/div').click()  # 单击搜索按钮

data = driver.window_handles  # 将所有窗口编号
driver.switch_to.window(data[2])  # 切换到第三个窗口

driver.find_element(By.XPATH, '//*[@id="all-list"]/div[1]/div[2]/ul[4]/li[2]/a/div/div[1]/img').click()  # 单击进入视频播放界面

data = driver.window_handles  # 将所有窗口编号
driver.switch_to.window(data[3])  # 切换到第四个窗口
time.sleep(5)
ele = driver.find_element(By.XPATH, '//*[@id="arc_toolbar_report"]/div[1]/span[1]')  # 找到点赞键

ac = ActionChains(driver)  # 将driver页面对象交给ActionChains管理
ac.click_and_hold(ele).perform()  # 让ac对象做鼠标操作
time.sleep(5)  # 长按三秒

ac.release()  # 松开鼠标
