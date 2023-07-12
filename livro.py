class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getAno(self):
        return self.ano

    def setAno(self, ano):
        self.ano = ano