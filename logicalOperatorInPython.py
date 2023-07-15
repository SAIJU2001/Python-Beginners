# logical operator( and,or,not)

value=input("Enter a value : ")

#and condition if both true then output is true
print( int(value)>=18 and int(value)<45 )

#or condition if any one is true then output is true
print( int(value)>=18 or int(value)==12 )

#not condition if input is true then output is false and viceversa
print( not int(value)>=18 )