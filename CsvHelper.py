import csv

class CsvHelper:
    def wczytaj_dane(self, plik_csv, etykiety = True):
        dane = []
        etykiety_kolumn = []

        with open(plik_csv, 'r') as plik:
            for linia in plik:
                wiersz = linia.strip('\n').replace('"', '').split(';')

                if etykiety:
                    etykiety_kolumn = wiersz
                    etykiety = False
                else:
                    dane.append(wiersz)

        return dane, etykiety_kolumn
    
    def czy_to_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def wypisz_etykiety(self, plik_csv):
        with open(plik_csv, 'r') as plik:
            for linia in plik:
                wiersz = linia.strip('\n').replace('"', '').split(';')
                break # tylko pierwsza linia

        if self.czy_to_number(wiersz[0]):
            print('Brak etykiet w danym datasecie')
        else:
            print('Etykiety w pliku csv:')
            for etykieta in wiersz:
                print(etykieta)

    def wypisz_dane(self, dane, start=None, koniec=None):    
        if start is None and koniec is None:
            for line in dane:
                print(line)
        else:
            for line in dane[start:koniec]:
                print(line)

    
    def podziel_dane(self, dane, procent_treningowy, procent_testowy):
        rozmiar = len(dane)
        rozmiar_treningowy = int(rozmiar * procent_treningowy)
        rozmiar_testowy = int(rozmiar * procent_testowy)

        dane_treningowe = dane[:rozmiar_treningowy]
        dane_testowe = dane[rozmiar_treningowy : rozmiar_treningowy + rozmiar_testowy]
        dane_walidacyjne = dane[rozmiar_treningowy + rozmiar_testowy:]

        return dane_treningowe, dane_testowe, dane_walidacyjne
    
    def wypisz_liczebnosc_klas(self, dane):
        counts = {
            '0': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': 0
        }

        for i in range(len(dane)):
            quality = dane[i][-1]
            counts[quality] += 1

        return counts
    
    def wypisz_dane_dla_klasy(self, dane, quality):
        lista = []
        
        for wiersz in dane:
            if wiersz[-1]==quality:
                lista.append(wiersz)

        return lista
    
    def zapisz_do_pliku(self, nazwa_pliku, dane, etykiety=None):
        with open(nazwa_pliku, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            if etykiety is not None:
                writer.writerow(etykiety)

            writer.writerows(dane)