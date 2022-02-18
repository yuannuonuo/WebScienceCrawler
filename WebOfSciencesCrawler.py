# author: 袁钺&庞娜
# date: 2022-02-18
# 山穷水复疑无路，柳暗花明又一村

from selenium import webdriver
from time import sleep

totalDocumentNumber=32835 #预先指定

mode="完整记录"# 完整记录/全记录与引用的参考文献
if mode=="完整记录":
    maxNumber = 1000
elif mode=="全记录与引用的参考文献":
    maxNumber = 500
downloadBatchNum=(totalDocumentNumber//maxNumber)+1

browser = webdriver.Chrome()
for currentBatch in range(downloadBatchNum):
    #导出不同的batch时，每次都再刷新一下
    browser.get("https://www.webofscience.com/wos/woscc/summary/db97acb7-8ffe-4d85-8725-6b8b41dc656d-24258777/relevance/1(overlay:export/ext)")
    sleep(15)
    #关闭一些弹框
    if currentBatch==0:
        closeButtonElements_1=browser.find_elements_by_xpath("//button[@class='_pendo-close-guide']")
        closeButtonElements_1[0].click()
        sleep(1)
    #确定每次导出时，起始与终止记录数值
    startNum = currentBatch * maxNumber + 1
    if currentBatch!=downloadBatchNum-1:
        EndNum=(currentBatch+1)*maxNumber
    else:
        EndNum = totalDocumentNumber
    #点选：选择记录选项
    labelElements=browser.find_elements_by_xpath("//label[@for='radio3-input']")
    labelElements[0].click()
    #确定起始记录
    inputElements_1=browser.find_elements_by_xpath("//input[@type='text']")
    inputElements_1[0].clear()
    inputElements_1[0].send_keys(str(startNum))
    #确定终止记录
    inputElements_2=browser.find_elements_by_xpath("//input[@type='text']")
    inputElements_2[1].clear()
    inputElements_2[1].send_keys(str(EndNum))
    #点击记录内容下拉框
    dropdownElements = browser.find_elements_by_xpath("//button[@class='dropdown']")
    dropdownElements[0].click()
    fullRecordsElements = browser.find_elements_by_xpath("//div[@title='"+mode+"']")##WOS最易修改之处
    fullRecordsElements[0].click()
    #点击导出
    exportElements=browser.find_elements_by_xpath("//button[@class='mat-focus-indicator cdx-but-md mat-stroked-button mat-button-base mat-primary']")
    exportElements[0].click()
    print("Downloading records:"+str(startNum)+"~"+str(EndNum)+"!")
    #注意间隔时间要足够长，不然容易出现问题
    sleep(25)


