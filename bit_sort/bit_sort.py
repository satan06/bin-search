def bubble_sort(ar):
    for passed in range(len(ar) - 1, 0, -1):
        for i in range(passed):
            if ar[i] > ar[i + 1]:
                temp = ar[i]
                ar[i] = ar[i + 1]
                ar[i + 1] = temp
    return ar



            


