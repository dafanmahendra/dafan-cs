def findSmallest(arr):
    smallest = arr[0] # Stores the smallest value
    smallest_index = 0 # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    copiedArr = list(arr) # 
    for i in range(len(copiedArr)):
                   smallest = findSmallest(copiedArr)
                   newArr.append(copiedArr.pop(smallest))
    return newArr

print(selection_sort([5, 3, 6, 2, 10, 19, 1, 4, 8, 12, 7, 11, 13, 70]))
            
                