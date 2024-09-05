import json
from statistics import mean

def analyze_faturamento(data):

    faturamento_dias = [dia['valor'] for dia in data if dia['valor'] > 0]
    
    if not faturamento_dias:
        return "Não há dados de faturamento válidos."

    menor_valor = min(faturamento_dias)
    maior_valor = max(faturamento_dias)
    media_mensal = mean(faturamento_dias)
    
    dias_acima_media = sum(1 for valor in faturamento_dias if valor > media_mensal)

    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media
    }


try:
    with open('dados.json', 'r') as file:
        dados_faturamento = json.load(file)
except FileNotFoundError:
    print("Arquivo 'dados.json' não encontrado.")
    exit(1)
except json.JSONDecodeError:
    print("Erro ao decodificar o arquivo JSON.")
    exit(1)

resultado = analyze_faturamento(dados_faturamento)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"Menor valor de faturamento: R$ {resultado['menor_valor']:.2f}")
    print(f"Maior valor de faturamento: R$ {resultado['maior_valor']:.2f}")
    print(f"Número de dias acima da média mensal: {resultado['dias_acima_media']}")
