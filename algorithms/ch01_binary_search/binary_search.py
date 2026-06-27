# def binary_search(arr, item):
#     low = 0  
#     high = len(arr) - 1

#     while low <= high: 
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None 

# my_list = [1, 3, 5, 7, 9]

# print(binary_search(my_list, 3))
# print(binary_search(my_list, 2))


# def binary_search(arr, target):
#     lo = 0
#     hi = len(arr) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2
#         guess = arr[mid]
#         if  guess == target:
#             return mid
#         elif guess < target:
#             lo = mid + 1
#         else: 
#             hi = mid - 1
#     return None
    
# my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# print(binary_search(my_list, 5))

def binary_search(arr, x): # bikin fungsi binary search 
    left = 0  # indeks paling kiri dari list/array
    right = len(arr) - 1 # indeks paling kanan dari list/array

    while left <= right: # selama indeks kiri lebih kecil atau sama dengan indeks kanan 
        mid = (left + right) // 2 # menghitung indeks tengah dari list/array``


        # if[arr] # gunanya if[arr] untuk ngecek nilai tengahnya itu sama dengan nilai yang dicari atau tidak 
        if arr[mid] == x: # jika nilai tengah sama dengan nilai yang dicari
            return mid # mengembalikan indeks dari nilai yang dicari
        
        if arr[mid] < x: 
            left = mid + 1 # jika nilai tengah lebih kecil dari nilai yang dicari, maka indeks kiri digeser ke kanan
        
        else: 
            right = mid - 1 # jika nilai tengah lebih besar dari nilai yang dicari, maka indeks kanan digeser ke kiri
        
    return None 
    
my_list3 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 7

result = binary_search(my_list3, x)

if result != None:
    print("Item ditemukan pada indeks:", result)
else:
    print("Item tidak ditemukan dalam list.")





        

