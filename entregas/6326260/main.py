
from mod_estoque import cadastrar_item, calcular_valor_estoque, listar_itens_em_falta


def main():
    # Cadastrando alguns itens de teste
    estoque = [
        cadastrar_item("Teclado", 10, 150.0),
        cadastrar_item("Mouse", 3, 80.0),
        cadastrar_item("Monitor", 2, 900.0),
        cadastrar_item("Cabo HDMI", 15, 25.0),
    ]

    # Calculando valor total do estoque
    valor_total = calcular_valor_estoque(estoque)
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    # Verificando produtos abaixo da quantidade minima (ex: 5)
    limite_minimo = 5
    itens_baixo = listar_itens_em_falta(estoque, limite_minimo)

    print(f"\nItens com estoque abaixo de {limite_minimo}:")
    for item in itens_baixo:
        print(f"- {item['nome']}: {item['quantidade']} unidades")


if __name__ == "__main__":
    main()