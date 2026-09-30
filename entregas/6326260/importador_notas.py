import logging
import pandas as pd

# Configuração simples do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("importacao.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def importar_notas(caminho: str) -> float:
    """Importa notas do CSV e calcula o total."""
    try:
        # Lendo o CSV
        df = pd.read_csv(caminho)

        # Log de cada linha do arquivo
        for _, linha in df.iterrows():
            logging.info(
                f"Nota: {linha['nota']} | Cliente: {linha['cliente']} | Valor: {linha['valor']}"
            )

        # Somando a coluna de valor
        total = float(df["valor"].sum())
        logging.info(f"Total faturado: R$ {total:.2f}")
        return total

    except FileNotFoundError:
        logging.error(f"Arquivo nao encontrado: {caminho}")
        return 0.0

    except pd.errors.EmptyDataError:
        logging.error(f"Arquivo CSV esta vazio: {caminho}")
        return 0.0

    finally:
        logging.info(f"Fim da tentativa de importacao do arquivo: {caminho}\n")


if __name__ == "__main__":
    # Teste 1: Arquivo que nao existe
    print("--- Teste 1: Arquivo Inexistente ---")
    importar_notas("arquivo_inexistente.csv")

    # Teste 2: Criando um notas.csv simples para testar
    print("--- Teste 2: Arquivo Existente ---")
    dados = {
        "nota": [101, 102, 103],
        "cliente": ["Cliente A", "Cliente B", "Cliente C"],
        "valor": [1500.50, 2300.00, 450.75],
    }
    pd.DataFrame(dados).to_csv("notas.csv", index=False)

    # Executando a importacao real
    resultado = importar_notas("notas.csv")
    print(f"Resultado final: R$ {resultado:.2f}")