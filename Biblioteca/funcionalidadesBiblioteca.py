informacoesLivro = []
def cadastroDeLivros():

    nomeLivro = str(input("Insira o nome/título do livro: "))
    autorLivro = str(input("insira o nome do autor da obra/livro"))
    identificacao = str(input("insira o ID do livro"))
    numeroEdicao = str(input("informe o numero da edição do livro"))
    livroAlugavel = str(input("Informe se este livro é alugável (S/N): "))
    livroUnidades = int(input("Quantas unidades tem deste livro? "))

    informacoesLivro.append(nomeLivro)
    informacoesLivro.append(autorLivro)
    informacoesLivro.append(identificacao)
    informacoesLivro.append(numeroEdicao)
    informacoesLivro.append(livroAlugavel)
    informacoesLivro.append(livroUnidades)

    print("Livro cadastrado com sucesso!")
    perguntaCadastro = str(input("Deseja cadastrar mais algum livro? (S/N) "))
    if perguntaCadastro.upper() == "S":
        cadastroDeLivros()

def atualizarQtdTitulo():
    informacoesLivro.pop(5)
    novaQuantidade = int(input("Digite a nova quantidade de unidades: "))
    informacoesLivro.insert(5,novaQuantidade)
    print("Alteração concluída!")

def removerTitulos():
    informacoesLivro.clear()
    print("Livro removido!")

