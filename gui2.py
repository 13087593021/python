import xlrd
import pymysql
import tkinter as tk
from tkinter import ttk

def shujuku():
    root = tk.Tk()  # 创建窗口对象
    root.title('数据库')
    root.geometry('600x500')


    db = pymysql.connect(host='localhost', user='root', password='123456',
                         port=3306, db='haha', charset='utf8')
    cursor = db.cursor()
    print("数据库连接成功")

    work_book = xlrd.open_workbook('1.xlsx')
    sheet_name = work_book.sheet_by_name('动漫数据分析')  # 按名称获取值

    t1 = tk.StringVar()
    t2 = tk.StringVar()
    t3 = tk.StringVar()
    t4 = tk.StringVar()
    t5 = tk.StringVar()
    t6 = tk.StringVar()

    l1 = tk.Label(root, text="编号")
    l1.place(x=60, y=20, width=40, height=30)
    e1 = tk.Entry(root, textvariable=t1, show=None)  # 输入框
    e1.place(x=110, y=20, width=80, height=30)

    l2 = tk.Label(root, text="动漫名")
    l2.place(x=230, y=20, width=40, height=30)
    e2 = tk.Entry(root, textvariable=t2, show=None)  # 输入框
    e2.place(x=280, y=20, width=80, height=30)

    l3 = tk.Label(root, text="播放量")
    l3.place(x=400, y=20, width=50, height=30)
    e3 = tk.Entry(root, textvariable=t3, show=None)  # 输入框
    e3.place(x=450, y=20, width=80, height=30)

    l4 = tk.Label(root, text="评论数")
    l4.place(x=60, y=60, width=40, height=30)
    e4 = tk.Entry(root, textvariable=t4, show=None)  # 输入框
    e4.place(x=110, y=60, width=80, height=30)

    l5 = tk.Label(root, text="收藏数")
    l5.place(x=230, y=60, width=40, height=30)
    e5 = tk.Entry(root, textvariable=t5, show=None)  # 输入框
    e5.place(x=280, y=60, width=80, height=30)

    l6 = tk.Label(root, text="综合评分")
    l6.place(x=400, y=60, width=50, height=30)
    e6 = tk.Entry(root, textvariable=t6, show=None)  # 输入框
    e6.place(x=450, y=60, width=80, height=30)

    yscrollbar = ttk.Scrollbar(root, orient='vertical')  # 右边的滑动按钮
    columns = ('编号', '播放量（万）', '评论数（万）', '收藏数（万）', '综合评分')
    tree = ttk.Treeview(root, columns=('编号', '动漫名', '播放量（万）', '评论数（万）', '收藏数（万）', '综合评分'),
                        selectmode='browse', show="headings", yscrollcommand=yscrollbar.set)
    tree.column('编号', width=40, anchor='center')
    tree.column('动漫名', width=120, anchor='center')
    tree.column('播放量（万）', width=70, anchor='center')
    tree.column('评论数（万）', width=70, anchor='center')
    tree.column('收藏数（万）', width=70, anchor='center')
    tree.column('综合评分', width=70, anchor='center')

    tree.heading('编号', text='编号')
    tree.heading('动漫名', text='动漫名')
    tree.heading('播放量（万）', text='播放量（万）')
    tree.heading('评论数（万）', text='评论数（万）')
    tree.heading('收藏数（万）', text='收藏数（万）')
    tree.heading('综合评分', text='综合评分')

    tree.place(x=50, y=160, width=500, height=300)
    yscrollbar.place(x=550, y=160, height=300)

    # 获取列表的第一个元素
    def takeSecond(elem):
        return int(elem[0])

    def treesort(tree, col, reverse):
        l = [(tree.set(k, col), k) for k in tree.get_children('')]
        l.sort(key=takeSecond, reverse=reverse)
        for index, (val, k) in enumerate(l):
            tree.move(k, '', index)
        tree.heading(col, command=lambda: treesort(tree, col, not reverse))

    for col in columns:
        tree.heading(col, text=col, command=lambda _col=col: treesort(tree, _col, False))

    def qingkong(tree):
        x = tree.get_children()  # 清空内容
        for item in x:
            tree.delete(item)

    # 显示
    def xianshi():
        qingkong(tree)
        sql = "select * from sheet"
        cursor.execute(sql)  # 使用游标对象执行SQL语句；
        results = cursor.fetchall()
        if results:
            for i in range(0, len(results)):
                tree.insert('', i, values=(results[i]))
            print("查找成功")
        else:
            tree.insert('', 0, values=('无', '无', '无', '无', '无', '无'))
            print("查找失败")
    xianshi()


    def sqlinsert():
        qingkong(tree)
        sql1 = "insert into sheet(id,name,bfl,pls,scs,TScore) values (%s,%s,%s,%s,%s,%s)"
        value = [(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get())]
        try:
            cursor.executemany(sql1, value)
            db.commit()
            print("插入成功")
        except:
            print("插入失败")
        xianshi()


    def sqldelete():
        qingkong(tree)
        sql2 = 'delete from sheet where id=%s'
        value = [e1.get()]
        try:
            cursor.executemany(sql2, value)
            db.commit()
            print("删除成功")
        except:
            print("删除失败")
            db.rollback()
        xianshi()


    def sqlquery():
        qingkong(tree)
        sql3 = 'select * from sheet where id=%s'
        value = [(e1.get())]
        try:
            if e1.get() == 'all':
                xianshi()
            else:
                cursor.executemany(sql3, value)  # 使用游标对象执行SQL语句；
                results1 = cursor.fetchall()
                if results1:
                    for i in range(0, len(results1)):
                        tree.insert('', i, values=(results1[i]))
                    print("查找成功")
                else:
                    tree.insert('', 0, values=('无', '无', '无', '无', '无', '无'))
                    print("无结果")
        except:
            print("查找失败")
            db.rollback()

    def sqlupdate():
        qingkong(tree)
        sql4 = 'update sheet set name=%s where id=%s'
        value = [(e2.get(), e1.get())]
        try:
            cursor.executemany(sql4, value)
            db.commit()
            print("更新成功")
        except:
            print("更新失败")
            db.rollback()
        xianshi()

    def reset():  # 重置
        t1.set('')
        t2.set('')
        t3.set('')
        t4.set('')
        t5.set('')
        t6.set('')

    def daoru():
        for i5 in range(0, sheet_name.nrows):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            row_data = sheet_name.row_values(i5)
            sql5 = "insert into sheet(id,name,bfl,pls,scs,TScore) values (%s,%s,%s,%s,%s,%s)"
            value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5])
            cursor.execute(sql5, value)
            db.commit()
        print("导入成功")

    b1 = tk.Button(root, text="增加", command=sqlinsert)
    b1.place(x=70, y=120, width=40, height=20)
    b2 = tk.Button(root, text="删除", command=sqldelete)
    b2.place(x=140, y=120, width=40, height=20)
    b3 = tk.Button(root, text="查找", command=sqlquery)
    b3.place(x=210, y=120, width=40, height=20)
    b4 = tk.Button(root, text="更改", command=sqlupdate)
    b4.place(x=280, y=120, width=40, height=20)
    b5 = tk.Button(root, text="重置", command=reset)
    b5.place(x=350, y=120, width=40, height=20)
    b6 = tk.Button(root, text="导入", command=daoru)
    b6.place(x=420, y=120, width=40, height=20)
    b7 = tk.Button(root, text="显示", command=xianshi)
    b7.place(x=490, y=120, width=40, height=20)

    root.mainloop()  # 启动消息循环
    db.close()  # 关闭连接