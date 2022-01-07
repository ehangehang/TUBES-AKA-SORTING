import time

from colors import *

def bubble_sort(data, drawDataBubble, timeTick):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawDataBubble(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                time.sleep(timeTick)
    drawDataBubble(data, [BLUE for x in range(len(data))])