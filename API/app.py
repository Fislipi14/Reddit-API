import requests
import json

CLIENT = 'Client'
SECRET = 'Secret'

CONNECT = requests.auth.HTTPBasicAuth(CLIENT, SECRET)

data ={
    'grant_type': 'password',
    'username': 'user',
    'password': 'passwd'
}

headers = {'User-Agent': 'MyAPI/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=CONNECT, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

res = requests.get('https://oauth.reddit.com/r/python/best', headers=headers, params={'limit': '5'}) #<-- link da pagina

def json_puro(): #Gera um json da pagina
    with open('arq.json', 'w', encoding='utf-8') as arquivo:       
        json.dump(res.json(), arquivo, ensure_ascii=False, indent=4)

    return arquivo
pass

def limpa_arquivo(arquivo):
    linhas_unicas = set()
    with open(arquivo, 'r', encoding='utf-8') as arquivo_entrada:
        for linha in arquivo_entrada:
            linhas_unicas.add(linha.strip())

def pick_media():

    url = []

    for i in res.json()['data']['children']:
        url.append(i['data']['url'])

    with open('media_links.txt', 'w', encoding='utf-8') as media_arq:
        for link in url: 
            media_arq.write(link + '\n') 
    
    with open('cache.txt', '+a', encoding='utf-8') as arquivo_saida: #<-- Historico de links
        for linha in url:
            arquivo_saida.write(linha + '\n') 
pass

def filtro_media(arquivo, filtro):
    linhas_encontradas = set()
    with open(arquivo, 'r', encoding='utf-8') as f:
        for numero, linha in enumerate(f, start=1):
            if filtro in linha:
                linhas_encontradas.add(linha.strip())

    with open('filtrado_links.txt', 'w', encoding='utf-8') as arquivo:
        for link in linhas_encontradas:
            arquivo.write(link + '\n')

    return linhas_encontradas

pass

def main():
    json_puro()
    pick_media()
    ##filtro_media('media_links.txt', 'watch') <-- filtro de midias
    limpa_arquivo('filtrado_links.txt')

if __name__ == "__main__":
    main()
