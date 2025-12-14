import os

CONTACTS_FILE = "rehber_kaydi.txt"
contacts = {}

def save_contacts():
    try:
        with open(CONTACTS_FILE ,"w" ,encoding="utf-8") as f:
            for name,details in contacts.items():
                phones_str = ";".join(details['Phone'])
                emails_str = ";".join(details['Email'])

                f.write(f"{name},{phones_str},{emails_str}\n")
        print(f"Rehber ({len(contacts)} kisi) [{CONTACTS_FILE}] dosyasina kaydedildi")

    except Exception as e:
        print(f"Kaydetme hatasi : {e}")

def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE,"r",encoding="utf-8") as f:
                temp_contacts = {}
                for line in f:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split(',',2)

                    if len(parts) == 3:
                        name, phones_str ,emails_str = parts

                        phones = phones_str.split(';') if phones_str else []
                        emails = emails_str.split(';') if emails_str else []

                        name = name.strip()
                        phones = [p.strip() for p in phones]
                        emails = [e.strip() for e in emails]

                        temp_contacts[name] = {"Phone": phones, "Email" : emails}
                contacts = temp_contacts
                print(f"[{CONTACTS_FILE}] dosyasindan {len(contacts)} kisi yuklendi.")
        except Exception as e:
            print(f"Uyari: Kayit dosyasi okunurken hata olustu ({e}). Yeni rehber olusturuluyor.")
            contacts = {}
    else:
        print("Kayit dosyasi bulunamadi, bos rehber ile basliyor.")
            
def get_multiple_inputs(prompt):
    #Kullanıcıdan birden fazla değer alır (virgülle ayrılmış)
    user_input = input(prompt).strip()
    if not user_input:
        return []
    # Virgülle ayırır, her parçayı temizler ve boş parçaları atar
    return [item.strip() for item in user_input.split(',') if item.strip()]

def show_menu():
    print("\n--- Rehber Menusu")
    print("1.Kisi ekle")
    print("2.Kisileri goruntule")
    print("3.Kisi bul")
    print("4.Kisiyi duzenle")
    print("5.Kisiyi sil")
    print("6.Kisi defterinden cik")

def add_contact():
    name = input("Eklemek istediginiz kisinin adini giriniz : ").strip()

    if not name:
        print("Hata: İsim alani bos birakilamaz.")
        return
        
    phones = get_multiple_inputs("Telefon numaralarini giriniz (Virgülle ayirarak): ")
    emails = get_multiple_inputs("Email adreslerini giriniz (Virgülle ayirarak): ")
    
    if name in contacts:
        print(f"Hata: '{name}' adli kisi rehberinizde zaten var.")
        return

    contacts[name] = {"Phone": phones, "Email": emails} 
    print(f"'{name}' adli kisi rehberinize eklendi.")

def view_contact():
    if not contacts:
        print("Rehberinizde kimse bulunmamaktadir")
        return
    else:
        print("\n---Kisiler---")
        for name,details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {', '.join(details['Phone']) if details['Phone'] else 'Yok'}")
            print(f"Email: {', '.join(details['Email']) if details['Email'] else 'Yok'}")
            print("-" * 30)

def search_contact():
    name = input("Bulmak istediginiz kisinin adini giriniz : ").strip()
    if name in contacts:
        details = contacts[name]
        print("\n---Kisi Bilgileri---")
        print(f"Name: {name}")
        print(f"Phone: {', '.join(details['Phone']) if details['Phone'] else 'Yok'}")
        print(f"Email: {', '.join(details['Email']) if details['Email'] else 'Yok'}")
    else:
        print(f"'{name}' adinda biri rehberinizde bulunamadi")

def edit_contact():
    old_name = input("Duzenlemek istediginiz kisinin adini giriniz : ").strip()
    
    if old_name not in contacts:
        print("Kisi adi rehberde bulunamadi")
        return

    details = contacts[old_name]
    
    new_name = input(f"'{old_name}' icin yeni ismi giriniz (Bos birakirsaniz degismez): ").strip()
    
    current_phones = ', '.join(details['Phone'])
    current_emails = ', '.join(details['Email'])
    
    print("\n*Telefon/E-posta değişimi için yeni listeyi virgülle girin. Değiştirmemek için boş bırakın.*")
    new_phones = get_multiple_inputs(f"Yeni telefonlar (Mevcut: {current_phones}): ")
    new_emails = get_multiple_inputs(f"Yeni emailler (Mevcut: {current_emails}): ")
    
    final_name = new_name if new_name else old_name

    if final_name != old_name:
        del contacts[old_name]
        contacts[final_name] = details

    if new_phones:
        contacts[final_name]["Phone"] = new_phones
    
    if new_emails:
        contacts[final_name]["Email"] = new_emails
    
    print(f"'{old_name}' kaydinin bilgileri basariyla guncellendi (Yeni İsim: {final_name}).")

def delete_contact():
    name = input("Silmek istediginiz kisinin adini giriniz : ")
    if name in contacts:
        del contacts[name]
        print(f"{name} Adli kisi rehberinizden basariyla silindi")
    else:
        print("Oyle bir kisi rehberinizde bulunamadi")
    
load_contacts()

while True:
    show_menu()
    choice = input("İslem yapmak istediginiz secenegin numarasini giriniz : ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contact()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        edit_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        save_contacts()
        print("Kisi rehberinden cikiliyor")
        break
    else:
        print("Hatali tuslama yaptiniz lutfen (1-6) arasinda bir tuslama yapiniz")

