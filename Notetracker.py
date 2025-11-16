def menu_anzeige():

    print('====================================')
    print('         NOTEN-TRACKER')
    print('====================================')
    print('1) Note bearbeiten')
    print('2) Note hinzufügen')
    print('4) Alle Fächer anzeigen')
    print('5) speichern und beenden')
    print('====================================')




menu_anzeige()

def user_auswahl_menu():
    
    choice = input("Bitte Auswahl eingeben (1-5): ")
    return choice

user_auswahl_menu()

def menu_funktionen():
    
    while True:
        menu_anzeige()
        choice = user_auswahl_menu()

        if choice == "1":
            print(">> [Platzhalter] Noten eines Fachs ansehen / bearbeiten.\n")

        elif choice == "2":
            print(">> [Platzhalter] Neue Note hinzufügen.\n")

        elif choice == "4":
            print(">> Alle Fächer und ihre Durchschnitte:")
            for subject, notes in grades.items():
                avg = calculate_average(notes)
                if avg is None:
                    print(f"- {subject}: keine Noten vorhanden")
                else:
                    print(f"- {subject}: Durchschnitt = {avg:.2f}")
            print()

        elif choice == "5":
            print("Programm wird beendet. Daten werden gespeichert (später).")
            break

        else:
            print("Ungültige Eingabe, bitte 1–5 eingeben.\n")

menu_funktionen()



