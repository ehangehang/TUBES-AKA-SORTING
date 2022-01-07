from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms 
from algorithms.bubbleSort import bubble_sort
from algorithms.insertionSort import insertion_sort

# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

data = []

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawDataInsertion(data, colorArray):
    canvas1.delete("all")
    canvas_width = 400
    canvas_height = 200
    x_width = canvas_width / (len(data) + 1)
    offset = 2
    spacing = 1
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 195
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas1.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawDataBubble(data, colorArray):
    canvas2.delete("all")
    canvas_width = 400
    canvas_height = 200
    x_width = canvas_width / (len(data) + 1)
    offset = 2
    spacing = 1
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 195
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas2.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

def generateData():
    global data1
    global data2

    data1 = []
    data2 = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data1.append(random_value)
        data2.append(random_value)

# This function will generate array with random values every time we hit the generate button
def generateInsertion():
    global data1

    drawDataInsertion(data1, [BLUE for x in range(len(data1))])

# This function will generate array with random values every time we hit the generate button
def generateBubble():
    global data2

    drawDataBubble(data2, [BLUE for x in range(len(data2))])

### User interface here ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# sort button 
timeTick = 0.001
b1 = Button(UI_frame, text="Sort", command=lambda:[insertion_sort(data1, drawDataInsertion, timeTick), bubble_sort(data2, drawDataBubble, timeTick)], bg=LIGHT_GRAY)
b1.grid(row=1, column=1, padx=5, pady=5)

# button for generating array 
generateData()
b3 = Button(UI_frame, text="Generate Array", command=lambda:[generateInsertion(), generateBubble()], bg=LIGHT_GRAY)
b3.grid(row=1, column=0, padx=5, pady=5)

# canvas to draw our array 
l1 = Label(window, text="Insertion Sort", bg="#FFFFFF")
l1.grid(row=1, column=0, padx=10, pady=5)
canvas1 = Canvas(window, width=400, height=200, bg=WHITE)
canvas1.grid(row=2, column=0, padx=10, pady=5)

# canvas to draw our array 
l1 = Label(window, text="Bubble Sort", bg="#FFFFFF")
l1.grid(row=3, column=0, padx=10, pady=5)
canvas2 = Canvas(window, width=400, height=200, bg=WHITE)
canvas2.grid(row=4, column=0, padx=10, pady=5)


window.mainloop()