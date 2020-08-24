Q = 'w'
while Q != 'q':
    zifuchuan = input('请输入一个字符串')
    zimu = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
            'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b',
            'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
            'C', 'V', 'B', 'N', 'M']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    kongge = [' ']
    zimuNumber = 0
    Number = 0
    kongNumber = 0
    qitaNumber = 0
    for i in zifuchuan:
        if i in zimu:
            zimuNumber = zimuNumber+1
        elif i in number:
            Number += 1
        elif i in kongge:
            kongNumber += 1
        else:
            qitaNumber += 1
    Number = str(Number)
    qitaNumber = str(qitaNumber)
    kongNumber = str(kongNumber)
    zimuNumber = str(zimuNumber)
    print('你输入的字母个数为：{},数字的个数为{}'.format(zimuNumber, Number))
    print('空格的个数为{},其他的个数为{}'.format(kongNumber, qitaNumber))
    Q = input('按q结束，按回车键继续')
