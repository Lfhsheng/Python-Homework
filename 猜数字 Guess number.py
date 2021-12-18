import random
num = random.randint(0,100)
Player_num = 0 # 声明变量 Declare variable 
while True:
    Player_num = int(input('请输入你猜的数字：')) # Speak in English: Enter the number you guessed:
    if Player_num > num:
        print('猜的大了') # Speak in Englsh: Big guess
    elif Player_num < num:
        print('猜的小了') # Speak in Englsh: Small guess
    elif Player_num == num:
        print('猜对了') # Speak in Englsh: You guessed it
        break # 跳出循环 Break out of cycle