import tkinter.messagebox
import webbrowser
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import gui2
import tkinter.messagebox
import pandas
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib import font_manager
import tkinter as tk
import re
import time
import threading
import sys
import tkinter


class myStdout():  # 重定向类
    def __init__(self):
        # 将其备份
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
        # 重定向
        sys.stdout = self
        sys.stderr = self

    @staticmethod
    def write(info):  # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
        t1.insert('end', info)  # 在多行文本控件最后一行插入print信息
        t1.update()  # 更新显示的文本，不加这句插入的信息无法显示
        t1.see(tkinter.END)  # 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行

    def restoreStd(self):  # 恢复标准输出
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak


mystd = myStdout()  # 实例化重定向类

root1 = tk.Tk()  # 创建窗口对象
root1.title('主页面')
root1.geometry('600x500')

# https://www.bilibili.com/v/popular/rank/bangumi
url = tk.StringVar()
lock = threading.Lock()
global img_png           # 定义全局变量 图像
global dm_name
global dm_play
global dm_review
global dm_favorite
global dm_com_score


def chazhao():
    if not re.match("^(http://|https://)?((?:[A-Za-z0-9]+-[A-Za-z0-9]+|"
                    "[A-Za-z0-9]+)\.)+([A-Za-z]+)[/?:]?.*$", e1.get()):
        tkinter.messagebox.askokcancel(title='检查url合法性', message='url非法，请重新输入！')
        e1.delete(0, "end")
        print("url非法，请重新输入！")
    else:
        print("url合法，请继续下一步操作！")
        r = requests.get(url.get())
        if r.status_code==200:
            webbrowser.open(url.get())
        else:
            print("状态码：", r.status_code)
        # tkinter.messagebox.askokcancel(title='检查url合法性', message='url合法！')




e1 = tk.Entry(root1, textvariable=url, show=None, )  # 输入框
e1.place(x=100, y=20, width=400, height=30)

t1 = tk.Text(root1, bg="grey", font=("Arial", 12))  # 创建多行文本控件
t1.place(x=100, y=100, width=400, height=50)  # 布局在窗体上

l2 =tk.Label(root1, bg="grey", font=("Arial", 12))  # 显示框
l2.place(x=100, y=160, width=400, height=300)

def view1():
    global img_png
    photo = Image.open("1.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view1_1():
    global img_png
    photo = Image.open("1条形图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view1_2():
    global img_png
    photo = Image.open("1折线图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view2():
    global img_png
    photo = Image.open("2.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view2_1():
    global img_png
    photo = Image.open("2条形图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view2_2():
    global img_png
    photo = Image.open("2折线图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view3():
    global img_png
    photo = Image.open("3.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view3_1():
    global img_png
    photo = Image.open("3条形图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view3_2():
    global img_png
    photo = Image.open("3折线图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view4():
    global img_png
    photo = Image.open("4.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view4_1():
    global img_png
    photo = Image.open("4条形图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)

def view4_2():
    global img_png
    photo = Image.open("4折线图.png")  # 括号里为需要显示在图形化界面里的图片
    photo = photo.resize((400, 300))  # 规定图片大小
    img_png = ImageTk.PhotoImage(photo)
    img1 = ttk.Label(text="照片:", image=img_png)
    img1.place(x=100, y=160, width=400, height=300)


# 图1
cmb1 = ttk.Combobox(root1)  # 创建下拉菜单
cmb1.place(x=20, y=225, width=60, height=20)
cmb1['value'] = ('条形图', '折线图', '饼图', '组合图', '图1')  # 设置下拉菜单中的值 ,设置默认值，即默认下拉框中的内容
cmb1["state"] = "readonly"
cmb1.current(4)  # 默认值中的内容为索引，从0开始

def func(event):
    if cmb1.get() == "条形图":
        view1_1()
    elif cmb1.get() == "折线图":
        view1_2()
    elif cmb1.get() == "饼图":
        view1_2()
    elif cmb1.get() == "组合图":
        view1_2()
    elif cmb1.get() == "图1":
        view1()

cmb1.bind("<<ComboboxSelected>>", func)


# 图2
cmb2 = ttk.Combobox(root1)  # 创建下拉菜单
cmb2.place(x=20, y=270, width=60, height=20)

cmb2['value'] = ('条形图', '折线图', '饼图', '组合图', '图2')  # 设置下拉菜单中的值 ,设置默认值，即默认下拉框中的内容
cmb2["state"] = "readonly"
cmb2.current(4)  # 默认值中的内容为索引，从0开始

def func(event):
    if cmb2.get() == "条形图":
        view2_1()
    elif cmb2.get() == "折线图":
        view2_2()
    elif cmb2.get() == "饼图":
        view2_2()
    elif cmb2.get() == "组合图":
        view2_2()
    elif cmb2.get() == "图2":
        view2()

cmb2.bind("<<ComboboxSelected>>", func)


# 图3
cmb3 = ttk.Combobox(root1)  # 创建下拉菜单
cmb3.place(x=20, y=315, width=60, height=20)

cmb3['value'] = ('条形图', '折线图', '饼图', '组合图', '图3')  # 设置下拉菜单中的值 ,设置默认值，即默认下拉框中的内容
cmb3["state"] = "readonly"
cmb3.current(4)  # 默认值中的内容为索引，从0开始

def func(event):
    if cmb3.get() == "条形图":
        view3_1()
    elif cmb3.get() == "折线图":
        view3_2()
    elif cmb3.get() == "饼图":
        view3_2()
    elif cmb3.get() == "组合图":
        view3_2()
    elif cmb3.get() == "图3":
        view3()

cmb3.bind("<<ComboboxSelected>>", func)


# 图4
cmb4 = ttk.Combobox(root1)  # 创建下拉菜单
cmb4.place(x=20, y=360, width=60, height=20)

cmb4['value'] = ('条形图', '折线图', '饼图', '组合图', '图4')  # 设置下拉菜单中的值 ,设置默认值，即默认下拉框中的内容
cmb4["state"] = "readonly"
cmb4.current(4)  # 默认值中的内容为索引，从0开始

def func(event):
    if cmb4.get() == "条形图":
        view4_1()
    elif cmb4.get() == "折线图":
        view4_2()
    elif cmb4.get() == "饼图":
        view4_2()
    elif cmb4.get() == "组合图":
        view4_2()
    elif cmb4.get() == "图4":
        view4()

cmb4.bind("<<ComboboxSelected>>", func)


def reset():  # 重置
    url.set('')

def xianshi():
    url.set('https://www.bilibili.com/v/popular/rank/bangumi')
    print(url.get())

def gethtml():
    if url.get()=='':
        print(tkinter.messagebox.askokcancel(title='检查url合法性', message='url不能为空，请输入！'))
        return False
    else:
        try:
            r = requests.get(url.get())  # 使用get来获取网页数据
            r.raise_for_status()  # 如果返回参数不为200，抛出异常
            r.encoding = r.apparent_encoding  # 获取网页编码方式
            print("获取页面数据成功！")
            return r.text  # 返回获取的内容
        except:
            return False


def save():  # 解析网页
    html=gethtml()
    soup = BeautifulSoup(html, 'html.parser')  # 指定Beautiful的解析器为“html.parser”
    with open('1.txt', 'r+', encoding='UTF-8') as f:
        f.write(soup.text)

    # 定义好相关列表准备存储相关信息
    name = []  # 动漫名字
    bfl = []  # 播放量
    pls = []  # 评论数
    scs = []  # 收藏数
    TScore = []  # 综合评分

    # 动漫名字存储
    for i in soup.find_all('div', class_='info'):
        # print(i)
        bf = i.a.string
        name.append(str(bf))
    # print(name)

    # 播放量存储
    for i in soup.find_all('div', class_='detail'):
        bf = i.find('span', class_='data-box').get_text()
        if '亿' in bf:
            num = float(re.search(r'\d(.\d)?', bf).group()) * 10000
            bf = num
        else:
            bf = re.search(r'\d*(\.)?\d', bf).group()
        bfl.append(float(bf))
    # print(bfl)

    # 评论数存储
    for i in soup.find_all('div', class_='detail'):
        pl = i.find('span', class_='data-box').next_sibling.next_sibling.get_text()
        if '万' not in pl:
            pl = '%.1f' % (float(pl) / 10000)
        else:
            pl = re.search(r'\d*(\.)?\d', pl).group()
        pls.append(float(pl))
    # print(pls)

    # 收藏数
    for i in soup.find_all('div', class_='detail'):
        sc = i.find('span', class_='data-box').next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        sc = re.search(r'\d*(\.)?\d', sc).group()
        scs.append(float(sc))
    # print(scs)

    #  综合评分
    for i in soup.find_all('div', class_='pts'):
        zh = i.find('div').get_text()
        TScore.append(int(zh))
    # print('综合评分', TScore)

    # 存储至excel表格中
    info1 = {'动漫名': name, '播放量(万)': bfl, '评论数(万)': pls, '收藏数(万)': scs, '综合评分': TScore}
    dm_file = pandas.DataFrame(info1)
    dm_file.to_excel('1.xlsx', sheet_name="动漫数据分析")


    global dm_name
    dm_name = name
    global dm_play
    dm_play = bfl
    global dm_review
    dm_review = pls
    global dm_favorite
    dm_favorite = scs
    global dm_com_score
    dm_com_score = TScore
    print("保存文件成功！")
    return name, bfl, pls, scs, TScore


my_font = font_manager.FontProperties(fname='wqy-microhei.ttc')  # 设置中文字体（图标中能显示中文）
# 为了坐标轴上能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def v1_0():  # 综合评分条形图
    global lock
    lock.acquire()
    fig, ax1 = plt.subplots()
    plt.bar(dm_name, dm_play, color='red')
    plt.title('播放量--评论数 组合图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('播放量（万）')  # 纵轴名
    ax1.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')  # 设置横坐标变量名旋转度数和颜色

    # 播放量折线图
    ax2 = ax1.twinx()  # 组合图必须加这个
    ax2.plot(dm_review, color='cyan')  # 设置线粗细，节点样式
    plt.ylabel('评论数（万）')  # y轴
    plt.plot(1, label='播放量', color="red", linewidth=5.0)  # 图例
    plt.plot(1, label='评论数', color="cyan", linewidth=1.0, linestyle="-")  # 图例
    plt.legend()
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\1.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("1.0")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v1_1():   # 柱状图
    global lock
    lock.acquire()
    plt.bar(dm_name, dm_play, color='red')
    plt.title('播放量 条形图', fontproperties=my_font)
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('播放量（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\1条形图.png',
                dpi=1000, bbox_inches='tight')
    print("1.1")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v1_2():  # 折线图
    global lock
    lock.acquire()
    plt.plot(dm_name, dm_review, color='blue', linewidth=1.0, linestyle="-")
    plt.title('评论数折线图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('评论数（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\1折线图.png',
                dpi=1000, bbox_inches='tight')  # 保存至本地
    print("1.2")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v2_0():  # 评论数条形图
    global lock
    lock.acquire()
    fig, ax3 = plt.subplots()
    plt.bar(dm_name, dm_review, color='green')
    plt.title('评论数--收藏数 组合图')
    plt.ylabel('评论数（万）')
    ax3.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')

    # 收藏数折线图
    ax4 = ax3.twinx()  # 组合图必须加这个
    ax4.plot(dm_favorite, color='yellow')  # 设置线粗细，节点样式
    plt.ylabel('收藏数（万）')
    plt.plot(1, label='评论数', color="green", linewidth=5.0)
    plt.plot(1, label='收藏数', color="yellow", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\2.png', dpi=1000, bbox_inches='tight')
    print("2.0")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v2_1():
    global lock
    lock.acquire()
    plt.bar(dm_name, dm_review, color='red')  # 设置柱状图
    plt.title('评论数 条形图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('评论数（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\2条形图.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("2.1")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v2_2():
    global lock
    lock.acquire()
    plt.plot(dm_name, dm_favorite, color='blue', linewidth=1.0, linestyle="-")  # 设置柱状图
    plt.title('收藏数 折线图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('收藏数（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\2折线图.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("2.2")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v3_0():  # 综合评分条形图
    global lock
    lock.acquire()
    fig, ax5 = plt.subplots()
    plt.bar(dm_name, dm_favorite, color='red')
    plt.title('收藏数--评分 组合图')
    plt.ylabel('收藏数（万）')
    ax5.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')

    # 收藏折线图
    ax6 = ax5.twinx()  # 组合图必须加这个
    ax6.plot(dm_com_score, color='yellow')  # 设置线粗细，节点样式
    plt.ylabel('评分（万）')
    plt.plot(1, label='收藏数', color="red", linewidth=5.0)
    plt.plot(1, label='评分', color="yellow", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\3.png', dpi=1000, bbox_inches='tight')
    print("3.0")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v3_1():
    global lock
    lock.acquire()
    plt.bar(dm_name, dm_favorite, color='red')  # 设置柱状图
    plt.title('收藏数 条形图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('收藏数（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\3条形图.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("3.1")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v3_2():
    global lock
    lock.acquire()
    plt.plot(dm_name, dm_com_score, color='blue', linewidth=1.0, linestyle="-")  # 设置柱状图
    plt.title('评分 折线图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('评分（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\3折线图.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("3.2")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v4_0():  # 播放量条形图
    global lock
    lock.acquire()
    fig, ax7 = plt.subplots()
    plt.bar(dm_name, dm_com_score, color='cyan')
    plt.title('评分--播放量 组合图')
    plt.ylabel('评分（万）')
    ax7.tick_params(labelsize=6)
    plt.xticks(rotation=90, color='green')

    # 评论数折线图
    ax8 = ax7.twinx()  # 组合图必须加这个
    ax8.plot(dm_play, color='green')  # 设置线粗细，节点样式
    plt.ylabel('播放量（万）')
    plt.plot(1, label='评分', color="cyan", linewidth=5.0)
    plt.plot(1, label='播放量', color="green", linewidth=1.0, linestyle="-")
    plt.legend()
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\4.png', dpi=1000, bbox_inches='tight')
    print("4.0")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v4_1():
    global lock
    lock.acquire()

    plt.bar(dm_name, dm_com_score, color='red')  # 设置柱状图
    plt.title('评分 条形图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('评分（万）')  # 纵轴名 plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\4条形图.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("4.1")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v4_2():
    global lock
    lock.acquire()
    plt.plot(dm_name, dm_play, color='blue', linewidth=1.0, linestyle="-")  # 设置柱状图
    plt.title('播放量 折线图', fontproperties=my_font)  # 表标题
    plt.xlabel('剧名')  # 横轴名
    plt.ylabel('播放量（万）')  # 纵轴名
    plt.xticks(rotation=90, color='black')  # 设置横坐标变量名旋转度数和颜色
    plt.savefig(r'E:\大二下学期\Python程序设计\python实验\大作业\1\4折线图.png', dpi=1000, bbox_inches='tight')  # 保存至本地
    print("4.2")
    lock.release()
    plt.show()
    time.sleep(0.1)

def v():
    v1_0()
    v1_1()
    v1_2()
    v2_0()
    v2_1()
    v2_2()
    v3_0()
    v3_1()
    v3_2()
    v4_0()
    v4_1()
    v4_2()

def mi():
    T1=threading.Thread(target=v)
    T1.start()
    T1.join()
    print("生成视图成功！")

def shujuku():
    gui2.shujuku()
    print("数据库")

b1 = tk.Button(root1, text="查找", command=chazhao)
b1.place(x=130, y=70, width=40, height=20)
b2 = tk.Button(root1, text="重置", command=reset)
b2.place(x=190, y=70, width=40, height=20)
b3 = tk.Button(root1, text="显示", command=xianshi)
b3.place(x=250, y=70, width=40, height=20)
b4 = tk.Button(root1, text="保存", command=save)
b4.place(x=310, y=70, width=40, height=20)
b5 = tk.Button(root1, text="视图", command=mi)
b5.place(x=370, y=70, width=40, height=20)
b6 = tk.Button(root1, text="数据库", command=shujuku)
b6.place(x=430, y=70, width=40, height=20)

root1.mainloop()  # 启动消息循环

mystd.restoreStd()  # 恢复标准输出