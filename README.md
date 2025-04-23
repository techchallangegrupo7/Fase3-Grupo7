
# 🤖 Tech Challenge - Fase 3 - Fine-Tuning de Foundation Model

Projeto desenvolvido como parte do **Tech Challenge da 3ª fase do curso IADT**, cujo objetivo é realizar o *fine-tuning* de um modelo de fundação (como LLaMA, BERT ou Mistral) utilizando o dataset **AmazonTitles-1.3MM**.

---

## 📌 Objetivo

Treinar um modelo de linguagem capaz de **responder perguntas sobre produtos** com base nos títulos e descrições extraídas do dataset `trn.json`, simulando uma interface de perguntas e respostas como um chatbot para e-commerce.

---

## 🧠 Modelo Utilizado

- Modelo: `Nome_do_Modelo (ex: BERT-base, LLaMA-7B, Mistral-7B, etc)`
- Framework: `Transformers (Hugging Face) / Unsloth / LoRA / PEFT`
- Ambiente de Treinamento: `Google Colab / Local com GPU / etc`

---

## 🗂️ Dataset

- Nome: `AmazonTitles-1.3MM`
- Fonte: [Link para o dataset](https://drive.google.com/file/d/12zH4mL2RX8iSvH0VCNnd3QxO4DzuHWnK/view)
- Arquivo usado: `trn.json`
- Campos utilizados:
  - `title`: título do produto
  - `content`: descrição do produto

---

## ⚙️ Processo de Fine-Tuning

1. **Pré-processamento do Dataset**:

   - Limpeza de caracteres especiais
   - Conversão para prompts no formato:
     ```
     Pergunta: O que é [title]?
     Resposta: [content]
     ```
2. **Configuração do Modelo**:

   - Tokenizer e modelo base carregados da HuggingFace
   - Estratégia de fine-tuning: `full fine-tuning` ou `LoRA` com PEFT
3. **Treinamento**:

   - Batch Size: X
   - Epochs: X
   - Learning Rate: X
   - Ferramentas: `Transformers`, `Datasets`, `PEFT`

---

## 💬 Exemplo de Pergunta e Resposta

**Pergunta**: O que é *Echo Dot (4ª geração)*?
**Resposta**: Echo Dot é um alto-falante inteligente com Alexa projetado para se adaptar a qualquer ambiente da sua casa...

---

## 📽️ Demonstração

🎥 Link para o vídeo no YouTube: [Clique aqui](https://youtube.com/link-do-video)

---

## 📁 Repositório

📦 Link do repositório com os códigos: [https://github.com/techchallangegrupo7/Fase3-Grupo7](https://github.com/techchallangegrupo7/Fase3-Grupo7)

---

## 👨‍💻 Desenvolvedores (Grupo 9)

- Fábio Yuiti Takaki (Discord: takakisan.)
- Luiz Claudio Cunha de Albuquerque (Discord: inefavel1305)
- Matheus Felipe Condé Rocha (Discord: mfconde)
- Pedro Vitor Franco de Carvalho (Discord: pedro_black10)
- Tatiana Yuka Takaki (Discord: tatianayk)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
