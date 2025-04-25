import json
from datetime import datetime

def gerar_sugestoes(genero="Fantasia"):
    filmes = []
    for i in range(1, 11):
        filmes.append({
            "titulo": f"{genero} - Filme {i}",
            "genero": genero,
            "ano": 2000 + i
        })

    data = datetime.today().strftime("%Y-%m-%d")
    with open(f"sugestoes/{data}_{genero}.json", "w", encoding="utf-8") as f:
        json.dump(filmes, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    gerar_sugestoes("Fantasia")