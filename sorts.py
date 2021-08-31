"""
Description: This program contains a number of sorting algorithms
Author: Maya Krolik
Date: August. 2021
"""

def customSort(x): #'backwards' bubble sort
    h = 1
    for i in range (0, l-1):
        for j in range (1, l):
            if x[j] > x[j-h]: #if the card on the left is larger than the card on the right
                x[j], x[j-h] = x[j-h], x[j] #swap
            h+=1
    #not done
    return x

def bubbleSort(x): #large values 'bubble up' to end of list
    for i in range(l-1): #for cards in entire range of list (0, l-1)
        for j in range(l-i-1): #iterate for each card below first card (0, i-1)
            if x[j] > x[j+1]: #if the card on the left is smaller than the card on the right
                x[j], x[j+1] = x[j+1], x[j] #swap
                #numberOfSwaps += 1
                #tmp = x[j]
                #x[j] = x[j+1]
                #x[j+1] = x[j]
    return x

def insersionSort(x):
    """
    the first itiration will check the second card with the first, the next itiration will
    check the second card with the second card, then second with third card and so on untill the
    second card has been checked with all cards in the list and is in the right spot. The process
    repeats with the third card and so on.
    """
    for i in range(1, l): #for all cards besides first one in list
        for j in range(0, l): #all cards in list
            if (x[i] < x[j]):
                x[j], x[i] = x[i], x[j]
    return x

def insersionSortWhileLoop():
    for i in range(1, l):
  
        key = x[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < x[j] :
                x[j+1] = x[j]
                j -= 1
        x[j+1] = key

def selectionSort(x):
    for i in range(l):
        min_idx = i
        for j in range(i+1, l):
            if x[j] < x[min_idx]:
                #min_idx = j
                x[j], x[min_idx] = x[min_idx], x[j]
    return x
    # for i in range(l):
    #     min_indx = 0
    #     for j in range (min_indx, l):
    #         if (x[i] < x[min_indx]):
    #             x[i], x[min_indx] = x[min_indx], x[i]
    #     if x[i] < x[min_indx] :
    #         min_indx = i  

def mergeSort():
    print("placeholder")

if __name__ == "__main__":
    from random import shuffle
    from time import time

    N = 10
    x = []
    listCopy = []
    for i in range(N):
        x.append(i)
        listCopy.append(i)

    shuffle(x)
    print(x)

    l = len(x)
    t1 = time()
    shuffle(x)
    selectionSort(x)

    t2 = time()
    shuffle(x)
    insersionSort(x)

    t3 = time()
    shuffle(x)
    bubbleSort(x)

    t4 = time()
    shuffle(x)
    x.sort()
    t5 = time()

    #customSort(x, numberOfSwaps)
    print("Selection Sort time %.10f seconds" %(t2-t1))
    print("Insersion Sort time %.10f seconds" %(t3-t2))
    print("Bubble Sort time %.10f seconds" %(t4-t3))
    print("Python Sort time %.10f seconds" %(t5-t4))
    print(x)
    #assert x == listCopy
    #print(listCopy)
    #print("number of swaps %d" %numberOfSwaps)