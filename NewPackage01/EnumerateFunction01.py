#Python program to illustrate enumera function
l1=["Elsa", "Anna", "Olaf"]
s1="Kristoff"

#Creatring enumerate objects
obj1=enumerate(l1)
obj2=enumerate(s1)

print "Return type:",type(obj1)
print list(enumerate(l1))

#Changing start index to 2 from 0
print list(enumerate(s1,2))
