# 🤖 Tech Challenge - Fase 3 - Fine-Tuning de Foundation Model

Projeto desenvolvido como parte do Tech Challenge da 3ª fase do curso IADT, cujo objetivo é realizar o fine-tuning de um modelo de fundação (como LLaMA, BERT ou Mistral) utilizando o dataset AmazonTitles-1.3MM.

---

## 📌 Objetivo

Treinar um modelo de linguagem capaz de responder perguntas sobre produtos com base nos títulos e descrições extraídas do dataset `trn.json`, simulando uma interface de perguntas e respostas como um chatbot para e-commerce. .

---

## 🧠 Modelo Utilizado

- **Modelo:** Nome_do_Modelo (ex: BERT-base, LLaMA-7B, Mistral-7B, etc)
- **Framework:** Transformers (Hugging Face) / Unsloth / LoRA / PEFT
- **Ambiente de Treinamento:** Google Colab / Local com GPU / etc

---

## 🗂️ Dataset

- **Nome:** AmazonTitles-1.3MM
- **Fonte:** [Link para o dataset](https://drive.google.com/file/d/12zH4mL2RX8iSvH0VCNnd3QxO4DzuHWnK/view)
- **Arquivo usado:** `trn.json`

### Campos utilizados:

- `title`: título do produto
- `content`: descrição do produto

---

## ⚙️ Processo de Fine-Tuning

### 🔍 Pré-processamento do Dataset

Foi criado o notebook [`preparar_dataset.ipynb`](https://colab.research.google.com/github/techchallangegrupo7/Fase3-Grupo9/blob/main/preparar_dataset.ipynb), responsável por:

- Instalar dependências automaticamente (`gdown`)
- Baixar o arquivo `trn.json` do Google Drive, caso não exista
- Validar e transformar os dados no formato `.jsonl`:
  - Verifica presença de título e descrição
  - Gera arquivos com o seguinte formato:
    - **Prompt:** `O que é [title]?`
    - **Completion:** `[content]`
- Exibir relatório de registros válidos e ignorados:
  - Quantidade de linhas ignoradas por:
    - Falha de parsing (JSON inválido)
    - Título vazio
    - Descrição vazia

## 🧪 Configuração do Modelo

- Tokenizer e modelo base carregados via Hugging Face
- Estratégia de fine-tuning:
  - `full fine-tuning` ou `LoRA` com `PEFT`

### 🧬 Treinamento

- **Batch Size:** X
- **Epochs:** X
- **Learning Rate:** X
- **Ferramentas:** Transformers, Datasets, PEFT

---

## 💬 Exemplo de Pergunta e Resposta

```text
Pergunta: O que é Echo Dot (4ª geração)?
Resposta: Echo Dot é um alto-falante inteligente com Alexa projetado para se adaptar a qualquer ambiente da sua casa...
```

---

## 📽️ Demonstração

🎥 Link para o vídeo no YouTube: [Clique aqui](https://www.youtube.com/@Grupo7TechChallenge-IAparaDevs)

---

## 📁 Repositório

📦 Link do repositório com os códigos:
👉 [https://github.com/techchallangegrupo7/Fase3-Grupo9](https://github.com/techchallangegrupo7/Fase3-Grupo9)

---

## 👨‍💻 Desenvolvedores (Grupo 9)

- **Fábio Yuiti Takaki** (Discord: `takakisan.`)
- **Luiz Claudio Cunha de Albuquerque** (Discord: `inefavel1305`)
- **Matheus Felipe Condé Rocha** (Discord: `mfconde`)
- **Pedro Vitor Franco de Carvalho** (Discord: `pedro_black10`)
- **Tatiana Yuka Takaki** (Discord: `tatianayk`)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
