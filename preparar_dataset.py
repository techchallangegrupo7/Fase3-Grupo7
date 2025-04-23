# Importa o módulo JSON da biblioteca padrão para manipulação de dados em formato JSON
import json

# Caminho completo para o arquivo 'trn.json' descompactado com os dados brutos do dataset.
# Atenção: utilize o 'r' antes da string para evitar erros com barras invertidas no caminho.
CAMINHO_JSON = r"D:\Drive\Meu Drive\Cursos - Pós\Fiap - Póstech - 4IADT - IA para Devs\Fase 3 - OpenAI - de 18-03-2025 a 27-05-2025\Tech Challenge\Github\Fase3-Grupo7\LF-Amazon-1.3M\trn.json"

# Caminho onde será salvo o novo arquivo JSONL com os dados processados e formatados para o fine-tuning.
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
                    completion = descricao # A resposta esperada será a descrição do produto
                    
                    # Escreve o objeto como uma linha JSON no arquivo de saída
                    # O formato será compatível com treinamentos baseados em prompt/completion
                    f_out.write(json.dumps({
                        "prompt": prompt,
                        "completion": completion
                    }, ensure_ascii=False) + '\n') # Adiciona nova linha após cada entrada
                    contador += 1 # Conta as linhas válidas
                else:
                    ignorados += 1 # Ignora entradas com campos ausentes ou vazios

            except json.JSONDecodeError:
                # Se ocorrer erro ao decodificar a linha como JSON (linha malformada), ignora
                ignorados += 1
                continue

    # Mensagens finais no terminal com o resultado do processamento
    print(f"✅ Dataset gerado com sucesso!")
    print(f"📄 Linhas válidas: {contador}")
    print(f"🚫 Linhas ignoradas (sem conteúdo ou erro): {ignorados}")
    print(f"💾 Arquivo salvo em: {caminho_saida}")

# Executa a função apenas se o script estiver sendo executado diretamente (não importado)
if __name__ == "__main__":
    preparar_dataset_jsonl(CAMINHO_JSON, SAIDA_JSONL)