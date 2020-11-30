import pandas as pd

afn = {}
n = int(input("Estados: "))               
t = int(input("Transições/alfabeto: "))   
for i in range(n):  
    estado = input("Nome do estado: ")         
    afn[estado] = {}                             
    for j in range(t):
        caminho = input("Transicao: ")             
        print("estado final a partir do estado {} pelo caminho {}:".format(estado,caminho))
        estado_alcancado = [x for x in input().split()]  
        afn[estado][caminho] = estado_alcancado        

print("\nAFN :\n")
print(afn)                                      
print("\nAFN: ")
tabela_afn = pd.DataFrame(afn)
print(tabela_afn.transpose())

print("estado final da AFN : ")
afn_estado_final = [x for x in input().split()]              
    
lista_novos_estados = []                          
afd = {}                                      
lista_chaves = list(list(afn.keys())[0])     
lista_caminhos = list(afn[lista_chaves[0]].keys())    

afd[lista_chaves[0]] = {}                      
for y in range(t):
    var = "".join(afn[lista_chaves[0]][lista_caminhos[y]])   
    afd[lista_chaves[0]][lista_caminhos[y]] = var            
    if var not in lista_chaves:                         
        lista_novos_estados.append(var)                  
        lista_chaves.append(var)                        

while len(lista_novos_estados) != 0:                     
    afd[lista_novos_estados[0]] = {}                     
    for _ in range(len(lista_novos_estados[0])):
        for i in range(len(lista_caminhos)):
            temp = []                                
            for j in range(len(lista_novos_estados[0])):
                temp += afn[lista_novos_estados[0][j]][lista_caminhos[i]]  
            s = ""
            s = s.join(temp)                         
            if s not in lista_chaves:                   
                lista_novos_estados.append(s)            
                lista_chaves.append(s)                  
            afd[lista_novos_estados[0]][lista_caminhos[i]] = s   
        
    lista_novos_estados.remove(lista_novos_estados[0])       

print("\nAFD: \n")    
print(afd)                                           
print("\nTabela AFD ")
tabela_afd = pd.DataFrame(afd)
print(tabela_afd.transpose())

afd_lista_estados = list(afd.keys())
afd_estados_finais = []
for x in afd_lista_estados:
    for i in x:
        if i in afn_estado_final:
            afd_estados_finais.append(x)
            break
        
print("\nEstados finais do afd: ",afd_estados_finais)
