def take():
    inpt = str(input("Do yoy want to add dic (y/n)"))
    if inpt == "y":
        dict()
        take()
    else:
        return

def dict(): 
    name = str(input("add dic name: "))
    number = int(input("Enter number : "))
    d[name] = number
    print(d)


d = {"usman":232434234, "tayyab":827382733, "ayyan":123213441 }
take()

# for k, v in d.items():
#     print("Keys", k , "values", v)

# if "usman" in d:
#     print(True) 

# d.clear()
# print(d)

# point = (3, 4)
# print(point[0])