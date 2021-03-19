arr = "111111111111111111111111100000000"
def firstZero(arr):
  for el in arr:
    if el == '0':
      return arr.index(el)

print(firstZero(arr))