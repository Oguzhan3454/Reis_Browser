import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        search = request.POST["search"]

        sonuc = []
        arama_terimi = search

        url = f"https://www.google.com/search?q={arama_terimi}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        soup = BeautifulSoup(response.text, 'html.parser')

        print("sa")

        for result in soup.find_all('div', {'class': 'g'}):
            title_tag = result.find('h3')
            title = title_tag.text.strip() if title_tag else 'Başlık bulunamadı'
            
            link_tag = result.find('a')
            link = link_tag['href'] if link_tag else 'Link bulunamadı'
            
            description_tag = result.find('span', {'class': 'aCOpRe'})
            description = description_tag.text.strip() if description_tag else 'Açıklama bulunamadı'
            
            sonuc.append({'title': title, 'link': link, 'description': description})

        context = {
            'sonuc': sonuc,
        }

        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

