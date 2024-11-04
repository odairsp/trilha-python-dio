import datetime


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.datetime = datetime.datetime.now()
        print("Inicializando Classe...")
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Bicicleta parada.")

    def correr(self):
        print("Bicicleta correndo.")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}:\n\t{''.join([
            f'{chave}'.ljust(8) + ' = ' + f'{valor}\n\t'.rjust(12) for chave, valor in self.__dict__.items()
            ])}"

    def __del__(self):
        print("Excluindo Classe...")
        print(
            datetime.timedelta(self.datetime).microseconds
            - datetime.datetime.now().microsecond
        )


caloi = Bicicleta("vermelha", "caloi", 2024, 1600)

print(caloi)