n = int(input("Enter : "))
count = 1
Fact = 1
for count in range (0,n):
    count = (count + 1)
    Fact = (Fact * count )
    if count == n :
        break
print (Fact)