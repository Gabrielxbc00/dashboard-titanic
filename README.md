# 🚢 Dashboard Titanic

Este repositório contém um dashboard interativo construído com **Streamlit** para a visualização e análise dos dados do Titanic.

## 📌 Descrição

O objetivo deste projeto é explorar os dados do Titanic e apresentar insights através de visualizações interativas. O dashboard permite aplicar filtros, visualizar estatísticas e entender padrões sobre sobrevivência com base em diferentes variáveis.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Streamlit** (para criação do dashboard)
- **Pandas** (para manipulação dos dados)
- **Plotly** (para visualização de gráficos interativos)

## 📂 Estrutura do Projeto
```
├── assets/                     # Imagens e arquivos auxiliares
│   ├── titanic.csv             # Dataset do Titanic
│   ├── titanic-image.jpg       # Imagem usada no dashboard
├── data_processing.py          # Script para carregar e tratar os dados
├── filters.py                  # Script para aplicar filtros no dataset
├── dashboard.py                # Arquivo principal do Streamlit
├── requirements.txt            # Dependências do projeto
├── dashboard_titanic.zip       # Arquivo compactado com todo o projeto
├── README.md                   # Documentação do projeto
```

## 🚀 Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o dashboard**
   ```bash
   streamlit run dashboard.py
   ```

5. **Acesse o dashboard**
   O Streamlit abrirá automaticamente no navegador. Caso não abra, acesse manualmente: [http://localhost:8501](http://localhost:8501)

## 🌍 Acesse o Dashboard Online
O projeto também está disponível online e pode ser acessado pelo link abaixo:
🔗 [Dashboard Titanic](https://dashboard-titanic.streamlit.app/)

## 📥 Download do Projeto Compactado
Para facilitar o download do projeto completo, também foi enviado para o repositório o arquivo `dashboard_titanic.zip`, que contém todos os arquivos necessários.

## 📊 Funcionalidades
✅ **Filtros interativos**: Classe, sexo e faixa etária dos passageiros  
✅ **Visualizações dinâmicas**: Gráficos interativos com Plotly  
✅ **Insights sobre os dados**: Principais conclusões sobre a sobrevivência no Titanic  

## 📜 Licença
Este projeto é de livre uso para fins educacionais e de estudo.

---
**Desenvolvido por Gabriel Ximenes** 🚢

