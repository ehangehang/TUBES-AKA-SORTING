def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [25, 62, 56, 90, 37, 35, 36, 81, 94, 94, 56, 16, 22, 9, 85, 55, 48, 34, 88, 92, 99, 46, 41, 38, 21, 6, 76, 82, 52, 28, 17, 66, 18, 50, 55, 31, 83, 69, 6, 4, 8, 39, 93, 24, 31, 22, 98, 75, 100, 12]

print("Unsorted Array: ")
for i in range(len(arr)):
  print(arr[i], end=" ")

print("")
bubble_sort(arr)

print("Sorted Array (Ascending): ")
for i in range(len(arr)):
  print(arr[i], end=" ")