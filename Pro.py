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

#------print numbers upto 10-------
 
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

#-----max(biggest value) , min(smallest value)------
# print(max(l))
# print(min(l))

#-----extend( adding the values from one to other)-----

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
a = [1,2,3,4,5,6]
s = set(a)
print(s)


