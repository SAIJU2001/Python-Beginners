#tuple in python
#tupple is immutable

my_tuple=(45,"saikat",78.9,True,"coders")

#check the type
print(type(my_tuple))

#print the tuple
print(my_tuple)

#print any specific index
print(my_tuple[1])

#neagtive indexing also present
print(my_tuple[-2])

#iterate on tuple using for loop
for j in my_tuple :
    print(j)

#print the length of the tuple
print(len(my_tuple))

#check any value is present in the tuple or not
print( "saikat" in my_tuple)
print( "welcome" in my_tuple)

#iterate on tuple using while loop
i=0
while i<len(my_tuple) :
    print(my_tuple[i])
    i+=1

#count how many times a element appear in the tuple
print(my_tuple.count("saikat"))

#find the index
print(my_tuple.index("coders"))





