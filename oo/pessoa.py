class Pessoa:
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



