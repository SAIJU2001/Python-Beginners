#calculator using python

first=input("Enter first number : ")
operator=input("Enter the operator(+,-,*,/,%,**) : ")
second=input("Enter second number : ")

if operator=='+' :
    print("addition is : "+str( int(first)+int(second) ))
elif operator=='-' :  
    print("subtraction is : "+str( int(first)-int(second) ))
elif operator=='*' :
    print("multiplication is : "+str( int(first)*int(second) ))
elif operator=='/' :
    print("division is : "+str( int(first)/int(second) ))
elif operator=='%' :
    print("modulus is : "+str( int(first)%int(second) ))
elif operator=='**' :
    print("to the power is : "+str( int(first)**int(second) ))
else :
    print("Invalid operator")

