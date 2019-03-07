'''
    使用方法  
    1.pip3 install selenium

    2.安装chromedrive  https://blog.csdn.net/qq_40604853/article/details/81388078

    3. python3 serach.py

    只是查看通知公告 的第一个 的标题是否与 defualt 的内容一样 而已。
    小黑框拉长点 方便看
'''
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import Select


flag =[0 ,0, 0, 0, 0, 1, 0, 0, 0,1, 0,0 ,0, 0,0]
name  = ["计算机学",
        "宇航学院",
        "数理学院",
        "机电学院",
        "物理学院",
        "机械学院",
        "经管学院",
        "光电学院",
        "信息电子",
        "自动化学",
        "法学学院",
        "化工学院",
        "外国语院"
]
xpath =[
        "/html/body/div/div[2]/div[2]/div[1]/ul/li[1]/a",
        "/html/body/div[2]/div[4]/div[2]/div[2]/ul/li[1]/a",
        "/html/body/div[2]/div[1]/div[2]/ul/li[1]/a",
        "/html/body/div[2]/div[3]/div/div[2]/ul/li[1]/a",
        "/html/body/div[2]/div[2]/div[2]/div[1]/ul/li[1]/a",
        "/html/body/div[3]/div[2]/div[1]/ul/li[1]/a",
        "/html/body/section[2]/div[2]/div[2]/ul/li[1]/a",
        "//*[@id=\"main\"]/div[2]/ul/li[1]/a",
        "/html/body/div/div[2]/div[3]/div[2]/ul/li[1]/a",
        "/html/body/div[2]/div[2]/div[1]/ul/li[1]/a",
        "/html/body/div[2]/div[4]/div/div[1]/ul/li[1]/a",
        "/html/body/div/div[2]/div[2]/div/div[2]/ul/li[1]/a",
        "//*[@id=\"content\"]/div/div[2]/ul/li[1]/a"

]
defualt =[  "关于做好2018年度团员基本信息采集统计和团费收缴工作的通知",
            "关于评选宇航学院红箭奖学金、11791奖学金、13781奖励金、03821奖学金、1678...",
            "数学与统计学院本学期课程任课教师答疑安排",
            "关于开展机电学院第八届“机电先锋”评选工作的通知",
            "关于开展北京理工大学2018年度工信创新创业奖学金评选的通知",
            "机械与车辆学院2019年硕士研究生入学考试复试通知",
            "管理与经济学院拟接收2017级、2018级本科生转专业名单公示",
            "关于开展北京理工大学第十六届“世纪杯”竞赛的通知",
            "英国中央兰开夏大学2019年暑期项目报名通知",
            "2019年自动化学院硕士研究生入学考试复试办法",
            "2018-2019 Second Semester, Internat...",
            "关于推荐青春榜样至学校青春榜样库的公示",
            "北京理工大学外国语学院优秀青年骨干教师招聘公告"
]
url =[  "http://cs.bit.edu.cn/tzgg/index.htm",
        "http://sae.bit.edu.cn/tzgg/index.htm",
        "http://math.bit.edu.cn/tzgg/index.htm",
        "http://smen.bit.edu.cn/tzgg1/index.htm",
        "http://physics.bit.edu.cn/sytzgg/index.htm",
        "http://me.bit.edu.cn/tzgg/index.htm",
        "http://sme.bit.edu.cn/gbxwzx/tzgg/index.htm",
        "http://opt.bit.edu.cn/tzgg/index.htm",
        "http://sie.bit.edu.cn/tzgg/zhtz/index.htm",
        "http://ac.bit.edu.cn/tzgg/index.htm",
        "http://law.bit.edu.cn/tzgg/xsbd/index.htm",
        "http://cce.bit.edu.cn/tzgg/index.htm",
        "http://sfl.bit.edu.cn/tzgg/index.htm"
]
def printf(*args):
    print(*args, end='')

def printfChart():
    for i in range(len(name)):
        printf (name[i])
        printf("|")
    print("\n")
    for i in range(len(name)):
        printf("  ")
        if flag[i]==1:
            printf("√")
        else:
            printf("x")
        printf("     |")
    print("\n")
    print("当前已经出了的有:")
    for i in range(len(name)):
        if(flag[i]==1):
            printf (name[i])
            printf(" | ")
    print("\n")

def Func():
    Browser=webdriver.Chrome()
    while 1:
        printfChart()#打印表头
        for i in range(len(name)):
            if flag[i] == 0:
                defualtname = defualt[i]
                Browser.get(url[i])
                time.sleep(2)#延时
                get=Browser.find_element_by_xpath(xpath[i])
                print("学院：%s 标题：%s"%(name[i],get.text))
                if get.text == defualtname:
                    flag[i]=0
                else:
                    print("当前学院: %s 查到已经更新!"%(name[i]))
                    flag[i]=1
                    Browser.get("https://www.douyu.com/3870925")#打开视频直播 就能听到声音 提醒更新了
                    time.sleep(10)

Func()
