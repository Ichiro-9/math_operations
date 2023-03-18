def solution(num):
    a = 0
    b = 1
    for a in range(0,num):
        b = a + 1
        if a * b == num*2:
            print (f"{a}, {b}")

num = int(input("Enter the Number: "))

def output(num):
    x = []
    for a in range(0,num+1):
        x.append(a)
        if sum(x)== num:
            print(True)
            break
output(num)
