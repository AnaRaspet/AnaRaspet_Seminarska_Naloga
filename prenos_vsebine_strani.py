import requests
from bs4 import BeautifulSoup
import os

def main():
    for stran in range(1, 44):
        try:
            pridobi_html_kodo(stran)
        except Exception as e:
            print("Prišlo je do napake pri prenosu vsebine strani" + str(e))


def pridobi_html_kodo(stran):
    vsebina = './vsebina'
    if not os.path.exists(vsebina):
        os.makedirs(vsebina)
    
    url = 'https://www.studentski-servis.com/studenti/prosta-dela?scrolltop=1&kljb=&page=' + str(stran) + '&isci=1&sort=&dm1s=1&hourlyratefrom=6.32&hourlyrateto=35&hourly_rate=6.32%3B35'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dokument = os.path.join(vsebina, 'stran_' + str(stran) + '.html')
    with open(dokument, 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    main()