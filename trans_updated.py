# -*- coding: UTF-8 -*-


def trans2num(c):
    if c == "零":
        return 0
    elif c == "一":
        return 1
    elif c == "二":
        return 2
    elif c == "三":
        return 3
    elif c == "四":
        return 4
    elif c == "五":
        return 5
    elif c == "六":
        return 6
    elif c == "七":
        return 7
    elif c == "八":
        return 8
    elif c == "九":
        return 9
    elif c == "十":
        return 10
    else:
        print("暂不支持0-10以外数字！")


def trans2cn(num):
    if num == 0:
        return "零"
    elif num == 1:
        return "一"
    elif num == 2:
        return "二"
    elif num == 3:
        return "三"
    elif num == 4:
        return "四"
    elif num == 5:
        return "五"
    elif num == 6:
        return "六"
    elif num == 7:
        return "七"
    elif num == 8:
        return "八"
    elif num == 9:
        return "九"
    elif num == 10:
        return "十"
    else:
        print("暂不支持0-10以外数字！")


print("输入仅支持0-10以内的加减运算，按回车结束。")
try:
    ndict = {}  # 用字典存放变量名及对应变量值
    while 1:  # 用死循环来变得像交互式
        no = input()  # 装入语句
        n = no.split(" ")   # 空格分片并简化
        if no is "":  # 输入结束后按回车退出
            exit()
        if n[0] == "整数":  # 对“整数”开头语句的定义
            ndict[n[1]] = trans2num(n[3])  # 装入变量名及对应变量值
        elif n[0] in ndict.keys():  # 对“变量名”开头语句的操作
            if n[1] == "减少":
                ndict[n[0]] -= trans2num(n[2])
            elif n[1] == "增加":
                ndict[n[0]] += trans2num(n[2])
            
        elif n[0] == "看看":
            if n[1] in ndict.keys():
                print(trans2cn(ndict[n[1]]))    # 输出指定变量值
            else:
                print("未声明的变量！")        # 未定义变量时发出提示
        elif n[0] == "如果":  # 判断部分
            if n[2] == "大于":  # 判断是否大于
                if ndict[n[1]] > trans2num(n[3]):  # “则”后的处理
                    if n[5] == "看看":
                        print(n[6][1:-1])
                    else:
                        if n[6] == "增加":
                            ndict[n[5]] += trans2num(n[7])  # 增加操作
                        elif n[6] == "减少":
                            ndict[n[5]] -= trans2num(n[7])  # 减少操作

                else:  # “否则”后的处理
                    if n[8] == "看看":
                        print(n[9][1:-1])
                    elif n[8] == "无":
                        pass
                    elif n[9] == "无":
                        pass
                    elif n[9] == "增加":
                        ndict[n[8]] += trans2num(n[10])
                    elif n[9] == "减少":
                        ndict[n[8]] -= trans2num(n[10])

                    elif n[9] == "看看":
                        print(n[10][1:-1])
                    elif n[10] == "增加":
                        ndict[n[9]] += trans2num(n[11])
                    elif n[10] == "减少":
                        ndict[n[9]] -= trans2num(n[11])

            if n[2] == "小于":  # 判断是否小于
                if ndict[n[1]] < trans2num(n[3]):  # “则”后的处理
                    if n[5] == "看看":
                        print(n[6][1:-1])
                    else:
                        if n[6] == "增加":
                            ndict[n[5]] += trans2num(n[7])
                        elif n[6] == "减少":
                            ndict[n[5]] -= trans2num(n[7])

                else:  # “否则”后的处理
                    if n[8] == "看看":
                        print(n[9][1:-1])
                    elif n[8] == "无":
                        pass
                    elif n[9] == "无":
                        pass
                    elif n[9] == "增加":
                        ndict[n[8]] += trans2num(n[10])
                    elif n[9] == "减少":
                        ndict[n[8]] -= trans2num(n[10])

                    elif n[9] == "看看":
                        print(n[10][1:-1])
                    elif n[10] == "增加":
                        ndict[n[9]] += trans2num(n[11])
                    elif n[10] == "减少":
                        ndict[n[9]] -= trans2num(n[11])

            if n[2] == "等于":  # 判断是否等于
                if ndict[n[1]] == trans2num(n[3]):  # “则”后的处理
                    if n[5] == "看看":
                        print(n[6][1:-1])
                    else:
                        if n[6] == "增加":
                            ndict[n[5]] += trans2num(n[7])
                        elif n[6] == "减少":
                            ndict[n[5]] -= trans2num(n[7])

                        else:  # “否则”后的处理
                            if n[8] == "看看":
                                print(n[9][1:-1])
                            elif n[8] == "无":
                                pass
                            elif n[9] == "无":
                                pass
                            elif n[9] == "增加":
                                ndict[n[8]] += trans2num(n[10])
                            elif n[9] == "减少":
                                ndict[n[8]] -= trans2num(n[10])

                            elif n[9] == "看看":
                                print(n[10][1:-1])
                            elif n[10] == "增加":
                                ndict[n[9]] += trans2num(n[11])
                            elif n[10] == "减少":
                                ndict[n[9]] -= trans2num(n[11])
        else:
            print("请按指定格式输入！")
except IndexError:
    print("请按要求进行输入")
except SystemExit:
    print("运行结束！")