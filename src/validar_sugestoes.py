import json
import sys

def validar(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    if not isinstance(dados, list) or len(dados) > 10:
        raise ValueError("Lista inválida ou mais de 10 sugestões!")

    titulos = set()
    for filme in dados:
        if filme["titulo"] in titulos:
            raise ValueError(f"Filme duplicado: {filme['titulo']}")
        titulos.add(filme["titulo"])

    print("Validação concluída com sucesso!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validar_sugestoes.py caminho_para_arquivo.json")
        sys.exit(1)

    validar(sys.argv[1])
