import requests
from bs4 import BeautifulSoup

def fetch_news_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h3')
        headlines_list = [headline.get_text(strip=True) for headline in headlines]
        if headlines_list:
            for i, headline in enumerate(headlines_list, 1):
                print(f"{i}. {headline}")
        else:
            print("Nenhuma manchete encontrada na BBC.")
        return headlines_list
    else:
        print(f"Falha ao acessar o site da BBC: Status {response.status_code}")
        return []

def fetch_news_g1():
    url = "https://g1.globo.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('a', class_='feed-post-link')
        headlines_list = [headline.get_text(strip=True) for headline in headlines]
        if headlines_list:
            for i, headline in enumerate(headlines_list, 1):
                print(f"{i}. {headline}")
        else:
            print("Nenhuma manchete encontrada no G1.")
        return headlines_list
    else:
        print(f"Falha ao acessar o site do G1: Status {response.status_code}")
        return []

def save_news_to_file(headlines, filename):
    if headlines:
        with open(filename, 'w', encoding='utf-8') as file:
            for i, headline in enumerate(headlines, 1):
                file.write(f"{i}. {headline}\n")
        print(f"Notícias salvas em {filename}")
    else:
        print("Nenhuma manchete para salvar.")

if __name__ == "__main__":
    site = input("Digite o site de notícias (bbc ou g1): ").strip().lower()
    
    if site == "bbc":
        headlines = fetch_news_bbc()
        save_news_to_file(headlines, "bbc_headlines.txt")
    elif site == "g1":
        headlines = fetch_news_g1()
        save_news_to_file(headlines, "g1_headlines.txt")
    else:
        print("Site não suportado. Por favor, escolha entre 'bbc' ou 'g1'.")
