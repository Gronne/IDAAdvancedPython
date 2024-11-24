



func_a = lambda: "Hello"
print(func_a())

func_a2 = lambda: print("There")
func_a2()

func_b = lambda number: number*2
print(func_b(10))

func_c = lambda value_a, value_b: value_a + value_b
print(func_c(8, 6))


def multiplier_func(multiplier: float):
    return lambda value: value*multiplier

double_multiplier = multiplier_func(2)
print(double_multiplier(15))


def do_something(function_to_call):
    print("Before")
    name="Mathias"
    function_to_call(name)
    print("After")

def print_name(name):
    print(name)

do_something(lambda name: print_name(name))