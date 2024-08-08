import matplotlib.pyplot as plt

# Dados
produtos = ['Cerveja Brahma', 'Pão Francês', 'Urarana Antártica']
quantidade = [6, 6, 2]
preco_unitario = [3.99, 0.75, 7.99]
valores_totais = [q * p for q, p in zip(quantidade, preco_unitario)]

# Dimensões da figura
plt.figure(figsize=(774.35/100, 270/100))  # Convertendo de pixels para polegadas

# Criar gráfico de barras
plt.bar(produtos, valores_totais, color=['gold', 'lightcoral', 'skyblue'])

# Adicionar títulos e rótulos
plt.title('Total por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor Total (R$)')

# Adicionar valores no gráfico
for i, valor in enumerate(valores_totais):
    plt.text(i, valor + 0.2, f'R$ {valor:.2f}', ha='center', va='bottom')

# Exibir gráfico
plt.tight_layout()
plt.show()