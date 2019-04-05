#FUNÇÕES
def Minimo(temp):
    min = temp[0]
    for i in temp:
        if (i < min):
            min = i
    return min

def Maximo(temp):
    max = temp[0]
    for i in temp:
        if (i > max):
            max = i
    return max

def MinMax(temp):
    print('A menor temperatura encontrada:', Minimo(temp),'ªC')
    print('A maior temperatura encontrada:', Maximo(temp),'ªC')

#INÍCIO DO PROGRAMA 
print("*************************************************************************")      
print("                      MINIMO E MAXIMO DE TEMPERATURAS                    ")
print("*************************************************************************\n")       
mylist = [] 
for i in range(9):
    userInput = input( "Digite a temperatura: ")
    userInput = int(userInput)
    mylist.append(userInput)
print("\n*************************************************************************\n") 
MinMax(mylist) 
print("\n\n")  
