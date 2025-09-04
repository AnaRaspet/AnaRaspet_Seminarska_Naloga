from bs4 import BeautifulSoup
import os
import json
import csv

def main():
    try:
        vsa_dela = izberi_vse_oglase()
        vsa_dela_s_urejenimi_podatki = urejanje_vsebine_oglasov(vsa_dela)
        shrani_vsebino_oglasov(vsa_dela_s_urejenimi_podatki)
    except Exception as e:
        print("Prišlo je do napake ko smo urejali podatke" + str(e))

def izberi_vse_oglase():
    vsa_dela = []
    for stran in os.listdir('./vsebina'):
        with open('./vsebina/' + stran, 'r') as f:
            stran = BeautifulSoup(f, 'html.parser')
            #najdemo vse oglase na strani
            dela = stran.find_all('article', class_='job-item')
            vsa_dela.extend(dela)
    return vsa_dela

def urejanje_vsebine_oglasov(vsa_dela):
    seznam_del = []
    #s for zanko iteriramo po vseh oglasih in iz vsakega oglasa izluščimo podatke ter jih shranimo v slovar
    for delo in vsa_dela: 
        naslovi = delo.findAll('h5', class_='mb-0')
        vrsta_dela = naslovi[0].text.strip()
        try:
            naslov_oglasa = naslovi[1].text.strip()
        except:
            naslov_oglasa = "Brez naslova"
            
        kraj = delo.find('svg', class_='ticon text-primary').parent.text.strip()
        if "-" in kraj or "Z OKOLICO" in kraj or "IN OKOLICA" in kraj or "IN" in kraj or "," in kraj or "LJUBLJANA" in kraj or "(" in kraj or "/" in kraj:
            kraj = kraj.split(" ")[0]
            kraj = kraj.split("-")[0]
            kraj = kraj.split(",")[0]
            kraj = kraj.split("/")[0]
        kraj = kraj.strip()

        placilo = delo.find('li', class_="job-payment").find('a').find('strong').text.strip()
        placilo = placilo.split(" ")[0] #pri placilu ohranimo le vrednost brez "€" in "h" za lazjo obdelavo kasneje
        placilo = placilo.replace(",", ".")

        #placilo pretovrim v float ce je to mogoce, sicer pa preskocimo to oglas
        try:
            placilo = float(placilo)
        except ValueError:
            continue
        
        
        atributi_ul = delo.find_all('ul', class_='job-attributes')[1]
        atributi = atributi_ul.find_all('li')
        count = 0
        prosta_mesta, trajanje, delovnik, zacetek_dela = "1", "Brez podatka", "Brez podatka", "Brez podatka"
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
    return seznam_del

def shrani_vsebino_oglasov(vsa_dela_s_urejenimi_podatki):
    with open('podatki_dela.json', 'w') as f:
        json.dump(vsa_dela_s_urejenimi_podatki, f, ensure_ascii=False, indent=2)

    with open('podatki_dela.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Vrsta dela", "Naslov oglasa", "Kraj", "Placilo", "Prosta mesta", "Trajanje", "Delovnik", "Začetek dela"])
        for delo in vsa_dela_s_urejenimi_podatki:
            writer.writerow([delo["vrsta_dela"], delo["naslov_oglasa"], delo["kraj"], delo["placilo"], delo["prosta_mesta"], delo["trajanje"], delo["delovnik"], delo["zacetek_dela"]])

if __name__ == "__main__":
    main()