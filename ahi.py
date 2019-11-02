x = int(input())
y = int(input())
try:
    print(x/y)
except ZeroDivisionError:
    print('不能除以0')
