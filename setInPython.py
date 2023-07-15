#set in python
#for unique element we used set

my_set={45,"saikat",45,78.9,45,True,"saikat",45,True,45}

#check the type
print(type(my_set))

#print the set
print(my_set)

#iterate on set using for loop
for j in my_set :
    print(j)

#print the length of the set
print(len(my_set))

#check any value is present in the set or n
print( "saikat" in my_set)
print( "welcome" in my_set)

#to remove all the elements from the set
my_set.clear()
print(my_set)





