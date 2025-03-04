import re

n = int(input())
for i in range(n):
    s = input()
    s = re.findall(r"https:\/\/www\.google\.com\/maps\/[A-z]*\/([A-z0-9+]*)\/@([0-9\.\-]+)\,([0-9\.\-]+)", s)

    x = s[0][0].replace("+", ' ')
    y = float(s[0][1])
    yy = round(y, 3)
    if yy == 0.0:
        yy = 0
    z = float(s[0][2])
    zz = round(z, 3)
    if zz == 0.0:
        zz = 0
    print("No {}. {}: ({}, {})".format((i+1), x, zz, yy))