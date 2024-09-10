# n = int(input('length of list:'))
# lst1 = []
# lst2 = []
# for i in range(n):
#     element = int(input('enter the element:'))
#     lst1.append(element)
# print('\n')
# print(lst1)
# print('\n')   
# for j in lst1:
#     if j%2 == 1:
#         lst2.append(j)
# print(lst2)
# print('\n')
# for k in lst2:
#     for l in range(1,6):
#         print(f'{k} * {l} = {k*l}')
#     print('\n')
    
###  USING LIST COMPREHENSION   


n = int(input('length of list:'))
lst1 = [int(input('enter the number:')) for i in range(n)]

print('\n')
print(lst1)
print('\n')  
 
lst2 = [j for j in lst1 if j % 2 == 1]   

print(lst2)
print('\n')
for k in lst2:
    for l in range(1,6):
        print(f'{k} * {l} = {k*l}')
    print('\n')
    