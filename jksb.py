import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get('https://jksb.v.zzu.edu.cn/')
    driver.switch_to.frame('my_toprr')                                                                #切换iframe
    time.sleep(3)
    driver.find_element(
        "xpath", "/html/body/form/div/div[2]/div[2]/div[3]/input").send_keys('你的学号')          # 找到账号框并输入账号
    print("成功输入用户名")
    driver.find_element(
        By.XPATH, "/html/body/form/div/div[2]/div[3]/div[3]/input").send_keys('你的密码')             # 找到密码框并输入密码
    print("成功输入密码")
    driver.find_element(
        By.XPATH, "/html/body/form/div/div[2]/div[5]/div/input").click()                              # 找到“进入健康上报平台”按钮并点击
    print("成功进入申报页面")
    time.sleep(3)
    driver.switch_to.frame("zzj_top_6s")                                                              #切换到“本人填报”按钮所在iframe
    driver.find_element(
        By.XPATH, "//html/body/form/div/div[13]/div[3]/div[4]").click()                               #点击本人填报
    print("开始今日填报")
    time.sleep(3)
    driver.find_element(
        By.XPATH, "/html/body/form/div/div[8]/div[2]/div[2]/div[2]/select[1]/option[2]").click()      #选择绿码
    print("成功选择绿码")
    driver.find_element(
        By.XPATH, "/html/body/form/div/div[8]/div[2]/div[2]/div[2]/div[6]/div[4]/span").click()       #提交表格
    print("成功提交表格")
except Exception as e:
    print("填报失败：{}".format(e))
    driver.close()