from queue import PriorityQueue
from turtle import distance
with open('input1.txt') as fh:
    data = fh.readlines()



city={}
neighbor={}
dis={}
prev={}


for i in data:
    j=i.split()
    city[j[0]]=j[1]
    dis[j[0]]=0
    prev[j[0]]=0
    new_list=[]
    for k in range(2,len(j)):
        if k%2 == 0:
            new_list+=[[j[k],j[k+1]]]
        neighbor[j[0]] = new_list





def A_star(start,neighbor,h,d,prev,goal):
    q=PriorityQueue()
    visited=[]
    q.put((int(h[start]),start))
    while not q.empty():
        u=q.get()
        
        visited+=[u[1]]
        
        if u[1]==goal:
            break
        for i in neighbor[u[1]]:
            new_dis=int(i[1])+d[u[1]]
           
            if new_dis<d[i[0]] or d[i[0]]==0:
                prev[i[0]]=u[1]
                q.put((new_dis+int(h[i[0]]),i[0]))
                d[i[0]]=new_dis
            
    list1=[goal]
    iter=goal
    exists=0
    while(True):
        temp=prev[iter]
        list1+=[temp]
        iter=temp
        if temp==start:
            break
        exists+=1
        if exists>100:
            print("NO PATH FOUND")
            return -1

    return [list1[::-1],d[goal]]



ans=A_star("Arad",neighbor,city,dis,prev,"Bucharest")

if ans!=-1:
    print("Path:",end=" ")
    for i in ans[0]:
        
        
        if i=="Bucharest":
            print(i)
        else:
            print(i,"---->",end=" ")

    print("Total Distance: ",ans[1],"km" )

