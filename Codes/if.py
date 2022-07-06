pakistani = ["karai", "shanwari", "roosh"]
indian = ["Daal", "naan", "chana"]
Chinnese = ["Mickroni", "fried rice", "Spagetti"]

dish = str(input("Enter dish and we will tell you it's couisine\n"))

if dish in pakistani:
    print("Pakistani Cuisine")
elif dish in indian:
    print("Inidan Cuisine")
elif dish in Chinnese:
    print("Chineese Cuisine")
else:
    print("it does't belong to current cuisine")
