#Question 1 : create the list with user defined input
print("enter the list of items")
list=[]
x=input("1")
y=input("2")
z=input("3")
print("the list is")
list=[x,y,z]
print(list)
print("\n")

#Question 2 :  add the following list to the upper created list
['google','apple','facebook','microsoft','tesla']
L2=['google','apple','facebook','microsoft','tesla']
print(L2)
print(list.extend(L2))
print(list)
print("\n")

#Question 3 : count the no. of times object occur
print(list.count(1))

Question 4 : create the list with number and sort in ascending order
list=[1,3,2,6,5]
print(list)
print(list.sort())
print(list)


#Question 5 : enter two array and merge them and save them in another
A=[1,2,3]
print(A)
B=[6,4,5]
print(B)
print(A.sort())
print(A)
print(B.sort())
print(B)
C=(A,B)
print(C)
C=A+B
print(C)

#Question 6 : implement stack and queue using list

#stack operations

S=["Diksha","Meenaakshi","Bikram"]
S.append("Ishu")
S.append("Muskan")
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)

#queue operations

q=(["Poonam","Diksha","Mansi","Bikram"])
print(q)
q.append("Harleen")
print(q)
print(q.pop())
q.append("Oreo")
print(q)
print(q.pop())
print(q)


