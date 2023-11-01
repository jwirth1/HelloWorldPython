weight = int(input("Weight: "))
type = input("(K)g or (L)bs: ")
if type.upper() == "K":
    converted = weight / .45
    print("Weight in Lbs: "+str(converted))
else:
    converted=weight*.45
    print("Weight in Kgs: "+str(converted))
