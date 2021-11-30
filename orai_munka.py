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

num_a = int(input("Adja meg az első számot: "))
num_b = int(input("Adja meg az második számot: "))
print("{} és {} távolsága a számegyenesen: {}".format(num_a,num_b,abs(num_a-num_b)))

osszeg = 0
while osszeg<100:
    osszeg += int(input("Adjon meg egy számot: "))
    print("Az összeg {}".format(osszeg))