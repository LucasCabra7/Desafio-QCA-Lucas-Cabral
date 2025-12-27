<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=66CDAA&height=120&section=header"/>

# ⭐ Desafio Técnico - QCA 

Projeto desenvolvido como parte do processo seletivo para a área de Desenvolvimento e Aplicações da QCA - Queiros Cavalcante Advocacia.

---

## 📌 Descrição do Projeto

Este projeto foi desenvolvido como solução para um desafio técnico de automação em **Python**, cujo objetivo é processar **Invoices (faturas)** em formato PDF, extrair informações estruturadas, armazená-las localmente e disponibilizar consultas analíticas sobre os dados. 

A aplicação realiza as seguintes operações:

- Extração automática de dados a partir de PDF's
- Validação de dados com **Pydantic**
- Armazenamento incremental em **JSON**, com verificação de duplicidade
- Análises estatísticas utilizando **Pandas**

Todo o projeto foi desenvolvido seguindo **Programação Orientada a Objetos (POO)**.

---

## 💻 Funcionalidades Implementadas

### 1. Ingestão de Dados:

- Leitura de múltiplos arquivos PDF's a partir de um diretório
- Extração das seguintes features:
  - Order ID
  - Data da fatura
  - Customer ID
  - Itens da fatura: Nome do produto, Quantidade e Preço unitário.
 
### 2. Validação:

- Utilização do **Pydantic** para garantir a integridade e tipagem dos dados antes do armazenamento.

### 3. Armazenamento:

- Persistência dos dados em um arquivo `database.json`
- Implementação de **verificação de duplicidade**, impedindo a gravação de faturas com o mesmo `Order ID`
- Criação e atualização do arquivo em tempo de execução do script

### 4. Análises:

A partir da base JSON gerada, o sistema retorna:
- Média do valor total das faturas
- Produto com maior frequência de compra (moda)
- Valor total gasto por cada produto
- Listagem de protudos contendo nome e preço unitário

---

## 🧱 Modularização do Projeto

1. O arquivo `database.json` não é versionado. Ele é gerado automaticamente em tempo de execução do projeto, devido a solicitação do desafio.
2. O arquivo `.gitkeep`, presente na pasta `data`, tem a única finalidade de permitir que o Git mantenha a pasta no repositório. Portanto, ao executar o projeto, esse arquivo pode ser removido e substituído pelos arquivos PDF necessários.

```text
DESAFIO-QCA-LUCAS-CABRAL/
│
├── data/
│   └── .gitkeep               # Acrescente aqui os arquivos PDF de invoices
│
├── src/
│   ├── extrator.py             
│   ├── modelos.py              
│   ├── database.py            
│   └── analises.py             
│
├── main.py                     
├── requirements.txt            
├── .gitignore                  
└── README.md                   

```

---

## ⚙️ Tecnologias de Desenvolvimento utilizadas

- **Python 3.13**
- **pdfplumber** - Leitura e extração de dados de PDF's
- **pydantic** - Validação e modelagem dos dados
- **pandas** - Análises e agregações estatísticas
- **JSON** - Persistência local dos dados

---

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/LucasCabra7/Desafio-QCA-Lucas-Cabral.git
cd /Desafio-QCA-Lucas-Cabral
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto
1. Adicione os arquivos PDF de invoices na padas `data`
2. Execute o script principal:

```bash
python main.py
```

---

### 🔎 Exemplo de Saída
<img width="549" height="396" alt="image" src="https://github.com/user-attachments/assets/dd257570-aa2e-49e3-99d1-5003ff734383" />


---

## 💡 Decisões Técnicas

- Separação entre **extração, persistência e análise** permite reutilização e fácil manutenção, pois este é o objetivo da modularização por **POO**
- A deduplicação por `Order ID` garante integridade dos dados, pois atua como chave primária
- O uso de Pydantic assegura que apenas dados válidos sejam armazenados
- O projeto foi estruturado para facilitar futuras extensões, como novos formatos de entrada ou exportação dos dados.

---

## 📃 Licença

Este projeto foi desenvolvido exclusivamente para fins de avaliação técnica, sem fins lucrativos. Todos os direitos reservado ao autor.

---

## Participante

<div align="center">

  <table>
    <tr>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/155683708?v=4" width="100px" alt="Lucas Cabral"/><br/>
        <b>Lucas Cabral</b>
      </td>
    </tr>
  </table>
</div>

---

<p align="center">
  &copy; 2025 Universidade Federal de Pernambuco - Centro de Informática. Todos os direitos reservados.
</p>

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=66CDAA&height=120&section=header"/>
