Day1=int(input('请输入一个介于1~7的数：'))
if Day1==1:
    Day2="一"
elif Day1==2:
    Day2="二"
elif Day1==3:
    Day2="三"
elif Day1==4:
    Day2="四"
elif Day1==5:
    Day2="五"
elif Day1==6:
    Day2="六"
else:
    Day2='七'
print("星期{}".format(Day2))