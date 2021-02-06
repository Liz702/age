driving = input('请问您有没有开过车？')
age = input('请问您的年龄？')
age = int(age)
if driving == '有':
    if age >= 18:
    	print('您已通过验证')
    else:
    	print('您未通过验证')
elif driving == '没有':
	print('您已通过验证')
else:
	print('系统无法识别您的回答')