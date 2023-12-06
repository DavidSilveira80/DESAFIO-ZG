"""
Pergunta: P4 - As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, 
e R$ 1,00 se forem compradas pelo menos 12. Escreva um algoritmo (sequência de passos)
que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
"""

# Declarei as constantes
MACAS_MENOS_DE_UMA_DUZIA: float = 1.30
MACAS_A_PARTIR_DE_UMA_DUZIA: float = 1.00


# defini a função que troca de ponto para virgula, para valores Brasileiros
def substiui_ponto_por_virgula(valor: float) -> str:
    valor_string = f'{valor:.2f}' 
    return valor_string.replace('.', ',')

# Defini a funçao com a lógica do custo das maçãs
def custo_macas(macas: int) -> str:
    if 0 < macas < 12:
        calculo1 = macas * MACAS_MENOS_DE_UMA_DUZIA
        return f'Valor total das {macas} maçãs é de {substiui_ponto_por_virgula(calculo1)} R$.'
    else:
        calculo1 = macas * MACAS_A_PARTIR_DE_UMA_DUZIA
        return f'Valor total das {macas} maçãs é de {macas * MACAS_A_PARTIR_DE_UMA_DUZIA:.2f} R$.'

# Fiz uso de type hints tanto para variáveis, parâmetros e saída de função   
# Chamada da função com a lógica principal
if __name__ == "__main__":
        print(custo_macas(10))
        print(custo_macas(24))
        