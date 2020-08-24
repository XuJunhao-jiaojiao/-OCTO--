while True:
    try:
        Nian=int(input('请输入一个年份'))
        break
    except:
        print('请输入一个正确的年份')
if Nian%100!=0 and Nian%4==0 :
    print('您输入的年份是{}，是闰年'.format(Nian))
elif Nian%400==0:
    print('您输入的年份是{}，是闰年'.format(Nian))
else:
    print('您输入的年份是{}，不是闰年'.format(Nian))
