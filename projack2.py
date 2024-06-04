from time import sleep
park = {"a" : "0011817988",
        "b" : "0011817989" ,
        "c" : "0011817990" ,
        "d" : "0011825959" ,
        "e" : "0011817979" ,
        "req" : "0011628501",
        "byp" : "0010727732"}
used = []
allp = ["a" , "b" , "c" , "d" , "e"]

while True:
    x = str(input())
    if x == park["req"]:
        o = list(set(allp) - set(used))
        if(o == []):
            print("all taken lmao")
        else:
            (used.append(o[0]))
            print(used[-1])
    elif(x == park["byp"]):
        print("which one?" , used)
        dele = str(input())
        if dele not in used:
            print("its not in used")
        else:
            used.remove(dele)

    else:
        for name in park:
            idd = park[name]
            if idd == x:
                if name not in used:
                    print("how?")
                else:
                    print("remove" , name)
                    used.remove(name)
    print(used)
    sleep(1)
    if x == "0010727717":
        break;