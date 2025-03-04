# 正確版本
n = input()
z = []
for i in range(int(n)):
    s = input()
    s = s.split(' ')[0]

    if s is None or s == '':
        s = 0

    # '爆'
    elif s == 'Bomb':
        s = 100

    elif 'XX' in s:
        s = -100
    # 'X'
    elif 'X' in s:
        boo_cnt = s.split('X')[-1]
        # 'X'
        if boo_cnt == '':
            s = -10
        # 'X2' 'X3' ...
        else:
            s = -int(boo_cnt) * 10
        # '12' , '65' ...
    else:
        s = int(s)
    print(s)

