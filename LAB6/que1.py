# 1. write a program in python to use various inbuild functions of list
list = [1,5,1,9,6,5,8,7]
list.append(100)
print(list)
list2 = list.copy()
print(list2)
list2.clear()
print(list2)
print(list.count(1))
list2 = [1,2,3]
list.extend(list2)
print(list)
print(list.index(6))
print(list.pop())
list.remove(9)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
print(min(list))
print(max(list))