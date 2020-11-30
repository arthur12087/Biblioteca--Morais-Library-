from funcionalidadesBiblioteca import*
usuario = "admin"
senha = "admin"

with open("livros.json","r") as read_file:
    dados = json.load(read_file)
    for d in dados:
        listaLivros.append(d)


with open("livrosReservados.json", "r") as read_file:
    informacoes = json.load(read_file)
    for i in informacoes:
        livrosReservados.append(i)


def login():
    usuarioLogin = str(input("Usuario:"))
    senhaLogin = str(input("Senha:"))
    if usuarioLogin ==usuario and senhaLogin == senha:
        menuSistema()
    else:
        print("Usuario ou senha incorreta, tente novamente!")
        login()


def menuSistema():
    print("* BEM VINDO AO MORAIS LIBRARY, A MELHOR BIBLIOTECA DA REGIÃO *\n")
    print("1 - DIGITE 1 PARA CADASTRAR UM LIVRO \n"
          "2 - DIGITE 2 PARA ATUALIZAR AS UNIDADES DE UM TÍTULO\n"
          "3 - DIGITE 3 PARA REMOVER UM TÍTULO\n"
          "4 - DIGITE 4 PARA BUSCAR POR EXEMPLARES\n"
          "5 - DIGITE 5 PARA RESERVAR OU RETORNAR UM TÍTULO\n"
          "6 - DIGITE 6 PARA OBTER STATUS DE UM LIVRO\n"
          "7 - DIGITE 7 PARA GERAR RELATÓRIO DO ACERVO\n"
          "8 - DIGITE 8 PARA GERAR RELATÓRIO POR CATEGORIA\n"
          "9 - DIGITE 9 PARA GERAR RELATÓRIO POR TEMATICA\n"
          "10 - DIGITE 10 PARA IMPORTAR UM LIVRO\n")
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

    elif respostaMenu == "4":
        buscarPorExemplares()
        menuSistema()

    elif respostaMenu == "5":
        reservarTitulo()
        menuSistema()

    elif respostaMenu == "6":
        statusLivro()
        menuSistema()

    elif respostaMenu == "7":
        relatorioAcervo()
        menuSistema()

    elif respostaMenu == "8":
        relatorioCategoria()
        menuSistema()

    elif respostaMenu == "9":
        relatorioTematica()
        menuSistema()

    elif respostaMenu == "10":
        importarLivro()
        menuSistema()

    else:
        print("Funcionalidade ainda não implementada!")
        menuSistema()

login()
