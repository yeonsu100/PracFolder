#Python program to illustrate enumera function in loop
l1=["Elsa", "Anna", "Olaf"]

#Printing the tuples in object directly
for ele in enumerate(l1):
    print ele
print
#Changing index and printing separately
for count, ele in enumerate(l1,100):
    print count,ele
