bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
  ----------------------------
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
  
