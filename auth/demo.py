num = []
size = int(input("How many elemnt you want to enter: "))
for i in range (size):
    temp = int(input("Enter the number at position "+str(i)+" : "))
    num.append(temp)
for i in range(size):
    j = 1
    for j in range(size-1):
        if(num[i])<(num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
        else:
            pass
            
print("Sorted list is ")
for i in range(size):
    print(str(num[i])+" ")