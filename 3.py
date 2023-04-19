#swap two elements of a list
list = [1,2,3,4,5,6]
print(list)
print("enter elements to swap")
a =  int(input())
b =  int(input())
#print(a,b)
size =  len(list)
if((a<size) and (b<size)):
    temp =  list[a]
    list[a] = list[b]
    list[b] = temp

print(list)