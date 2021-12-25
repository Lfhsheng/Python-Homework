i = int(input('请输入数字：'))
dig_4 = int(i/1000)
dig_3 = int(i/100)-dig_4*10
dig_2 = int(i/10)-dig_4*100-dig_3*10
dig_1 = i-dig_4*1000-dig_3*100-dig_2*10
total = int(dig_4**4+dig_3**4+dig_2**4+dig_1**4)
if i == total:
    print(i,'是四叶玫瑰数')
else:
    print(i,'不是四叶玫瑰数')