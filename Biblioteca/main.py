from funcionalidadesBiblioteca import*

def menuSistema():
    print("* BEM VINDO AO MORAIS LIBRARY, A MELHOR BIBLIOTECA DA REGIÃO *\n")
    print("1 - DIGITE 1 PARA CADASTRAR UM LIVRO \n"
          "2 - DIGITE 2 PARA ATUALIZAR AS UNIDADES DE UM TÍTULO\n"
          "3 - DIGITE 3 PARA REMOVER UM TÍTULO\n")
    respostaMenu = str(input(""))

    if respostaMenu == "1":
        cadastroDeLivros()
        menuSistema()

    elif respostaMenu == "2":
        atualizarQtdTitulo()
        menuSistema()

    elif respostaMenu == "3":
        removerTitulos()
        menuSistema()

    else:
        print("Funcionalidade ainda não implementada!")
        menuSistema()

menuSistema()