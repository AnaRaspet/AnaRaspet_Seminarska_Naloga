from bs4 import BeautifulSoup
import requests
import json
import csv

try:
    stran = 1
    seznam_del = []
    for stran in range(1, 44):
        #url do strani e-studentskega servisa z oglasi
        url = 'https://www.studentski-servis.com/studenti/prosta-dela?scrolltop=1&kljb=&page=' + str(stran) + '&isci=1&sort=&dm1s=1&hourlyratefrom=6.32&hourlyrateto=35&hourly_rate=6.32%3B35'

        #preberemo vsebino strani s pomočjo requests in BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #najdemo vse oglase na strani
        dela = soup.find_all('article', class_='job-item')

        #s for zanko iteriramo po vseh oglasih in iz vsakega oglasa izluščimo podatke ter jih shranimo v slovar<
        for delo in dela: 
            naslovi = delo.findAll('h5', class_='mb-0')
            vrsta_dela = naslovi[0].text.strip()
            try:
                naslov_oglasa = naslovi[1].text.strip()
            except:
                naslov_oglasa = "Brez naslova"
                
            kraj = delo.find('svg', class_='ticon text-primary').parent.text.strip()
            placilo = delo.find('li', class_="job-payment").find('a').find('strong').text.strip()
            
            atributi_ul = delo.find_all('ul', class_='job-attributes')[1]
            atributi = atributi_ul.find_all('li')
            count = 0
            prosta_mesta, trajanje, delovnik, zacetek_dela = "Brez podatka", "Brez podatka", "Brez podatka", "Brez podatka"
            for li in atributi:
                li_text = li.get_text(strip=True)
                
                if "Prosta mesta:" in li_text:
                    prosta_mesta = li.find('strong').text.strip()
                elif "Trajanje:" in li_text:
                    trajanje = li.find('strong').text.strip()
                elif "Šifra:" in li_text:
                    continue
                elif "Delovnik:" in li_text:
                    delovnik = li.find('strong').text.strip()
                elif "Začetek dela:" in li_text:
                    zacetek_dela = li.find('strong').text.strip()
                
                count += 1
            
            trenutno_delo = {
                "vrsta_dela": vrsta_dela,
                "naslov_oglasa": naslov_oglasa,
                "kraj": kraj,
                "placilo": placilo,
                "prosta_mesta": prosta_mesta,
                "trajanje": trajanje,
                "delovnik": delovnik,
                "zacetek_dela": zacetek_dela
            }
            seznam_del.append(trenutno_delo)
        stran += 1
    with open('podatki_dela.json', 'w') as f:
        json.dump(seznam_del, f, ensure_ascii=False, indent=2)

    with open('podatki_dela.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Vrsta dela", "Naslov oglasa", "Kraj", "Placilo", "Prosta mesta", "Trajanje", "Delovnik", "Začetek dela"])
        for delo in seznam_del:
            writer.writerow([delo["vrsta_dela"], delo["naslov_oglasa"], delo["kraj"], delo["placilo"], delo["prosta_mesta"], delo["trajanje"], delo["delovnik"], delo["zacetek_dela"]])
            
except Exception as e:
    print("Prišlo je do napake pri branju vsebine strani" + str(e))
    







