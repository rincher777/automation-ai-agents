# 🤖 Automation & AI Agents: Monitor de Preços Inteligente

Este repositório faz parte do meu portfólio de **Sistemas de Automação** e **Engenharia de Dados**. O projeto consiste em um ecossistema completo para monitoramento de preços da concorrência com visualização em tempo real.

## 🚀 Funcionalidades
- **Web Scraping Resiliente**: Coleta automatizada utilizando cabeçalhos que simulam navegação humana para evitar bloqueios.
- **Limpeza de Dados**: Algoritmos de filtragem para garantir que apenas valores numéricos válidos sejam processados.
- **Dashboard de KPIs**: Interface visual interativa para análise de histórico e variação de preços.

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem core do sistema.
- **BeautifulSoup4**: Extração de dados (Scraping).
- **Pandas**: Manipulação e tratamento de grandes volumes de dados.
- **Streamlit**: Interface web moderna para exibição de métricas.
- **Plotly**: Gráficos dinâmicos e interativos.

## 📈 Como Executar
1. Instale as dependências:
   `pip install requests beautifulsoup4 pandas streamlit plotly`
2. Execute o coletor:
   `python scraper.py`
3. Inicie o painel visual:
   `python -m streamlit run dashboard.py`

---
Desenvolvido por **Leomy Rincher** | Especialista em Automação e IA.