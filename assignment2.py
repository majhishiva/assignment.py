#calculate the sum of all numbers from 1 to a given number

# n = int(input("Please enter the number:"))
# sum = 0
# for i in range(n):
#     number = int(input())
#     sum = sum + number
    
# print("Total sum of number is : ", sum)

# n = int(input("Please ente the number :"))
# total_sum = 0
# number = [i for i in range(1,n+1)]
# total_sum = sum(number)
# print("The total sum of number is : ", total_sum)


# assignment no:1


# n = int(input("Please ente the number :"))
# number = [ int(input()) for i in range(n)]
# total_sum = sum(number)
# print("The total sum of number is : ", total_sum)


# assignment no:2

# print this pattern:
    
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5

# n = int(input("Please enter the number : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
    
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


n = int(input("Please enter no of rows : "))
for i in range(n):
    for j in range(i,n):
        print('*',end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()







    

    