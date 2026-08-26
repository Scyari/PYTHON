


n = 153
t = n
s = 0
p = len (str(n))

while t > 0:
    d = t % 10
    s+= d**p
    t//=10
    if s == n:
        print (n, "is an Armstrong number")
    else:
        print (n, "is not an Armstrong number")
