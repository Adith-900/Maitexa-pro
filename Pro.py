# -------notes-----

# print(type(-)) : to find type

# --------------






# print("hello world")

# a = "Hello world"
# print(a)
# print(type(a))

# ------loop----------

# ------if-elif-else----


# a = int(input("enter a number"))
# if a < 0:
#  print("Number is negative")
# elif a == 0:
#     print("Number is zero")
# else : 
#  print("Number is positive")


# ------while loop ---------

# i = 0
# while i < 10: 
#     print("hai")
#     i=i+1

# ------print numbers upto 10-------
 
# i = 1
# while i <= 100: 
#     print(i)
#     i= i + 2


# ------For loop-------

# for i in range (100,0,-1):
#     print(i)


# -------break & continue------

# i = 0
# while i < 10: 
#     i = i+1
#     if i==5:
#         continue
#     print(i)
    

# for num in range(1, 101):
#     if num % 5 == 0:  # Check if the number is a multiple of 5
#         continue  # Skip the rest of the loop and continue to the next iteration
#     print(num)

# -------------------------------------------------------------------------------------

# --------list--------

# --list-length----

# l=[1,2,3,4,5,9]
# print(type(l))
# print(len(l))

# # ----append( to add a element last to the list)-----
# l.append(23)

# # ---insert (for insert an element)
# l.insert(2,45)

# # ---pop (deletion of element)---
# # when only pop() the last element remove , when pop(position(0-n) that value will be removed)
# l.pop(3)

# # ---remove (deletion of element  by entiring the values)---
# l.remove(2)
# print(l)

# -----clear (to remove entire elements)-----
# l.clear()
# print(l)

# -----max(biggest value) , min(smallest value)------
# print(max(l))
# print(min(l))

# -----extend( adding the values from one to other)-----

# a = [2,4,5,1,9]
# b = [10,23,25,46]
# # ---the values from b to a---
# # a.extend(b)
# # ---the values from a to b--- 
# b.extend(a)
# print(b)

# -----------

# l = [1,2,3,4,5,6,7,8,9,10]
# a = []
# for i in l:
#     if i%2==0:
#      a.append(i)
# print("the even numbers are : ",a)

# ---------------------------------------------------

# -----tupple------

# abc = (1,2,3,4,5)
# print(type(abc))
# abc.add(10)
# print(abc)

# --------------

# -----Set-----

# s = { 1,2,3,4,5,6}
# print(type(s))
# ---to add a number---
# s.add(10)
# print(s)

# ---conversion(tuple to set)---
# a = [1,2,3,4,5,6]
# s = set(a)
# print(s)

# -----UNION & INTERSECTION-----

# a = {1,2,3,4,5}
# b = { 2,4,6,8}
# c = a.union(b)
# print("the union is : ",c)
# d = a.intersection(b)
# print("the intersection is : ",d)


# -----dictionary------

# s = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}
# #  to print a value in the dictionary
# print(s['b'])
# print(type(s))
# print(s)


# data = { 'name':["aara","entha","enthina"] , 'age':[25,26,27], 'salary':[20000,21000,22000 ]}

# print(data['name'])
# print(data.keys())
# print(data.values())
# data.pop('age')
# print(data)
# -----clear to delete all the data-----
# data.clear()
# print(data)


# -----update-----
# data = {'name': "John", 'age':22, 'salary':20000}
# data.update(age="25")
# print(data)


# ------------NOTE------------------------


# data.pop('age): pop use cheith ()il enthaano kodukkunne aa attribute pokum
# data.popitem() : popitem use cheith last item pokum


# ----------------

# ---------------CHATGPT CODE FOR MULTIPLE USER AND SELECT A USER BY SEARCH------------------

# # 10 membersinte details store cheyyunna list of dictionaries
# members = [
#     {"name": "Anu", "age": 25, "salary": 50000},
#     {"name": "Ravi", "age": 30, "salary": 60000},
#     {"name": "Maya", "age": 28, "salary": 55000},
#     {"name": "Rahul", "age": 35, "salary": 75000},
#     {"name": "Sneha", "age": 24, "salary": 48000},
#     {"name": "Arjun", "age": 29, "salary": 62000},
#     {"name": "Divya", "age": 27, "salary": 51000},
#     {"name": "Kiran", "age": 32, "salary": 70000},
#     {"name": "Priya", "age": 26, "salary": 52000},
#     {"name": "Vishnu", "age": 31, "salary": 68000},
# ]

# # User input edukkunnu
# search_name = input("Enter the name of the member: ")

# # Search cheythu result print cheyyunnu
# found = False
# for member in members:
#     if member["name"].lower() == search_name.lower():
#         print("Details found:")
#         print(f"  Name: {member['name']}")
#         print(f"  Age: {member['age']}")
#         print(f"  Salary: {member['salary']}")
#         found = True
#         break

# if not found:
#     print("Member not found!")



# ------------------------------------------------------------


# -----------FUNCTION---------------

# -------NOTE--------

#  def : used to define function
#  eg 
# def name():                first two lines are function definition
#     print("Hai")
# name()                     function calling
# 
# 

# ------------------

# def name():
#     print("Hai")
    
# name()    


# def add():
#     a = 5
#     b = 2
#     print(a-b)
#     print(a+b)
#     print(a*b)
#     print(a/b)
#     print(a%b)
# add() 


# ----by using actual values------

# def add(a,b):
#     c=a+b
#     print(c)
# add(17,7)       

# number = int(input("Enter a number:"))

# def add():
#     c = 2 * number
#     print(c)
# add()    

# ------to find a number is odd or even------

# num = int(input("Enter a number: "))

# def check():
#     if num % 2 == 0:
#         print("Given number is an Even number")
#     else:
#         print("Given number is Odd Number")       
        
# check()      
      
# -------------------------------
# ----------to find a number is odd or even by passing the number as a parameter------------
#----------- method 1----------

# def check(num):
#     if num % 2 ==0:
#         print("Given number is an Even number")
#     else:
#         print("Given number is odd")
       
# check(6)        


# -------method 2-----------

# def check():
#     if num % 2 ==0:
#         print("Given number is an Even number")
#     else:
#         print("Given number is odd")
# num = 7       
# check()
# ------------------