# 3-2 function2
"""
To understand local and global variables we will go through two examples.
"""
# function 1

def change(b):
    a = 90
    print(a)
a = 9
print("Before the function call ",a)
print("inside change function", end= ' ')
change(a)
print("After the function call ",a)
print()
# function2

def changeB(b):
    global a
    a = 90
    print(a)
a = 9
print("Before the function call ",a)
print("inside change function", end=' ')

changeB(a)
print("After the function call ", a)
print()
# function 3
def test(a, b = -20):
    if(a > b):
        return True
    else:
        return False
