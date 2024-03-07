from toanhoc import toanhoc

t = toanhoc()
uocchungmax = t.gcd(125,15)
print(uocchungmax)
print("================================")

if t.isPrime(17):
    print("Là số nguyên tố..")
else:
    print("Không là số nguyên tố..")
print("================================")

l = t.extendedEuclid(127,19)
print("UCLN là: " + str(l[0]))
print("x và y: " + str(l[1]) + " " +str(l[2]))

