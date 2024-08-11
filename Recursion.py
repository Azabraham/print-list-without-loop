def recurse(list1, index):
  if index == 0:
    return
  else:
    length = len(list1)
    if type(list1[length-index]) == list:
      leng = len(list1[length-index])
      recurse(list1[length-index], leng)
    else:
      print(list1[length-index]) # or append to a new list
    return recurse(list1, index-1)

MegaList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12], 13, 14, 15, 16, [17], 18, [[19], 20, [21, [22]], 23, [24]], 25]

length = len(MegaList)

recurse(MegaList, length)
