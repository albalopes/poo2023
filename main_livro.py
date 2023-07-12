from livro import Livro

titulo = input("Digite o título do livro: ")
autor = input("Digite o nome do autor: ")
ano = input("Digite o ano de publicação: ")
livro1 = Livro(titulo, autor, ano)
print("O titulo do livro é: ", livro1.getTitulo())
print("O ano de publicação do livro é: ", livro1.getAno())
novoautor = input("Digite um novo nome para o autor do livro: ")
livro1.setAutor(novoautor)
print("O novo autor do livro é: ", livro1.getAutor())