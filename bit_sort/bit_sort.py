def bubble_sort(ar):
    for passed in range(len(ar) - 1, 0, -1):
        for i in range(passed):
            if ar[i] > ar[i + 1]:
                temp = ar[i]
                ar[i] = ar[i + 1]
                ar[i + 1] = temp
    return ar

def bin_search(ar, n):
    bubble_sort(ar)
    low = 0
    high = len(ar) - 1

    while low <= high:
        mid = int((low + high) / 2)

        if n == ar[mid]:
            print("value", n, "is located at index of", mid)
            return 0
        elif n > ar[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return 1







            


