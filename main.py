import random

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 1]

def sigmoid(x):
    return 1 / (1 + 2.718281828459045 ** -x)

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
    return list(map(float, strArray.strip('[]').split(',')))

learning_rate = 0.1
cost = float('inf')

while cost > 0.01:  # Train until cost is sufficiently low
    cost = sum((sigmoid(X[i][0]*weights[0][0] + X[i][1]*weights[1][1] + biases[0]) - y[i])**2 for i in range(len(X))) / len(X)
    
    for i in range(len(X)):
        prediction = sigmoid(X[i][0]*weights[0][0] + X[i][1]*weights[1][1] + biases[0])
        error = prediction - y[i]
        weights[0][0] -= learning_rate * error * X[i][0]
        weights[1][1] -= learning_rate * error * X[i][1]
        biases[0] -= learning_rate * error


test_input = str2array(input())

output = test_input[0]*weights[0][0] + biases[0] + test_input[1]*weights[1][1] + biases[1]
output_activation = sigmoid(output)

print(1 if output_activation >= 0.5 else 0)
