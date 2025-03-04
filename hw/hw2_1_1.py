from pyquery import PyQuery as pq

html = """
<table id="customers">
    <caption>
        Purchasing List
    </caption>
    <thead>
        <tr>
            <th>Category</th>
                <th>Item</th>
            <th>Price</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Phone</td>
            <td>iPhone 13</td>
            <td>$25,900</td>
        </tr>
        <tr>
            <td>Tablet</td>
            <td>Redmi Pad5 Pro</td>
            <td>$4,999</td>
        </tr>
        <tr>
            <td>Air Phone</td>
            <td>AirPods</td>
            <td>$6,490</td>
        </tr>
        <tr>
            <td>Tablet</td>
            <td>iPad Pro</td>
            <td>$25,900</td>
        </tr>
        <tr>
            <td>Air Phone</td>
            <td>Redmi AirDots</td>
            <td>$1,800</td>
        </tr>
        <tr>
            <td>Air Phone</td>
            <td>Redmi AirDots2</td>
            <td>$2,800</td>
        </tr>
        <tr>
            <td>Tablet</td>
            <td>iPad Mini</td>
            <td>$14,900</td>
        </tr>
    </tbody>
</table>
"""
doc = pq(html)

purchasing = []
trs = doc("tbody tr")
for tr in trs.items():
    tds = tr('td')
    x = tds.text().split('td')
    tdlist = []
    for td in tds.items():
        y = td.text()
        if '$' in y:
            y = int(y.replace(',', '').replace('$', ''))
        tdlist.append(y)
    purchasing.append(tuple(tdlist))



s1 = input()
op = []
for j in range(len(purchasing)):
    if s1 == purchasing[j][0]:
        op.append(purchasing[j])
if op == []:
    print('No matched category')
else:
    print(op)

s2 = input()
op = []
for j in range(len(purchasing)):
    if s2 == purchasing[j][1]:
        op.append(purchasing[j])
if op == []:
    print('No matched item')
else:
    print(op)

s3 = input()
p1 = int(s3.split(' ')[0])
p2 = int(s3.split(' ')[1])
op = []
for j in range(len(purchasing)):
    if p1 < int(purchasing[j][2]) < p2:
        op.append(purchasing[j])
if op == []:
    print('No matched price')
else:
    print(op)