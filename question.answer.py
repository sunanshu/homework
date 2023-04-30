list=eval(input("enter element of list"))
num=int(input("enter the number you want  to search"))
if num in list:
     print(num,"number is present at position",list.index(num))
else:
     print("number is absent")
    
# list=eval(input("enter element of list"))
# print(list)
# print(max(list))


############################################### Group D q2

# list=eval(input("enter the list having the element between 1 and 12:"))
# for i in range(len(list)):
#     if list[i]>10:
#         list[i]=10
# print("new list is:",list)       
# even_count=0
# odd_count=0
# for num in list:
#     if num%2==0:
#         even_count+=1
#     else:
#         odd_count+=1

 print("even number in given list is",even_count)
# print("odd number in given list is",odd_count)

########Group c question 1 answer
list=[1,2,3,4,5]
print("Smallest integer of the above list is=",min(list))
print(max(list))
        
