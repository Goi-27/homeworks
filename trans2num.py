# -*- coding: UTF-8 -*-


def trans1(s):
    if len(s) <= 2:
        s[1] = s[1]
    elif s[2] == '零':
        s[2] = 0
    elif s[2] == '一':
        s[2] = 1
    elif s[2] == '二':
        s[2] = 2
    elif s[2] == '三':
        s[2] = 3
    elif s[2] == '四':
        s[2] = 4
    elif s[2] == '五':
        s[2] = 5
    elif s[2] == '六':
        s[2] = 6
    elif s[2] == '七':
        s[2] = 7
    elif s[2] == '八':
        s[2] = 8
    elif s[2] == '九':
        s[2] = 9
    elif s[2] == '十':
        s[2] = 10
    elif s[3] == '零':
        s[3] = 0
    elif s[3] == '一':
        s[3] = 1
    elif s[3] == '二':
        s[3] = 2
    elif s[3] == '三':
        s[3] = 3
    elif s[3] == '四':
        s[3] = 4
    elif s[3] == '五':
        s[3] = 5
    elif s[3] == '六':
        s[3] = 6
    elif s[3] == '七':
        s[3] = 7
    elif s[3] == '八':
        s[3] = 8
    elif s[3] == '九':
        s[3] = 9
    elif s[3] == '十':
        s[3] = 10
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
