opt = "opcao1"
while(opt !="opcao0"):
    opt = input("Digite opcao0 para sair ")
    item = ['Calça','Camisa', 'Camiseta', 'Jaqueta', 'Meia' , 'Tênis']
    item_escolhido = input("Escolha um item: \n Calça \n Camisa \n Camiseta \n Jaqueta \n Meia \n Tênis \n ")
    qnt = []
    
    for j in range():
        qnt[0] = int(input("Digite a quatidade: "))

    for i in range(qnt):
        print(item_escolhido)
        
    def opcao0():
        exit()

    def opcao1():
        print("Compra realizada com sucesso!")

    def opcao2():
        print("Adicionado ao carrinho")
        
    def opcao3():
        print("Pedido cancelado com sucesso")

    def default():
        print("Escolha uma opção válida!")
        
    if __name__ == "__main__":
        switch = {
            "Comprar": opcao1,
            "Adicionar ao carrinho": opcao2,
            "Cancelar pedido": opcao3,
            
            
        }
        
    # opt = switch.get("Comprar", default)
    # opt()