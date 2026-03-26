import random

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 1]

weights = [
    [random.uniform(-2, 2), random.uniform(-2, 2)],
    [random.uniform(-2, 2), random.uniform(-2, 2)],
    [random.uniform(-2, 2), random.uniform(-2, 2)],
    [random.uniform(-2, 2), random.uniform(-2, 2)],
]
biases = [
    random.uniform(-2, 2),
    random.uniform(-2, 2),
    random.uniform(-2, 2),
    random.uniform(-2, 2)
]

def str2array(strArray):
    # YASH: input ko string se array me convert kar
    # for example maine '[1, 1]' enter kiya to test input '[1, 1]' ki string hogi to usko [1, 1] aaray me convetr kar
    pass

test_input = str2array(input())

output = test_input[0]*weights[0][0] + biases[0] + test_input[1]*weights[1][1] + biases[1]
print(output)
