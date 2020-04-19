class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciana = Pessoa(renzo, nome='Luciana')

    print(Pessoa.cumprimentar(luciana))
    print(id(luciana))
    print(luciana.cumprimentar())
    print(luciana.nome)
    print(luciana.idade)
    print()
    for filho in luciana.filhos:
        print(filho.nome)