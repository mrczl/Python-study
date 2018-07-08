# 3-3 function4
#数字n的阶乘算法
#常规方法
x = int(input("Enter a number >"))
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
result = factorial(x)
print("%d 的阶乘是：%d" % (x,result))

#递归写法
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
result = factorial(x)
print("%d 的阶乘是：%d" %(x,result))
