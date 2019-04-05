largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i = 1
while(i <= altura):
    j = 1
    while(j <= largura):
        print("#", end="")
        j = j + 1
    print("")
    i = i + 1
