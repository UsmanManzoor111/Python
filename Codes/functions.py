# tomExp = [1200, 100, 200]
# joeExp = [100, 400, 300]

# def calculateExp(exp):
#     total = 0
#     for i in exp:
#         total = total + i

#     return total

# print("tom exp :" , calculateExp(tomExp))

def sum(a = 0, b = 0): # if you don't pass the argument i will autmatically assign it 0
    print("a : ", a, "\nb : ", b)
    total = a + b
    return total

print("sum : ", sum(34))