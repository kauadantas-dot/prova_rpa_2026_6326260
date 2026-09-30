def cadastrar_item(nome: str, quantidade: int, preco_unitario: float) -> dict:
    """Retorna um dict com as chaves 'nome', 'quantidade' e 'preco_unitario'."""
    return {
        "nome": nome,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
    }


def calcular_valor_estoque(itens: list) -> float:
    """Retorna a soma de (quantidade * preco_unitario) de todos os itens."""
    total = 0.0
    for item in itens:
        total += item["quantidade"] * item["preco_unitario"]
    return total


def listar_itens_em_falta(itens: list, minimo: int) -> list:
    """Retorna uma nova lista so com os itens cuja quantidade < minimo."""
    em_falta = []
    for item in itens:
        if item["quantidade"] < minimo:
            em_falta.append(item)
    return em_falta