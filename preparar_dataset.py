import json
import subprocess
import sys

# Tenta instalar gdown automaticamente caso não esteja disponível
try:
    import gdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
    import gdown


# ID do arquivo trn.json compartilhado no Google Drive
file_id = "1kq9bSDUfj0sxGO6C9bb95EYWtey6Smf_"
output = "trn.json"

# Baixa o arquivo trn.json do Google Drive
gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)

# Caminho do arquivo de entrada (baixado) e saída
CAMINHO_JSON = "trn.json"
SAIDA_JSONL = "dataset_preparado.jsonl"

# Função responsável por preparar os dados no formato necessário para treinamento do modelo
def preparar_dataset_jsonl(caminho_entrada, caminho_saida):
    contador = 0      # Contador de linhas válidas processadas
    ignorados = 0     # Contador de linhas ignoradas (inválidas ou sem conteúdo)

    # Abre o arquivo de entrada (JSON bruto) e o arquivo de saída (JSONL) ao mesmo tempo
    with open(caminho_entrada, 'r', encoding='utf-8') as f_in, \
         open(caminho_saida, 'w', encoding='utf-8') as f_out:

        # Percorre cada linha do arquivo (cada linha representa um JSON com dados de um produto)
        for linha in f_in:
            try:
                # Converte a linha (string) em um dicionário Python usando json.loads()
                item = json.loads(linha)

                # Extrai os campos 'title' e 'content'; se estiverem ausentes, retorna string vazia
                titulo = item.get("title", "").strip()
                descricao = item.get("content", "").strip()

                # Se ambos os campos existirem e não estiverem vazios, processa o item
                if titulo and descricao:
                    # Cria um prompt no formato de pergunta, como será fornecido ao modelo
                    prompt = f"O que é {titulo}?"
                    completion = descricao
                    
                    # Escreve o objeto como uma linha JSON no arquivo de saída
                    f_out.write(json.dumps({
                        "prompt": prompt,
                        "completion": completion
                    }, ensure_ascii=False) + '\n')
                    contador += 1
                else:
                    ignorados += 1

            except json.JSONDecodeError:
                ignorados += 1
                continue

    print(f"✅ Dataset gerado com sucesso!")
    print(f"📄 Linhas válidas: {contador}")
    print(f"🚫 Linhas ignoradas (sem conteúdo ou erro): {ignorados}")
    print(f"💾 Arquivo salvo em: {caminho_saida}")

# Executa a função apenas se o script estiver sendo executado diretamente (não importado)
if __name__ == "__main__":
    preparar_dataset_jsonl(CAMINHO_JSON, SAIDA_JSONL)
