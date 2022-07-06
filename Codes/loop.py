'''
months = ["January", "February", "March", "April", "May"]
exp = [1233, 4342, 3243, 4342, 1232]
total = 0

for i in range(len(exp)):
    print("Month = ", months[i], "\t", "Expense ", exp[i])
    total = total + exp[i]
print("Total expense is " , total)
'''
'''
keyLocation = "chair"
locations = ["desk", "Underbed", "shelf", "chair", "window", "table"]

for i in locations:
    if i == keyLocation:
        print("Key is found in " , i)
        break 
    else:
        print("Key is not found in " , i)
'''
'''
for i in range(1,6):
    if i%2 == 0:
        continue
    else:
     print(i*i)
'''
'''
i = 1
j = 10 
while i <= j:
    print(i)
    i = i + 1
'''    