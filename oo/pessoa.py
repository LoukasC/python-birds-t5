class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    lucas = Pessoa(nome = 'Lucas')
    arthur = Pessoa(lucas, nome = 'Arthur')
    print(Pessoa.cumprimentar(arthur))
    print(id(arthur))
    arthur.cumprimentar()
    print(arthur.nome)
    print(arthur.idade)
    for filho in arthur.filhos:
        print(filho.nome)
        arthur.sobrenome = 'Okamura'
        del arthur.filhos
        arthur.olhos = 1
        del arthur.olhos
        print(arthur.__dict__)
        print(lucas.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(arthur.olhos)
        print(lucas.olhos)
        print(id(Pessoa.olhos)), id(arthur.olhos), id(lucas.olhos)


