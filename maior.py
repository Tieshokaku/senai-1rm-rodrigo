def maior (n1, n2, n3):
        if (n1 >n2 and n1 > n3):
                return n1
        elif (n2 > n1 and n2>n3):
                return n2
        elif (n3 > n1 and n3 >n2):
                return n3       
a= float (input(" numero 1:"))
b= float (input(" numero 2:"))
c= float (input ("numero 3:"))

print (maior (a, b, c))