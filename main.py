import numpy

# Entry point
if __name__ == '__main__':
    print('Hy, PyCharm')

# Loops
print("\"for\" loop:")
for i in range(10):  # From 0 to 9
    print(i)

print("\"for\" loop with array:")
arr = ["one", "two", "three"]
for e in arr:
    print(e)

print("while loop:")
i = 1
while i < 6:
    print(i)
    i += 1


def function(arg):
    function_message = "message in a function: " + arg
    print(function_message)


print("function invocation:")
function("arg")


def function(*args):
    for x in args:
        print(x)


print("function with non-fixed number of arguments:")
function("one", "two", "three")


print("examples for types in python:")
x = str(3)
y = int(3)
z = float(3)
print(type(x))
print(type(y))
print(type(z))
