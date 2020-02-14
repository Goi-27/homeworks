# -*- coding: UTF-8 -*-


def trans1(s):
    if len(s) <= 2:
        s[1] = s[1]
        return s
    if s[0]=='整数':
        n=1
    elif s[1]=='增加' or s[1]=='减少':
        n=1
    elif s[0]=='如果':
        n=7
    if s[len(s)-n] == '零':
        s[len(s)-n] = 0
    elif s[len(s)-n] == '一':
        s[len(s)-n] = 1
    elif s[len(s)-n] == '二':
        s[len(s)-n] = 2
    elif s[len(s)-n] == '三':
        s[len(s)-n] = 3
    elif s[len(s)-n] == '四':
        s[len(s)-n] = 4
    elif s[len(s)-n] == '五':
        s[len(s)-n] = 5
    elif s[len(s)-n] == '六':
        s[len(s)-n] = 6
    elif s[len(s)-n] == '七':
        s[len(s)-n] = 7
    elif s[len(s)-n] == '八':
        s[len(s)-n] = 8
    elif s[len(s)-n] == '九':
        s[len(s)-n] = 9
    elif s[len(s)-n] == '十':
        s[len(s)-n] = 10
    return s


def trans2(temp):
    if temp[1] == 0:
        temp[3] = '零'
    elif temp[1] == 1:
        temp[3] = '一'
    elif temp[1] == 2:
        temp[3] = '二'
    elif temp[1] == 3:
        temp[3] = '三'
    elif temp[1] == 4:
        temp[3] = '四'
    elif temp[1] == 5:
        temp[3] = '五'
    elif temp[1] == 6:
        temp[3] = '六'
    elif temp[1] == 7:
        temp[3] = '七'
    elif temp[1] == 8:
        temp[3] = '八'
    elif temp[1] == 9:
        temp[3] = '九'
    elif temp[1] == 10:
        temp[3] = '十'
    return temp


def get_input():
    str = input()
    s = str.split(" ")
    if len(s) > 0:
        if s[0] == '整数':
            temp[0] = s[1]
        elif s[0] == '看看' or '如果':
            temp[0] = s[1]
        else:
            temp[0] = s[0]
        return s
    else:
        return None


def rep(s, temp):
    if (s[0] == '整数') and (s[2] == '等于'):
        temp[0] = s[1]  # 整数 气温
        # print(temp[0])
        temp[1] = s[3]  # 等于 十
        # print(temp[1])
    if s[0] == temp[0]:
        if s[1] == '减少':  # 气温 减少 三
            temp[1] = temp[1] - s[2]
            # print(temp[1])
        if s[1] == '增加':  # 气温 增加 二
            temp[1] = temp[1] + s[2]
            # print(temp[1])

    if s[0] == '看看':  # 看看 气温
        trans2(temp)
        print(temp[3])

    if s[0] == '如果':  # 如果 气温 大于 八 则 看看 “你好，世界” 否则 看看 “冻死我了”
        if s[2] == '大于':
            if temp[1] > s[3]:
                print(s[6])     # “你好，世界”
            else:
                print(s[9])     # “冻死我了”


if __name__ == '__main__':
    temp = ['', 0, 0, '']
    while 1:
        s = get_input()
        if s is not None:
            s = trans1(s)
            temp = trans2(temp)
            rep(s, temp)
