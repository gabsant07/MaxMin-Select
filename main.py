def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        min_idx = i
        

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [23, 5, 1, 18, 99, 3]
    
    print("Array Original: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Array Final: ", end="")
    print_array(arr)