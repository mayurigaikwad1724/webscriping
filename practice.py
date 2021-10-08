# num=int(input("enter the number"))
# rev=0
# while num>0:
#     reminder=num%10
#     rev=(rev*10)+reminder
#     num=num//10
# print(rev)




# num=int(input("enter a number"))
# m=["q","z"]
# k=list(m)
# i=0
# b=[]
# j=1
# while j<=num:
#     i=0
#     while i<len(m):
#         m[i]=k[i]+str(j)
#         b.append(m[i])
#         i+=1
#     j+=1
# print(b) 



#bubleshort
# num=[5,8,6,2,3,9,1,4]
# i=0
# while i<len(num):
#     j=0
#     while j<i:
#         if num[i]<num[j]:
#             t=num[i]
#             num[i]=num[j]
#             num[j]=t
#         j=j+1
#     i=i+1
# print(num) 



#count
# list=[50,40,23,70,56,12,5,10,7]
# count=0
# for k in list:
#     count+=1
# print(count)




# def delete_nth(list,n):
#     i=0
#     while i<n:
#         list.pop()
#         i=i+1
#     print(list)
# delete_nth([1,1,2,3],2) 





# n=[[1,2,3,4],[4,5,8,7]]
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         print(n[i][j])
#         j=j+1
#     i=i+1





#kitna paisa
# kitna_paisa=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
# i=0
# carorepati=0
# lakhpati=0
# dilwale=0
# while i<len(kitna_paisa):
#     n=kitna_paisa[i]
#     if n<100000:
#         dilwale=dilwale+1
#     elif n>=100000 and n<10000000:
#         lakhpati=lakhpati+1
#     elif n>=10000000:
#         carorepati=carorepati+1
#     i=i+1
# print(dilwale)
# print(lakhpati)
# print(carorepati)


#marks
# marks=[[78,34,56,45,34,63],
#        [45,43,63,53,23,24],
#        [23,43,65,56,75,34]]
# i=0
# sum=0
# while i<len(marks):
#        j=0
#        while j<len(marks[i]):
#               sum=sum+marks[i][j]
#               j=j+1
#        i=i+1
# print(sum) 




# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# b=a[0]
# c=a[0]
# while i<len(a):
#     if a[i]>b:
#         b=a[i]
#         if a[i]<c:
#             c=a[i]
#     i=i+1
# print("maximum number",b)
# print("minimum number",c)
 




# number=30
# n=[10,11,12,13,14,17,18,19]
# i=0
# a=[]
# while i<len(n):
#     j=4
#     while j<len(n):
#         if n[i]+n[j]==number:
#             a.append([n[i],n[j]])
#         j+=1
#     i+=1
# print(a)




# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     print(i-1,"+",end="")
#     i=i+1
# print(n,end="")
# print("=",sum) 



# dictionary

# dic1={1:10, 2:20}
# dic2={3:30, 2:40}
# dic3={5:50, 6:60}
# dict4={}
# dict4.update(dic1)
# dict4.update(dic2)
# dict4.update(dic3)
# print(dict4)





# dict={
#     "alex":["subj", "subj2", "subj3"],
#     "david":["subj1", "subj2"]}
# a = sum(map(len, dict.values()))
# print(a)



# my_dict = {
#     "a":50,
#     "b":58,
#     "c":56,
#     "d":40,
#     "e":100,
#     "f":20}
# c=[]
# for i in my_dict.values():
#     if i > 50:
#         c.append(i)
# print(c) 





# num = int(input("enter the number"))
# myDict = {}
# for x in range (1,num + 1):
#     myDict[x]= x**2
# print("Dictionary = ",myDict) 





# from heapq import nlargest
# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     } 
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest)




# dict1 = {'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
# sorted_values = sorted(dict1.values())
# sorted_dict = {}

# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break

# print(sorted_dict) 
