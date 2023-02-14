#smallest element in array
arr = [2,8,9,6,5,3,8,1]
mini = arr[0]
for i in range(len(arr)):
    if arr[i]<mini:
        mini = arr[i]

print(mini)        


print("______________________________")
#smallest element in array
arr = [10,50,90,50,10,9,87,5]
arr.sort()

print(arr[0])

print("___________largest element in array ______________________")
#initialize array
arr = [44,77,88,99,22,4,6,1,2]

#initialize max with first element of array
max = arr[0]

#loop through the array

for i in range(0,len(arr)):

#compare elements of array with max
    if (arr[i]>max):
        max = arr[i]
print("largest element present in given array",max)             



