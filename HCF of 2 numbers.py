print ("")
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
rank = 1
divisor = 1
C_list = ("1")
h_num = int(max(list(str(n1) + str(n2))))
print("")

for rank in range(0, h_num):
    divisor = int(divisor + 1)
    rank = int(rank + 1)
    n1d = int(n1) % (divisor)
    n2d = int(n2) % (divisor)
    if rank == h_num:
        break
    if n1d == 0:
        if n2d == 0:
            C_list = (C_list + (" , ") + str(divisor))
            HCF = max(C_list)
    hn = int(h_num) - 1
    if C_list == '1':
        HCF = ("It's a Co prime")


print(("Common Factors = {}".format(C_list)))
print(("HCF = {}".format(HCF)) )







