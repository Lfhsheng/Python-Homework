total = 0
num = int(input('请输入一个百位数：')) # Speak in Englsh: Please enter a hundreds digit:
hun_num = int(num/100)
ten_num = int(num/10)-10*hun_num
single_num = num%10
hun_num = hun_num**3
ten_num = ten_num**3
single_num = single_num**3
total = hun_num+ten_num+single_num
if total == num:
    print('这个数是水仙花数') # Speak in English: This number is the Narcissistic number
else:
    print('这个数不是水仙花数') # Speak in English: This number is not the Narcissistic number
