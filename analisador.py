# Lista de imóveis: [Bairro, Preço, Tamanho m²]
imoveis = [
    ["Petrópolis", 250000, 60],
    ["Adrianópolis", 450000, 80],
    ["Petrópolis", 210000, 65],  # Este vai ser a nossa oportunidade!
    ["Centro", 300000, 70],
    ["Ponta Negra", 600000, 100]
]

# Definindo o que é um preço bom (exemplo: abaixo de R$ 3.500/m²)
LIMITE_OPORTUNIDADE = 3500

print("--- ANÁLISE DE MERCADO: BUSCA DE OPORTUNIDADES ---")

for imovel in imoveis:
    bairro, preco, tamanho = imovel
    preco_m2 = preco / tamanho
    
    # Lógica de decisão (Aqui entra o cientista de dados!)
    if preco_m2 < LIMITE_OPORTUNIDADE:
        status = "🔥 OPORTUNIDADE DETECTADA!"
    else:
        status = "Preço Normal"
        
    print(f"Bairro: {bairro:<15} | m²: R${preco_m2:>8.2f} | Status: {status}")