# バブルソート
def bubble_sort(arr):
    arr = arr[:]
    count = len(arr)

    for i in range(count):
        for j in range(0, count - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr