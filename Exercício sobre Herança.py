class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def exibir_Informacoes(self):
        print(f"Nome: {self.nome}, Marca: {self.marca}, Preço {self.preco:.2f}")

class SmartPhone(ProdutoEletronico):
    def __init__(self, nome, marca, preco, armazenamento):
        super().__init__(nome, marca,preco)
        self.armazenamento = armazenamento

    def exibir_Informacoes(self):
        super().exibir_Informacoes()
        print(f"Capacidade de armazenamento: {self.armazenamento}GB")

class Laptop(ProdutoEletronico):
        def __init__(self, nome, marca ,preco,memoria_ram):
            super().__init__(nome,marca,preco)
            self.memoria_ram = memoria_ram

        def exibir_Informacoes(self):
            super().exibir_Informacoes()
            print(f"Memoria RAM: {self.memoria_ram}GB")

class Televisor(ProdutoEletronico):
    def __init__(self, nome, marca,preco, tamanho ):
        super().__init__(nome, marca, preco)
        self.tamanho = tamanho

    def exibir_Informacoes(self):
        super().exibir_Informacoes()
        print(f"Tamanho da Tela: {self.tamanho} polegadas")

loja = ProdutoEletronico
smartphone = SmartPhone ("Iphone 13", "Apple", 5999.99, 256)
laptop = Laptop ("MacBook Pro", "Apple", 8999.99, 16)
televisão = Televisor("Smart TV 4K", "Samsung", 3499.99,55)

print(smartphone.nome, smartphone.marca, smartphone.preco, smartphone.armazenamento )
print(laptop.nome, laptop.marca,laptop.preco,laptop.memoria_ram)
print(televisão.nome,televisão.marca, televisão.preco, televisão.tamanho)

#
# class CameraDigital(ProdutoEletronico):
#     def __init__(self, nome, marca,preco, resolucao):
#         super().__init__(nome, marca, preco)
#         self.resolucao = resolucao
#
#     def exibir_Informacoes(self):
#         super().exibir_Informacoes()
#         print(f"resolucao: {self.resolucao} PX")
#
# cameraDigital = CameraDigital ("alpha A7C", "Soni",13525.00,24)
#
# cameraDigital.exibir_Informacoes()
# print(cameraDigital.nome, cameraDigital.marca, cameraDigital.preco)

