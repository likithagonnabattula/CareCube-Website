def minimumVehicles(Weights, max_limit):
    sorted_weights=sorted(filter(lambda x:x!=0,Weights),reverse=True)
    left,right = 0,len(sorted_weights)-1
    vehicles = 0
    while left<=right:
        if sorted_weights[left]+sorted_weights[right]<=max_limit:
            right-=1
        left+=1
        vehicles+=1
    return vehicles
Weights = list(map(int, input().split()))
max_limit=int(input())
Answer = minimumVehicles(Weights,max_limit)
print(Answer,end="")