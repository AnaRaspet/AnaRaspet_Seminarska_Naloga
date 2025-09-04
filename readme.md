ANALIZA PODATKOV O ŠTUDENTSKIH DELIH

OPIS PROJEKTA

Ta projekt vsebuje analizo podatkov o študentskih delih, zbranih s spletne strani Studentski servis. Projekt vključuje zbiranje podatkov, njihovo obdelavo in statistično analizo z vizualizacijami.

FUNKCIONALNOSTI:
1. Zbiranje podatkov
- prenos_vsebine_strani.py: Avtomatsko prenaša HTML vsebino s spletne strani Studentski servis
- Zbira podatke o študentskih delih z različnih strani

2. Obdelava podatkov
- urejanje_vsebine.py: Obdeluje in čisti zbrane podatke
- Ekstrahtira ključne informacije iz HTML vsebine
- Shranjuje podatke v CSV in JSON formatih

3. Analiza podatkov
- Analiza_Podatkov.ipynb: Jupyter notebook z obsežno analizo
- Vključuje različne tipove vizualizacij:
  - Bar chart-i
  - Lollipop chart-i
  - Box plot-i
  - Scatter plot-i z regresijskimi modeli
  - Tortni diagrami

4. Statistične analize
- Pearsonov korelacijski koeficient
- Linearna regresija
- Analiza distribucije plačil
- Korelacije med različnimi spremenljivkami

PODATKI

Projekt analizira naslednje podatke o študentskih delih:
- Vrsta dela: Kategorija dela (npr. strežba, prodaja, administrativa)
- Naslov oglasa: Naziv delovnega mesta, oz. nekoliko bolj podroben opis dela
- Kraj: Lokacija dela
- Plačilo: Urna postavka v evrih
- Prosta mesta: Število razpoložljivih delovnih mest
- Trajanje: Dolžina dela
- Delovnik: Čas dela (dopoldan, popoldan, izmensko, itd.)
- Začetek dela: Datum začetka dela

NAMESTITEV IN ZAGON

Na svoj racunalnik si nalozi python verzije 3.7+
Kloniraj ta repozitorij s pomočjo ukaza git clone https://github.com/AnaRaspet/AnaRaspet_Seminarska_Naloga ki ga lahko poženeš v terminalu
premakni se v ta repozitorij z ukazom cd AnaRaspet_Seminarska_Naloga
Ustvari virtualno okolje z ukazom python -m venv venv
Zaženi virtualno okolje z ukazom source venv/bin/activate  #Na Windows: venv\Scripts\activate
namesti potrebne knjižnice z ukazom  pip install requirements.txt
Sedaj ima uporabnik na voljo več možnosti:
    - odprite Analiza_Podatkov.ipynb in poženite različne celice za različne analize
    - prenesite aktualne podatke iz interneta in jih uredite za analizo
            - z ukazom python prenos_vsebine_strani.py  prenestite vsebino strani in jo shranite v mapo vsebina
            - z ukazom python urejanje_vsebine.py to vsebino uredite in jo pretvorite v .json in .csv format
    # če na novo prenesete vsebino in jo uredite ter poženete celice v jupyter notebooku, opisi rezultatov morda nebodo skladni z vizualizaciji saj se nanašajo na trenutne podatke, podatki v času ko uporabnik ponovno pridobi podatke in jih uredi za analizo pa so drugačni


REZULTATI

Projekt omogoča:
- Analizo trga študentskih del
- Identifikacijo trendov v plačilih
- Primerjavo plačil po regijah
- Analizo povpraševanja po različnih vrstah del
- Korelacijske analize med različnimi dejavniki



AVTOR
Ana Raspet

LICENCA
Ta projekt je ustvarjen za izobraževalne namene.

KONTAKT
Za vprašanja o projektu se obrnite na avtorja.
