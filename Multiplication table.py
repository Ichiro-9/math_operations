N = input ("Enter the number: ")
count = 1
multiple = (int(N) * int(count))
print ("")
print ("here you go -")
print (str(N) + (" × ") + str(count) + (" = ") + str(multiple))

while int(count) < 20 :
    count = int(count) + 1
    multiple = (int(N) * int(count))
    print (str(N) + (" × ") + str(count) + (" = ") + str(multiple))
    
    