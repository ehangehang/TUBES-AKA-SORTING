import time

from colors import *

def insertion_sort(data, drawDataInsertion, timeTick):
    i = 1
    n = len(data)
    while i < n:
        key = data[i]
        j = i-1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
            drawDataInsertion(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
            time.sleep(timeTick)
        data[j+1] = key
        i += 1
    drawDataInsertion(data, [BLUE for x in range(len(data))])