#list in python
#list are the heterogenius data type(complex type)

my_list=[45,"saikat",78.9,True]

#check the type
print(type(my_list))

#print the list
print(my_list)

#print any specific index
print(my_list[1])

#neagtive indexing also present
print(my_list[-2])

#iterate on list using for loop
for j in my_list :
    print(j)

#append is used to add any element to the last of the list
my_list.append("coders")
print(my_list)

#insert any value to any index
my_list.insert(1,'z')
print(my_list)

#print the length of the list
print(len(my_list))

#check any value is present in the list or not
print( "saikat" in my_list)
print( "welcome" in my_list)

#iterate on list using while loop
i=0
while i<len(my_list) :
    print(my_list[i])
    i+=1

#to remove all the elements from the list
my_list.clear()
print(my_list)





