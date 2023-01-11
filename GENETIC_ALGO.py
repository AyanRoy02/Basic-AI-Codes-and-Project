import random 
from queue import PriorityQueue
with open('input2.txt') as fh:
    data = fh.readlines()

num,target_scr=data[0].split()
num=int(num)
target=int(target_scr)



players={}
player_list=[]

for i in data[1:]:
    temp=i.split()
    if len(temp)!=0:
        player_list+=[temp[0]]
        players[temp[0]]=int(temp[1])

def rand_select():
    list1=[]

    for i in range(int(num)):
        temp=random.randint(0,1)
        list1.append(temp)
    return list1


population=[0]*num
for i in range(num):
    population[i]=rand_select()

#SELECTION
def fitness(population):
    total_scr=[0]*num
    for i in range(num):
        for j in range(num):
            if population[i][j]==1:
                total_scr[i]+=players[player_list[j]]
    
    b_pop=[target]*num
    for i in range(num):
        temp=b_pop[i]-total_scr[i]
        if temp<0:
            temp=temp*-1
        b_pop[i]=temp

    return b_pop


def selection(population):
    total_scr=[0]*num
    for i in range(num):
        for j in range(num):
            if population[i][j]==1:
                total_scr[i]+=players[player_list[j]]

    b_pop=[target]*num
    best_population=[]
    q=PriorityQueue()
    for i in range(num):
        temp=b_pop[i]-total_scr[i]
        if temp<0:
            temp=temp*-1
        b_pop[i]=temp
        q.put((b_pop[i],i))


    if num%2==0:
        for i in range(int((num/2)+1)):
            best=q.get()
            best_population+=[population[best[1]]]
    else:
        for i in range(int((num/2)+2)):
            best=q.get()
            best_population+=[population[best[1]]]


    return best_population


        


#CROSSOVER
def crossover(best_population):
    offspring=[]
    flag=0
    for i in range(len(best_population)):
        for j in range(i+1,len(best_population)):
            a=random.randint(1,num-1)
            offspring+=[best_population[i][:a]+best_population[j][a:]]
            offspring+=[best_population[j][:a]+best_population[i][a:]]
            if len(offspring)==num:
                flag=1
                break
        if flag==1:
            break

    return offspring






#MUTATION
def mutation(offspring):

    for i in range(num):
        a=random.randint(0,num-1)
        if offspring[i][a]==0:
            offspring[i][a]=1
        else:
            offspring[i][a]=0
    return offspring
    



def genetic_algo(population):
    test=population
    flag=1
    for i in range(2000):
        best_population=selection(test)
        offspring=crossover(best_population)
        mutation(offspring)
        test=offspring
        if min(fitness(offspring))==0:
            flag=0
            break
    
    if flag==0:
        return offspring
    else:
        return -1

res=genetic_algo(population)

print(player_list)

if res==-1:
    print("-1")
else:
    ans=fitness(res)
    for i in range(num):
        if ans[i]==0:
            real_ans=res[i]
            break

    for i in real_ans:
        print(i,end="")



