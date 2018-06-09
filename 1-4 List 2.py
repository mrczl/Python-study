# 1-4 List 2
print ("------1-4 List 2-------")
print ()
# list 2.1 改变列表：元素赋值
print ("2.1 改变列表：元素赋值")
print ("list1 = [1,1,3,4]")
list1 = [1,1,3,4]
print ("list1[1] = 2")
list1[1] = 2
print ("list1=",list1)
print ("------------------------")

print ("***Exercise 1***")
months = ["January","February","Match","May","June"]
print ("months=",months)
months[3:] = "April","May"
print ("months[3:]=",months[3:])
print ("months =",months)
print ("------------------------")
print ("***Exercise 2***")
months = ["January","February","Match","May","June"]
print ("months=",months)
months[2:3] = "April","May"
print ("months[2:3]=",months[2:3])
print ("months =",months)
print ("Why Exercise 1 is different from Exercise 2???")
print ()

# list 2.2 删除元素
print ("2.2 删除元素")
names = ['Alice','Beth','Cecil','Dear','Earl']
print ("names=",names)
del names[3]
print ('del names[3]')
print ("names=",names)
print ()


# list 2.3 分片赋值
print ("2.3 分片赋值")
print ("list函数")
name = "Mrczl"
print("name =",name)
list(name)
print("list(name) =",list(name))
print ("type(name) :",type(name))
print()
mambers = [1,2,3,4,5,6]
print ("mambers =",mambers)
mambers[1:4] = []
print ("mambers[1:4] = []")
print ("mambers =",mambers)