#Super comp program
print ("Hey there,")
print ("I am Super comp🐱‍💻")
print ("what do you want in these operations?")
print ("")
print ("Basic calculations(a1)")
print ("Average of 5 or 4 numbers(a2)")
print ("time conversion(a3)")
print ("celcuis into fahrenheit(a4) ")
print ("fahrenheit into celcuis(a5)" )
print ("Factors and HCF of 2 num(a6)")
print ("multiples and LCM of num(a7)")
print ("square root of a number(a8)")
print ("calculate your simple interest and amount(a9)")
print ("time difference between london to any other place(b1)")
print ("BODMAS (b2)")

print("")
op = input("type the word near the operation your want: ")

# operations........................................................

#a1)_________________________________________________________________
if (op) == "a1" : 
    print ("")
    print ("Basic operations🐱‍💻")
    ab = input("please Enter 1st Number: ")
    ac = input("please Enter 2nd Number: ")
    print ("")
    print ("here you go")
    print("")
    print ("First num: " + str(ab))
    print ("second num: " + str(ac))
    print ('')
    add = float(ab) + float(ac)
    sub = float(ab) - float(ac)
    mul = float(ab) * float(ac)
    quo = float(ab) / float(ac)
    print ('total: {0}'.format(add))
    print ('differnce: {0}'.format(sub))
    print ('Product: {0}'.format(mul))
    print ('quotient: {0}'.format(quo))
    print ("")
    print ("pleased to answer your questions")

#a2__________________________________________________________________

if (op) == "a2" :
    print ("")
    print ("Average of 5 numbers🐱‍💻")
    sub54 = input("how many num average you want 5 or 4: ")
    if (sub54) == "5" :
        print ("please enter your numbers -")
        print ( "")
        m = int(input("num 1:"))
        s = int(input("num 2:"))
        e = int(input("num 3:"))
        sc = int(input ("num 4:"))
        c = int(input ("num 5:"))
        print("")
        print ("now lets see what is the average of your numbers")
        total_average = (m + s + e + sc + c)/5
        print("")
        finish_statment = 'The average of your numbers is '
        print ((finish_statment) + str(total_average))
        print("")
        print ("Wow!you are an intelligent student")
    if (sub54) == "4" :
        print ("please enter your numbers -")
        print ( "")
        m1 = int(input("num 1:"))
        s2 = int(input("num 2:"))
        e2 = int(input("num 3:"))
        sc3 = int(input ("num 4:"))
        print("")
        print ("now lets see what is the average of your numbers")
        total_average = (m1+s2+e2+sc3)/4
        print("")
        finish_statment = 'The average of your numbers is '
        print ((finish_statment) + str(total_average))
        print("")
        print ("pleased to tell the average of your numbers")
        
#a3___________________________________________________________________
        
if (op) == "a3" :
    print ("")
    print ("time conversion🐱‍💻")
    time = input("do you want to convert hours(h) or days(d): ")
    if (time) == "h" :
        print ("Enter")
        ho = int(input("hours:"))
        print ("")
        print ("answer is ")
        print("")
        m = int(ho)*60
        s = int(ho)*3600
        d = int(ho)/24
        h_statement = (str(ho) + (" hours is equal to "))
        s1_statement = (" seconds")
        m1_statement = (" minutes ")
        d1_statement = (" days ")
        print ((h_statement) + str(s) + (s1_statement))
        print ((h_statement) + str(m) + (m1_statement))
        print ((h_statement) + str(d) + (d1_statement))
        print("")
        print ("pleased to convert time with you")
    if (time) == "d" :
        print ("Enter")
        da = int(input("Days:"))
        print ("")
        print ("answer is ")
        print("")
        m = int(da)*144
        h = int(da)*24
        y = int(da)/365
        h_statement = (str(da) + (" days is equal to "))
        s1_statement = (" minutes ")
        m1_statement = (" hours ")
        d1_statement = (" years ")
        print ((h_statement) + str(m) + (s1_statement))
        print ((h_statement) + str(h) + (m1_statement))
        print ((h_statement) + str(y) + (d1_statement))
        print("")
        print ("pleased to convert time with you")
        
#a4____________________________________________________________________
        
awe = input("did you enjoy our programs: ")       
        
    