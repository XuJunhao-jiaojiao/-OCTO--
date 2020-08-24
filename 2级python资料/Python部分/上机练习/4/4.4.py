import random
shu=random.randint(1,100)
i=5
while i>0:
    try:
        shu1=eval(input("请输入一个0~100的数,您还有{}次机会:".format(i)))
        if isinstance(shu1,int)==True:
            print("游戏结束，谢谢使用")
            break
        if shu==shu1:
            print("恭喜你，猜对了")
            break
        elif shu>=shu1:
            print("抱歉，您输入的数小了")
        else:
            print("抱歉，您输入的数大了")
        i=i-1
    except:
        print('输入错误，请检查后请重新输入')
else:
    print("谢谢使用，随机生成的数字是：",shu)