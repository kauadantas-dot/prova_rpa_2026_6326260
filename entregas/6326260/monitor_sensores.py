# Questao 2 - Monitoramento de Sensores
leituras = [36.5, 41.2, 38.0, 105.0, 37.4, -999.0, 39.1, 40.0]


def monitorar(lista):
    soma = 0.0
    qtd = 0

    for leitura in lista:
        # Se for maior que 80, descarta e pula pro proximo
        if leitura > 80.0:
            print(f"[DESCARTE] Leitura de {leitura}°C fora da faixa: ignorada.")
            continue

        # Se for -999, eh erro no sensor e para o loop
        if leitura == -999.0:
            print(f"[FALHA] Sensor corrompido ({leitura}). Interrompendo monitoramento...")
            break

        # Se passou pelas validacoes, acumula os dados
        print(f"[OK] Leitura de {leitura}°C registrada.")
        soma += leitura
        qtd += 1

    # Calcula a media se tiver pelo menos 1 item valido
    if qtd > 0:
        media = soma / qtd
    else:
        media = 0.0

    print("\n--- RESUMO ---")
    print(f"Quantidade de leituras validas: {qtd}")
    print(f"Media das leituras validas: {media:.2f}°C")


if __name__ == "__main__":
    monitorar(leituras)