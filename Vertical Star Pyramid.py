a = ""

for i in range(15):
    a += "*"
    print(a)
for i in range(15):
    b = a[:-1]
    print(b)
    a = b