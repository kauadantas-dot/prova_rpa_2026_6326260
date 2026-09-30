def main():
    ENDPOINT_URL: str = "https://api.faturamento.com/v1"
    PORTA: int = 8080
    TAXA_AMOSTRAGEM: float = 1.5
    USA_HTTPS: bool = True

    parametros = {
        "ENDPOINT_URL": ENDPOINT_URL,
        "PORTA": PORTA,
        "TAXA_AMOSTRAGEM": TAXA_AMOSTRAGEM,
        "USA_HTTPS": USA_HTTPS,
    }

    print("=== RELATÓRIO DE VALIDAÇÃO DE PARÂMETROS ===")
    for chave, valor in parametros.items():
        print(f"Parâmetro: {chave:<15} | Valor: {valor:<32} | Tipo: {type(valor)}")


if __name__ == "__main__":
    main()
