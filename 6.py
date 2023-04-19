#palindrome
print("enter counter")
counter =  int(input())

while(counter>0):
    print("enter string")
    a = input()

    size = len(a)
    print(size)

    mid = int(size/2)
    print(mid)
    i = 0
    flag = 0

    for i in range (0, mid):
        if a[i] == a[size-1-i]:
            flag = +1
        else:
            flag = 0
            break

    if flag == 0:
        print("Not a palindrome string")
    else:
        print("palindrome string")
    counter = counter-1
