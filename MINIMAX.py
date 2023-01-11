import math
import random
#old_id="19201043"
old_id=input("Enter your Student ID: ")
min_p=0
max_p=0
win_point=0
s=0
id=""

#TASK 01

for i in old_id:
        if i=="0":
            id+="8"
        else:
            id+=i

for i in range(len(id)):
    if i==3:
        s=int(id[i])
    elif i==4:
        min_p=int(id[i])
    elif i==6:
        temp=""
        temp+=id[i+1]+id[i]
        win_point=int(temp)
        max_p=win_point*1.5


rp = [random.randrange(int(min_p),int(max_p)) for x in range(8)]

print(f"TASK 01:\nminimum_num {min_p},maximum_num {max_p},winning point {win_point},shuffle {s}")


neg_inf=-math.inf
pos_inf=math.inf


def minimax(depth, score, maximizingPlayer, alpha, beta, position):
  

    if depth == 0:
        return score[position]
 
    if maximizingPlayer:
      
        maxEval = neg_inf
 
        for i in range(2):
          eval=minimax(depth-1,score,False,alpha,beta,(position*2)+i)
          maxEval=max(maxEval,eval)
          alpha=max(alpha,maxEval)
 
          if beta <= alpha:
            break
          
        return maxEval
      
    else:

        minEval = pos_inf
 
        for i in range(2):
          eval=minimax(depth-1,score,True,alpha,beta,(position*2)+i)
          minEval=min(minEval,eval)
          beta=min(beta,minEval)
 
          if beta <= alpha:
            break
          
        return minEval



ans=minimax(3,rp,True,neg_inf,pos_inf,0)
print(f"Generated 8 random points between the minimum and maximum point: {rp}\nTotal points to win: {win_point}\nAchieved point by applying alpha-beta pruning {ans}")
if ans>=win_point:
  print("The winner is Optimus Prime")
else:
  print("The winner is Megatron")


#TASK 02

print("\nTASK 02:")

ans_list=[]
for i in range(s):
  random.shuffle(rp)
  ans=minimax(3,rp,True,neg_inf,pos_inf,0)
  ans_list+=[ans]

won=0
for i in ans_list:
  if i>=win_point:
    won+=1

print(f"After the shuffle:\nList of all points values from each shuffles: {ans_list}\nMaximum value: {max(ans_list)}\nWon {won} times out of {s} number of shuffles")
