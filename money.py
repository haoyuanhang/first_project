import os,time,re
global saved_money, _in_money

if not os.path.exists('money.txt'):
    f = open('money.txt', 'w')
    f.write('总计-余额：1000元  总工资：0元')
    print('没有money.txt文件，现在创建了一个')
    f.close()

with open('money.txt', 'r') as f:
    s_m = f.readlines()[0]
    complex_save = re.compile('余额：([0-9]*)')
    s = complex_save.findall(s_m)[0]
    complex_in = re.compile('总工资：([0-9]*)')
    i = complex_in.findall(s_m)[0]

saved_money = int(s)
_in_money = int(i)


def details(d):
    print('交易记录已保存')
    with open('money.txt', 'a') as f:
        f.write(d)
    with open('money.txt', 'r') as f:
        lines = f.readlines()
    with open('money.txt', 'w') as f:
        for line in lines:
            if "总计" in line:
                line = line.replace(line, f'总计-余额：{saved_money}元  总工资：{_in_money}元\n')
            f.write(line)


def send_money(_in):
    global saved_money, _in_money
    saved_money += _in
    print(saved_money)
    _in_money += _in
    dd = f'\n{time.strftime("%Y-%m-%d/%H:%M:%S")}:发工资{_in}元'
    details(dd)


def select_money():
    dd = f'\n{time.strftime("%Y-%m-%d/%H:%M:%S")}:合计发放工资{_in_money}元'
    with open('money.txt', 'a') as f:
        f.write(dd)


def money():
    dd = f'\n{time.strftime("%Y-%m-%d/%H:%M:%S")}:当前卡上剩余{saved_money}元'
    with open('money.txt', 'a') as f:
        f.write(dd)
