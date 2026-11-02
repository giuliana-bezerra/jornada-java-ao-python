class Livro:
    def __init__(self, titulo, autor, ano, disponivel=False):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self._disponivel = disponivel

    def emprestar(self):
        self._disponivel = False

    def devolver(self):
        self._disponivel = True

    def __eq__(self, livro):
        return self.titulo == livro.titulo and self.autor == livro.autor and self.ano == livro.ano

class Usuario:
    def __init__(self, nome, matricula, livros=[]):
        self.nome = nome
        self.matricula = matricula
        self._livros = livros

    def emprestar_livro(self, livro):
        livro.emprestar()
        self._livros.append(livro)

    def devolver_livro(self, livro):
        try:
            if self._livros.index(livro) >= 0:
                livro.devolver()
                self._livros.remove(livro)
        except ValueError:
            return

    def __eq__(self, usuario):
        return self.matricula == usuario.matricula

class Biblioteca:
    def __init__(self, livros=[], usuarios=[]):
        self.livros = livros
        self.usuarios = usuarios

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_livro(self, livro):
        try:
            return self.livros.index(livro)
        except ValueError:
            return -1

    def emprestar_livro(self, usuario, livro):
        if self.buscar_livro(livro) >= 0 and self.usuarios.__contains__(usuario):
            usuario.emprestar_livro(livro)

    def devolver_livro(self, usuario, livro):
        print(self.buscar_livro(livro))
        if self.buscar_livro(livro) >= 0 and self.usuarios.__contains__(usuario):
            usuario.devolver_livro(livro)

biblioteca = Biblioteca()
livro = Livro("Clean Architecture", "Robert Martin", 2008)
usuario = Usuario("Giuliana", 1)

biblioteca.adicionar_livro(livro)
biblioteca.cadastrar_usuario(usuario)

biblioteca.emprestar_livro(usuario, livro)

print(livro._disponivel)
print(usuario._livros.__len__())

biblioteca.devolver_livro(usuario, livro)

print(livro._disponivel)
print(usuario._livros)