# Tech Challenge - Fase 3: Fine-Tuning de Modelo de Linguagem

Este projeto foi desenvolvido como parte da Fase 3 do Tech Challenge no curso de Inteligência Artificial para Desenvolvedores (FIAP). O desafio consistiu em aplicar fine-tuning em um modelo de linguagem (foundation model), adaptando-o para responder perguntas com base em descrições de produtos do e-commerce.

## 🎯 Objetivo

Treinar um modelo capaz de responder, de forma clara e útil, a perguntas sobre produtos com base em seus títulos e descrições, simulando o comportamento de um assistente virtual de compras. O modelo foi ajustado com técnicas modernas de fine-tuning sobre dados reais.

## 🧠 Modelo

- **Modelo base:** Meta-LLaMA 3 (8B Instruct)
- **Técnicas aplicadas:** LoRA (Low-Rank Adaptation) + PEFT (Parameter-Efficient Fine-Tuning)
- **Frameworks:** Hugging Face Transformers, PEFT, Unsloth
- **Ambiente de execução:** Google Colab com suporte a GPU

## 📦 Dataset

- **Nome:** AmazonTitles-1.3MM
- **Fonte:** Arquivo `trn.json` (extraído de um ZIP via Google Drive)
- **Campos utilizados:** `title` (título do produto) e `content` (descrição)

## ⚙️ Pré-processamento

Realizado no notebook [`tc_preparar_dataset_removeJornais.ipynb`](https://github.com/techchallangegrupo7/Fase3-Grupo9/blob/main/Llama3.18bAlpaca/tc_preparar_dataset_removeJornais.ipynb). Etapas:

1. **Montagem do Google Drive** para acesso ao arquivo `.zip`.
2. **Download automático** do arquivo `dados.zip` via `gdown` (Google Drive).
3. **Extração e descompactação** do arquivo `trn.json` ou `trn.json.gz`.
4. **Filtragem de dados**:

   - Remoção de entradas com `title` ou `content` vazios ou genéricos.
   - Exclusão de produtos relacionados a jornais ou conteúdo não relevante para o objetivo.
5. **Conversão para formato `.jsonl`** no estilo Alpaca:

```json
{
  "instruction": "What is it",
  "input": "<title>",
  "output": "<content>"
}
```

## 🏋️ Treinamento

Dois notebooks com configurações diferentes de épocas:

- [`tc_fase3_Llama3_1_(8B)_Alpaca.ipynb`](https://github.com/techchallangegrupo7/Fase3-Grupo9/blob/main/Llama3.18bAlpaca/tc_fase3_Llama3_1_(8B)_Alpaca.ipynb) (1 época)
- [`tc_fase3_Llama3_1_(8B)_Alpaca_2_epocas.ipynb`](https://github.com/techchallangegrupo7/Fase3-Grupo9/blob/main/Llama3.18bAlpaca/tc_fase3_Llama3_1_(8B)_Alpaca_2_epocas.ipynb) (2 épocas)

**Parâmetros principais:**

- Modelo: Meta-LLaMA 3 8B
- Batch size: 4
- Learning rate: 2e-5
- Fine-tuning com LoRA via PEFT
- Dados no formato Alpaca
- Checkpoints salvos no Google Drive

## 🤖 Inferência

No notebook [`consultando_lora_opaca_tc_compare.ipynb`](https://github.com/techchallangegrupo7/Fase3-Grupo9/blob/main/Llama3.18bAlpaca/consultando_lora_opaca_tc_compare.ipynb), comparam-se:

- Modelo original (sem ajuste)
- Modelo ajustado com 1 época
- Modelo ajustado com 2 épocas

Exemplo de prompt:

```
Instruction:
Imagine you're introducing this product to a customer. Create a product summary from this title.

Input:
Miss Marple's Final Cases

Resposta modelo base:
The Miss Marple mysteries, first published between 1927 and 1971, are among Christie's most popular...

Resposta modelo LoRA - 1 epoch:
Agatha Christie's first collection of short stories, published in 1941, contains 14 stories, some...

Resposta modelo LoRA - 2 epoch:
The 12 stories in this volume are a wonderful send-off for Miss Marple, who, as Christie herself...
```

## 🎥 Demonstração em Vídeo

Assista ao vídeo explicativo do projeto:
[🔗 YouTube – Grupo 7 Tech Challenge](https://www.youtube.com/@Grupo7TechChallenge-IAparaDevs)

## 💻 Repositório

Código-fonte completo e notebooks disponíveis em:
[https://github.com/techchallangegrupo7/Fase3-Grupo9](https://github.com/techchallangegrupo7/Fase3-Grupo9)

## 🗂️ Arquivos de Dados e Modelos 

Devido à limitação de espaço no GitHub, os arquivos de dataset e os diretórios de modelos treinados estão disponíveis no Google Drive:

🔗 [Acessar pasta no Google Drive](https://drive.google.com/drive/folders/1-i7qAsALs1fy6cTVrHoo9Ggg8-Nzoccl?usp=drive_link)

**Conteúdo da pasta:**

- `trn.json`: Arquivo original com os dados brutos.
- `dataset_preparado_100_alpaca.jsonl`: Dataset final em formato Alpaca.
- `lora_model_alpaca/`: Modelo treinado com 1 época.
- `lora_model_alpaca_2_epocas/`: Modelo treinado com 2 épocas.

## 👥 Equipe

Grupo 9 da turma IA para Devs - FIAP:

- **Fábio Yuiti Takaki** (Discord: `takakisan.`)
- **Luiz Claudio Cunha de Albuquerque** (Discord: `inefavel1305`)
- **Matheus Felipe Condé Rocha** (Discord: `mfconde`)
- **Pedro Vitor Franco de Carvalho** (Discord: `pedro_black10`)
- **Tatiana Yuka Takaki** (Discord: `tatianayk`)
 
