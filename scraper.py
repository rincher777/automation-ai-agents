import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def monitorar_preco(url):
    # Headers para o site não bloquear o seu acesso (simula um navegador)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # NOTA: Os seletores ('h1' ou 'span') mudam conforme o site.
        # Aqui buscamos um título e um preço genérico.
        titulo = soup.find('h1').get_text().strip()
        
        # Exemplo: buscando uma classe que contenha o preço
        preco = soup.find('span', class_='a-offscreen').get_text().strip()

        print(f"Produto: {titulo}")
        print(f"Preço atual: {preco}")

        # Salvar num ficheiro CSV (Histórico)
        dados = {
            'Data': [datetime.now().strftime("%d/%m/%Y %H:%M:%S")],
            'Produto': [titulo],
            'Preço': [preco]
        }
        
        df = pd.DataFrame(dados)
        df.to_csv('precos_concorrencia.csv', mode='a', index=False, header=not pd.io.common.file_exists('precos_concorrencia.csv'))
        
    except Exception as e:
        print(f"Erro ao capturar dados: {e}")

# URL de teste (substitua por um produto real de um site que permita scraping)
url_produto = "COLOQUE_A_URL_AQUI"
monitorar_preco(url_produto)