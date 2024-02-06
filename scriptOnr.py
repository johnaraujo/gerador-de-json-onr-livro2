import pandas as pd
import json  # Importa o módulo json

# Substitua 'caminho_para_sua_planilha.xlsx' pelo caminho do seu arquivo Excel ou CSV
caminho_da_planilha = 'C:\\dados\\caminho_para_sua_planilha2.xlsx'
# Se o arquivo for CSV, use pd.read_csv em vez de pd.read_excel
df = pd.read_excel(caminho_da_planilha)

# Inicializa o payload e a variável seq
payload = {"lote": {"registro": []}}
seq = 1

for index, row in df.iterrows():
    registro = {
        "seq": seq,
        "tipo": "A",
        "livro": 2,
        "num": row['matricula'],  # Assumindo que a coluna na planilha se chama 'matricula'
        "cnm": row['cnm'],  # Assumindo que a coluna na planilha se chama 'cnm'
        "situacao": 0
    }
    payload["lote"]["registro"].append(registro)
    seq += 1

# Converte o payload para string JSON
json_payload = json.dumps(payload, indent=4)  # indent=4 para melhorar a legibilidade

# Especifica o caminho e o nome do arquivo onde o JSON será gravado
caminho_para_salvar_o_json = 'C:\\dados\\payload.json'

# Grava o JSON no arquivo
with open(caminho_para_salvar_o_json, 'w') as f:
    f.write(json_payload)

print(f'Arquivo JSON gravado com sucesso em: {caminho_para_salvar_o_json}')
