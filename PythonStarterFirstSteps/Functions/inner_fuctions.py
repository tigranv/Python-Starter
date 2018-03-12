
def outer_function():
    def inner_function():
        print("inner function")

    print("outer function")
    inner_function()

outer_function()

print("--------------------------global variables............")

var = "Global variable"

def function():
    print(var)

function()

print("--------------------------global variables............")

var1 = "Global variable"

def function():
    var1 = "local variable"
    print(var1)

function()
print(var1)

print("-------------------------- change global variables............")

var2 = "Global variable"

def function():
    global var2
    var2 = "local variable"
    print(var2)

function()
print(var2)