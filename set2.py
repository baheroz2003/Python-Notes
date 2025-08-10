thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
The return value of the pop() method is the removed item.
Example
Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
