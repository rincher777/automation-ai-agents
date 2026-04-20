import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

def monitorar_preco(url):
    # Headers para simular um navegador real e evitar bloqueios
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    try:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Acessando o site...")
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Erro de conexão: Status {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # --- EXTRAÇÃO DO TÍTULO ---
        titulo = "Não encontrado"
        seletores_titulo = ['#productTitle', '.product-title', 'h1']
        for s in seletores_titulo:
            tag = soup.select_one(s)
            if tag:
                titulo = tag.get_text().strip()
                break

        # --- EXTRAÇÃO DO PREÇO (Lógica de Redundância) ---
        preco = "Não encontrado"
        # Seletores comuns da Amazon e outros e-commerces
        seletores_preco = [
            'span.a-price-whole', 
            'span.a-offscreen', 
            '.priceToPay', 
            '.a-price',
            'span[class*="price"]'
        ]
        
        for s in seletores_preco:
            tag = soup.select_one(s)
            if tag:
                texto = tag.get_text().strip()
                # REGEX ou Filtro simples: Mantém apenas o que parece preço (números, vírgula e ponto)
                import re
                numeros = re.findall(r'\d+[.,]?\d*', texto)
                if numeros:
                    # Pega o maior grupo de números (geralmente o preço principal)
                    preco = numeros[0]
                    break

        # --- PROCESSAMENTO DOS RESULTADOS ---
        if titulo != "Não encontrado" and preco != "Não encontrado":
            print(f"✅ Sucesso!")
            print(f"📦 Produto: {titulo[:50]}...") # Mostra só os primeiros 50 caracteres
            print(f"💰 Preço: R$ {preco}")

            # Salvar no CSV (Banco de Dados simples)
            arquivo_csv = 'precos_concorrencia.csv'
            dados = {
                'Data': [datetime.now().strftime("%d/%m/%Y %H:%M:%S")],
                'Produto': [titulo],
                'Preço': [preco],
                'URL': [url]
            }
            
            df = pd.DataFrame(dados)
            # Verifica se o arquivo existe para não repetir o cabeçalho
            header = not os.path.exists(arquivo_csv)
            df.to_csv(arquivo_csv, mode='a', index=False, header=header, encoding='utf-8-sig')
            print(f"💾 Dados salvos em {arquivo_csv}")

        else:
            print("⚠️ Falha na extração. O site pode ter exibido um Captcha ou mudado o layout.")
            # Salva o erro para análise (Opcional)
            with open("log_erro.html", "w", encoding='utf-8') as f:
                f.write(response.text)
            print("📝 Log de erro salvo em 'log_erro.html'. Verifique o conteúdo do arquivo.")

    except Exception as e:
        print(f"❌ Erro fatal no sistema: {e}")

# --- EXECUÇÃO ---
# Use um link real aqui (exemplo: Mouse da Logitech na Amazon ou Mercado Livre)
url_alvo = "https://www.mercadolivre.com.br/apple-iphone-15-128-gb-preto/p/MLB27623301"

if __name__ == "__main__":
    monitorar_preco(url_alvo)