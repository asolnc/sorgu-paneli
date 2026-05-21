import os
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo_ciz():
    print(Fore.RED + Style.BRIGHT + """
  _______ _    _ ______       _______       _______ __   __ ___  _  _ 
 |__   __| |  | |  ____|   /\|__   __|/\   |__   __\ \ / // _ \| || |
    | |  | |__| | |__     /  \  | |  /  \     | |   \ V /| | | | || |_
    | |  |  __  |  __|   / /\ \ | | / /\ \    | |    > < | | | |__   _|
    | |  | |  | | |____ / ____ \| |/ ____ \   | |   / . \ \ |_| |  | | 
    |_|  |_|  |_|______/_/    \_\_/_/    \_\  |_|  /_/ \_\\___/   |_| 
                                                                      
                    [ BY THEATATV44 ]
    """)

def dev_tc_baslik():
    print(Fore.RED + """
  _______ _____ 
 |__   __/ ____|
    | | | |     
    | | | |     
    | | | |____ 
    |_|  \_____|
                """)

def sorgu_ekrani(baslik, api_url, params_dict):
    temizle()
    if "TC" in baslik:
        dev_tc_baslik()
    
    print(Fore.RED + "--------------------------------------------------")
    print(Fore.RED + f"       {baslik} SORGULAMA PANELI")
    print(Fore.RED + "--------------------------------------------------")
    print(Fore.RED + f" Yazar: theatatv44")
    print(Fore.RED + "--------------------------------------------------")
    
    query_params = {}
    for p_name, p_label in params_dict.items():
        val = input(Fore.WHITE + f" {p_label} Giriniz: ")
        query_params[p_name] = val
    
    print(Fore.YELLOW + "\n Veritabanina baglaniliyor...")
    
    try:
        response = requests.get(api_url, params=query_params)
        if response.status_code == 200:
            print(Fore.GREEN + "\n Veriler Cekildi:")
            print(Fore.RED + "--------------------------------------------------")
            print(Fore.WHITE + response.text)
            print(Fore.RED + "--------------------------------------------------")
        else:
            print(Fore.RED + "\n [!] Sunucu hatasi: " + str(response.status_code))
    except:
        print(Fore.RED + "\n [!] Baglanti saglanamadi!")

    print(Fore.RED + "\n 1 - Yeni Sorgu")
    print(Fore.RED + " 2 - Ana Menuye Don")
    
    secim = input(Fore.WHITE + "\n Secim: ")
    if secim == '1':
        sorgu_ekrani(baslik, api_url, params_dict)
    else:
        return

def ana_menu():
    while True:
        temizle()
        logo_ciz()
        print(Fore.RED + " [1] TC -> GSM")
        print(Fore.RED + " [2] SULALE")
        print(Fore.RED + " [3] ISYERI")
        print(Fore.RED + " [4] GSM -> TC")
        print(Fore.RED + " [5] ADRES")
        print(Fore.RED + " [6] TC DETAY (Sorgu)")
        print(Fore.RED + " [7] AD SOYAD (IL/ILCE)")
        print(Fore.RED + " [8] AD SOYAD (GENEL)")
        print(Fore.RED + " [0] CIKIS")
        
        secim = input(Fore.WHITE + "\n theatatv44 > ")

        if secim == '1':
            sorgu_ekrani("TC GSM", "https://arastir.sbs/api/tcgsm.php", {"tc": "TC No"})
        elif secim == '2':
            sorgu_ekrani("SULALE", "https://arastir.sbs/api/sulale.php", {"tc": "TC No"})
        elif secim == '3':
            sorgu_ekrani("ISYERI", "https://arastir.sbs/api/isyeri.php", {"tc": "TC No"})
        elif secim == '4':
            sorgu_ekrani("GSM", "https://arastir.sbs/api/gsmtc.php", {"gsm": "GSM No"})
        elif secim == '5':
            sorgu_ekrani("ADRES", "https://arastir.sbs/api/adres.php", {"tc": "TC No"})
        elif secim == '6':
            sorgu_ekrani("TC", "https://arastir.sbs/api/tc.php", {"tc": "TC No"})
        elif secim == '7':
            sorgu_ekrani("AD SOYAD", "https://arastir.sbs/api/adsoyad.php", 
                         {"adi": "Ad", "soyadi": "Soyad", "il": "Il", "ilce": "Ilce"})
        elif secim == '8':
            sorgu_ekrani("AD SOYAD", "https://arastir.sbs/api/adsoyad.php", 
                         {"adi": "Ad", "soyadi": "Soyad"})
        elif secim == '0':
            print(Fore.RED + "\n theatatv44 kapaniyor...")
            break

if __name__ == "__main__":
    ana_menu()
    
