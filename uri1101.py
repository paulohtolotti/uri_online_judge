def validateInput(a,b):
    if a>b:
        return b,a
    else:
        return a,b

while True:
    m = int(input())
    n = int(input())
    if (m <=0 or n<=0):
        break
    else:
        m,n = validateInput(m,n)
        for i in range(m,n+1):
            print(i)
        soma = sum(n for n in range(m,n+1))
        print(f"Sum={soma}")
