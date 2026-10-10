# BAB 8 - Scope Variabel

x = "global"

def tes():
    x = "lokal"
    print(x)

tes()
print(x)