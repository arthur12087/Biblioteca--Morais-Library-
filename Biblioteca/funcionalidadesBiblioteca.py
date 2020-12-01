import json
listaLivros = []
livrosReservados = []


def cadastroDeLivros():
    livro = {}

    nomeLivro = str(input("Insira o nome/título do livro: "))
    livro['titulo'] = nomeLivro

    autorLivro = str(input("insira o nome do autor da obra/livro:"))
    livro['autorLivro'] = autorLivro

    categoriaLivro = str(input("informe a categoria deste livro:"))
    livro['categoria'] = categoriaLivro

    tematicaLivro = str(input("informe a tematica deste livro:"))
    livro['tematica'] = tematicaLivro

    ano = str(input("insira o ano do livro:"))
    livro['anoLivro'] = ano

    livroAlugavel = str(input("Informe se este livro é alugável (S/N): "))
    livro['livroAlugavel'] = livroAlugavel

    livroUnidades = str(input("Quantas unidades tem deste livro? "))
    livro['livroUnidades'] = livroUnidades

    listaLivros.append(livro)

    with open("livros.json","w") as json_file:
        json.dump(listaLivros,json_file)


    print("Livro cadastrado com sucesso!")
    
    perguntaCadastro = str(input("Deseja cadastrar mais algum livro? (S/N) "))
    if perguntaCadastro.upper() == "S":
        cadastroDeLivros()


def atualizarQtdTitulo():
    nomeDoLivro = str(input("informe o livro para alteração:"))
    livroEncontrado = False
    for i in listaLivros:
        if i['titulo'] == nomeDoLivro:
            novaQuantidade = str(input("Digite a nova quantidade de unidades: "))
            i['livroUnidades'] = novaQuantidade

            salvarAlteracoes()

            print("Alteração concluída!")
            livroEncontrado = True
            break

    if livroEncontrado==False:
        print('Livro não encontrado, tente novamente!\n')


def removerTitulos():
    nomeDoLivro = input("informe o titulo do livro para excluir:")
    livroEncontrado = False
    for i in listaLivros:
        if i['titulo'] == nomeDoLivro:
            listaLivros.remove(i)
            salvarAlteracoes()
            print("Livro removido!")
            livroEncontrado = True
            break

    if livroEncontrado==False:
        print('Livro não encontrado,tente novamente!\n')


def buscarPorExemplares():
    exemplar = str(input("informe a informação que deseja buscar, seja ela ano,titulo,autor,tematica: "))
    livroEncontrado = False
    for i in listaLivros:
        if i['titulo'] == exemplar:
            print(i)
            livroEncontrado = True
            break

        if i['autorLivro'] == exemplar:
            print(i)
            livroEncontrado = True
            break

        if i['tematica'] == exemplar:
            print(i)
            livroEncontrado = True
            break

        if i['anoLivro'] == exemplar:
            print(i)
            livroEncontrado = True
            break

    if livroEncontrado==False:
        print("Livro não encontrado, tente novamente!\n")


def reservarTitulo():
    resposta = str(input("Digite (R) para reservar um titulo, ou (E) para remover um titulo da reserva:"))
    nomeLivro = str(input("Digite o nome do titulo:"))
    if resposta.upper() == "R":

        for i in listaLivros:
            if i['titulo'] == nomeLivro:
                if i['livroAlugavel'] == "S":
                    livrosReservados.append(i)

                    with open("livrosReservados.json", "w") as json_file:
                        json.dump(livrosReservados, json_file)

                    print("titulo reservado!\n")
                    break

                if i['livroAlugavel'] == "N":
                    print("este título não pode ser reservado!")
                    break


    if resposta.upper() == "E":
        livroEncontrado = False
        for j in livrosReservados:
            if j['titulo'] == nomeLivro:
                livrosReservados.remove(j)

                with open("livrosReservados.json", "w") as json_file:
                    json.dump(livrosReservados, json_file)

                print("Livro retornado da reserva!\n")
                livroEncontrado = True
                break

        if livroEncontrado==False:
            print("livro não encontrado")


def salvarAlteracoes():
    with open("livros.json", "w") as write_file:
        json.dump(listaLivros, write_file)


def importarLivro():
    print("--Para importar livros, certifique que o arquivo esteja na pasta do projeto--\n")
    nomeArquivo = str(input("digite o nome do arquivo, siga o modelo (nomeDoArquivo.json): "))
    with open(nomeArquivo, "r") as read_file:
        dados = json.load(read_file)

        listaLivros.append(dados)
        salvarAlteracoes()
        print("Importação feita!\n")


def statusLivro():
    nomeLivro = str(input("informe o livro para obter status:\n"))
    livroEncontrado = False

    for j in livrosReservados:
        if j['titulo'] == nomeLivro:
            print("** Existe uma reserva em ativa deste livro **")
            print("Há na biblioteca ", j['livroUnidades'], "unidades deste livro\n")
            livroEncontrado = True
            break

    if livroEncontrado == False:
        for i in listaLivros:
            if i['titulo'] == nomeLivro:
                print("Este livro não está reservado, está livre")
                print("Há na biblioteca,", i['livroUnidades'], "unidades disponíveis")
                livroEncontrado = True
                break


def relatorioAcervo():
    relatorio = open("relatorioAcervo.txt","w")
    relatorio.writelines("--- RELATÓRIO DO ACERVO ---\n")
    for i in listaLivros:
        relatorio.write("-" *40 + "\n")
        relatorio.write("Livro: "+ i['titulo'] + "\n" +
                        "Autor: "+ i['autorLivro'] + "\n" +
                        "Categoria: "+ i['categoria'] + "\n" +
                        "Tematica: "+ i['tematica'] + "\n" +
                        "Ano do Livro: "+ i['anoLivro'] + "\n" +
                        "Livro alugavel: "+ i['livroAlugavel'] + "\n" +
                        "Unidades: " + i['livroUnidades']+ "\n")

    print("Relatório gerado,visualize na pasta do projeto\n")
    relatorio.close()


def relatorioCategoria():
    respostaCategoria = str(input("informe a categoria: "))
    relatorio = open("relatorioPorCategoria.txt", "w")
    relatorio.writelines("--- RELATÓRIO DA CATEGORIA:" + respostaCategoria + "---\n")
    livroEncontrado = False
    for i in listaLivros:
        if i['categoria'] == respostaCategoria:
            relatorio.write("-" * 40 + "\n")
            relatorio.write("Livro: " + i['titulo'] + "\n" +
                            "Autor: " + i['autorLivro'] + "\n" +
                            "Categoria: " + i['categoria'] + "\n" +
                            "Tematica: " + i['tematica'] + "\n" +
                            "Ano do Livro: " + i['anoLivro'] + "\n" +
                            "Livro alugavel: " + i['livroAlugavel'] + "\n" +
                            "Unidades: " + i['livroUnidades'] + "\n")
            livroEncontrado = True


        if livroEncontrado == False:
            print("não existe livro com essa categoria!\n")
            break

    if livroEncontrado == True:
        print("Relatório gerado, está disponível na pasta do projeto\n")
        relatorio.close()



def relatorioTematica():
    respostaTematica = str(input("informe a tematica: "))
    relatorio = open("relatorioPorTematica.txt", "w")
    relatorio.writelines("--- RELATÓRIO DA CATEGORIA:" + respostaTematica + "---\n")
    livroEncontrado = False
    for i in listaLivros:
        if i['tematica'] == respostaTematica:
            relatorio.write("-" * 40 + "\n")
            relatorio.write("Livro: " + i['titulo'] + "\n" +
                            "Autor: " + i['autorLivro'] + "\n" +
                            "Categoria: " + i['categoria'] + "\n" +
                            "Tematica: " + i['tematica'] + "\n" +
                            "Ano do Livro: " + i['anoLivro'] + "\n" +
                            "Livro alugavel: " + i['livroAlugavel'] + "\n" +
                            "Unidades: " + i['livroUnidades'] + "\n")
            livroEncontrado = True


        if livroEncontrado == False:
            print("não existe livro com essa tematica!\n")
            break

    if livroEncontrado == True:
        print("Relatório gerado, está disponível na pasta do projeto")
        relatorio.close()
