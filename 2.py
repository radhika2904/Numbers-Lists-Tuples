#swap first and last element of a list
list = [1,2,3,4,5,6]
size = len(list)
print(list)
#print(size)

temp =  list[0]
list[0] = list[size-1]
list[size-1] = temp

print(list)