total = 0
a = 1000
for i in range(1000,10000):
    dig_4 = int(a/1000)
    dig_3 = int(a/100)-dig_4*10
    dig_2 = int(a/10)-dig_4*100-dig_3*10
    dig_1 = a-dig_4*1000-dig_3*100-dig_2*10
    total = dig_4**4+dig_3**4+dig_2**4+dig_1**4
    if a == dig_4**4+dig_3**4+dig_2**4+dig_1**4:
        print(a)
    a += 1