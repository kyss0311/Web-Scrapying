# 錯誤版本
import re

n = input()
z = []
for i in range(int(n)):
    s = input()
    if re.findall(r'(.*|\W) \".*\"', s):
        z += re.findall(r'(.*|\W) \".*\"', s)
    else:
        z += [0]

    if z[i] is None or z[i] == '0' or z[i] == '':
        z[i] = 0

        # '爆'
    elif z[i] == 'Bomb':
        z[i] = 100

    elif 'XX' in z[i]:
        z[i] = -100
        # 'X'
    elif 'X' in z[i]:
        boo_cnt = z[i].replace('X', '')
        # 'X'
        if boo_cnt == '':
            z[i] = -10
        # 'X2' 'X3' ...
        else:
            z[i] = -int(boo_cnt) * 10
        # '12' , '65' ...
    else:
        z[i] = int(z[i])
for i in z:
    print(i)
