
def findDistance(target_index,l1:list):
    min_value=len(l1)
    for i in range(target_index-1,-1,-1):
        index = i
        distance = (target_index-1)-i
        if l1[i] in l1 and i!=l1.index(l1[i]):
            index = l1.index(l1[i])
        total_distance = distance+index+1
        if  total_distance < min_value:
            min_value = total_distance
    print("total distance ==> "+str(min_value))



length = int(input("Enter Length Of The List :"))
l1=[]
for i in range(0,length):
    data = input(f"Enter element position{i+1}:")
    l1.append(data)
target_index =  int(input("Enter target index::"))
findDistance(target_index, l1)
        
