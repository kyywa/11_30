#Jancsurák Bence

for i in range(1,10):
    print("{} -- {}".format(i,1/i))

print("Az eredmény: {}".format(int(input("Adja meg a hatvány értékét: "))**int(input("Adja meg a hatvány kitevőjét: "))))

while True:
    num = int(input("Írjon be egy számot: "))
    if num<0:
        print("Knock it off with them negative waves")
    else:
        print("Siker!")
        break