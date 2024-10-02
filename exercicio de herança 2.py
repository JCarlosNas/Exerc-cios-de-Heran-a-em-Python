class Animal:
     def __init__(self, nome):
         self.nome = nome

     def fazer_som(self):
         return "Som de animal"

class Cachorro(Animal):
     def __init__(self, nome, raca):
         super().__init__(nome)
         self.raca = raca

     def fazer_som(self):
         return "Au au"

animal = Animal("Genérico")
cachorro = Cachorro ("Rex", "Labrador")

print(animal.fazer_som())
print(cachorro.fazer_som())
print(f"O cachorro {cachorro.nome} é da raça {cachorro.raca}. ")




#
# class Caneta:
#     def __init__(self, material, cor):
#         self.meterial = material
#         self.cor = cor
#
#     def exibir_ação (self):
#         print("Estou funcionando")
#
# class CanetaVermelha(Caneta):
#     def __init__(self, material, cor, ponta):
#         super().__init__(material, cor)
#         self.ponta = ponta
#
#     def atividade (self):
#         print("Estou escrevendo")
#
# caneta1 = CanetaVermelha ("plástico", "vermelho", "fina")
#
# print(caneta1.atividade())
# print()