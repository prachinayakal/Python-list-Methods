# List methods

# 1.append()
# Used for adding elements to the end of the List.
# Adds List Element as value of List.
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)

# 2.insert()
# Inserts an element at the specified position
List1 = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
List1.insert(2, 10087)
print(List1)

# 3.extend()
# Adds items of an iterable(list, array, string , etc.) to the end of a list
List2 = [1, 2, 3]
List3 = [2, 3, 4, 5]
# Add List2 to List1
List2.extend(List3)
print(List2)

# 4.reverse()
# Reverses objects of list in place
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

# 5.remove()
# The remove() method removes the specified item
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)