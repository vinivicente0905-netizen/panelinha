def dria_lista():
    # variavel "numeros" vai para a stack
    # a lista [1,2,3] vai para o heap
    numeros = [1,2,3,]
    return numeros 

resultado = criar_lista()
# a funçãp acabou, mas a lista 
# ainda existe no heap!
print(resultado) # [1,2,3]