counter = 0
num_a = int(input("Adjon meg egy számot"))
for i in range(2,num_a):
    if num_a%i == 0:
        counter= counter + 1
if counter>0:
    print("{} nem prím szám".format(num_a))
else:
    print("{} prím szám".format(num_a))
    