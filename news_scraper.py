import requests
from bs4 import BeautifulSoup

def fetch_news(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headlines = soup.find_all('h2')
        headlines_list = [headline.get_text(strip=True) for headline in headlines]
        if headlines_list:
            for i, headline in enumerate(headlines_list, 1):
                print(f"{i}. {headline}")
        else:
            print("Nenhuma manchete encontrada. Verifique o seletor HTML.")
        return headlines_list
    else:
        print(f"Falha ao acessar o site: Status {response.status_code}")
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
    url = "https://www.bbc.com/news"
    headlines = fetch_news(url)
    save_news_to_file(headlines, "news_headlines.txt")
