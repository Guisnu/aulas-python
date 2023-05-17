#Escreva um programa que leia um grupo de valores(não sabemos quantos são)
#para calcular e visualizar a média desses valores e, também,
#determinar e visualizar o maior deles. Utilize uma estrutura de repetição while ou for.7

gpvalores = int (input("Digite a quantidade de números que serão calculados"))
contador = 0
valor = 0

while contador < gpvalores:
    valor += float(input("Digite um valor"))
    contador += 1

media = valor/ contador

print(media)
