i=0
if  i > 0:
    print("This is positive number")
elif i==0:
    print("The vale is zero")
else:
    print("This is negative number")

list1=['apples','grapes','mangoes']
for i in list1:
    print(i)
else:
    print("there are no fruits left")

list2=[1,2,3,4,5]
tot=0;
for i in list2:
    tot=tot+i

print("The sum is", tot)

# i=1
# sum=0;
# print("Enter a number")
# num=int(input())
# while(i < num):
#     sum=sum+i
#     i=i+1
# print("Sum is",sum)

#  Reverse the String
# print("Enter a string")
# str1=input()
# len1= len(str1)
# print(len1)
# i=len1-1
# while  i >=0:
#     print(str1[i])
#     i=i-1

#Sorting Alpha numeric string AS2D34 is   ADS234
print("Enter a string")
str1=input()
c1=c2=output=''
for i in str1:
    if i.isalpha():
        c1=c1+i
    else:
        c2=c2+i
print(c1,c2)
for x in sorted(c1):
    output=output+x
for x in sorted(c2):
    output=output+x
print(output)

n=input("enter a number")
print(n)

