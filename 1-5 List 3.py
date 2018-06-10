# 1-5 List 3
print ("1-5 List 3")
print ()
# list 3 列表方法
print ("3 列表方法")
print ()
# 3.1 append
print ("3.1 append")
print ("append方法用于在列表末尾追加一个新的对象：")
animals = ["dog","cat","horse","mouse","bird"]
print ("animals =",animals)
animals.append("monkey")
print ('animals.append("monkey")')
print ("animals =",animals)
print ()
# 3.2 count
print ("3.2 count")
print ("count方法用于统计某个元素在列表中出现的次数：")
animals2 = ["dog","cat","horse","mouse","bird","bird","cat"]
print ("animals2 = ",animals)
animals2.count("cat")
print ('animals2.count("cat"):',animals2.count("cat"))
print ("animals2",animals2)
print ()
# 3.3 extend
print ("3.3 extend")
print ("extend方法可以在列表的末尾一次性追加另一个序列的多个值，也就是用心的列表扩展原有的列表:")
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print("a =",a)
print ()
# 3.4 index
print ("3.4 index")
print ("index方法用于从列表中找出某个值第一个匹配项的索引位置：")
print ("animals2 =",animals2)
print ('animals2.index("bird"):',animals2.index("bird"))
print ()
# 3.5 insert
print ("3.5 insert")
print ("insert方法用于将对象插入到列表中：")
print ("animals =",animals)
print ('animals.insert(3,"hen")',animals.insert(3,"hen"))
print (animals)
print ()
# 3.6 pop
print ("3.6 pop")
print ("pop方法会移除列表中的一个元素，并且返回该元素的值")
num1 = [1,2,3,4,5,6,7,8,9]
print ("num1",num1)
print ('num1.pop():',num1.pop())
print (num1)

print ('num1.pop(2)',num1.pop(2))
print (num1)
print ()
# 3.7 remove
print ("3.7 remove")
print ("...")
print ()
# 3.8 reverse
print ("3.8 reverse")
print ("...")
print ()
# 3.9 sort
print ("3.9 sort")
print ("...")
