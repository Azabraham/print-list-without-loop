def displayList(list_in_question, val=0):
    if val==len(list_in_question):
        return
    else:
        if type(list_in_question[val])==list:
            displayList(list_in_question[val])
        else:
            print(list_in_question[val]) # or append to new list
        return displayList(list_in_question, val+1)

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, [10, 11], 12, [13, [14], 15, [16, [17]], 18], [[[19], 20, [21, [22]], 23, [24], 25, 26], 27], 28]

displayList(list1)