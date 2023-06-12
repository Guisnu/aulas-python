valor = float(input("valor do produto: "))

valor_desconto10 = valor * 0.1
valor_desconto5 = valor * 0.05

forma_de_pagamento = str(input("escolha a forma de pagamento: A(avista), C(cartão) P(parcelado): "))

if(forma_de_pagamento == "A" or  forma_de_pagamento == "a"):
    resultado_final = valor - valor_desconto10
    print(f"O valor final com desconto fica: {resultado_final}")

if(forma_de_pagamento == "C" or forma_de_pagamento == "c"):
    resultado_final = valor - valor_desconto5
    print(f"O valor final do produto com desconto de cartaão fica: {resultado_final}")
        
if(forma_de_pagamento == "P" or forma_de_pagamento == "p"):
    resultado_final = valor * 1
    print(f"O valor final do produto é {resultado_final} pois em parcelamentos não há descontos")



