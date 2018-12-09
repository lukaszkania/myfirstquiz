#!/usr/bin/env python
import random
import time


# Question pool from my codebrainers FullStack Developer bootcamp.

# Questions about comments using in Linux terminal.
list_of_questions_1 = [
("Pokaz sciezke do biezacego katalogu:","pwd"),
("Wyswietl zawartosci katalogow:","ls"),
("Wyswietl zawartosci katalogow wraz z ukrytymi:","ls -a"),
("Wyswietl zawartosci katalogow posortowanych wedlug czasu modyfikacji","ls -t"),
("Wyswietl zawartosci katalogow w odwrotnej kolejosci sortowania:","ls -r"),
("Wyswietl zawartosci katalogow wraz z dodatkowymi informacjami w tzw. dlugim formacie:","ls -l"),
("Wyswietl strone pomocy danego polecenia","man"),
("Zmien katalog:","cd"),
("Skrot opisujacy biezacy katalog:","./"),
("Skrot opisujacy katalog nadrzedny:","../"),
("Skrot opisujacy katalog domowy:","~/"),
("Skrot opisujacy katalog root, \"korzen\" systemu plikow:","/"),
("Skrot klawiaturowy, przerywajacy dzialanie komendy/programu:","CTRL + c"),
("Skrot klawiaturowy, przeszukujacy historie wydanych komend:","CTRL + r"),
("Skrot klawiaturowy, czyszcacy terminal:","CTRL + l"),
("Tworzenie nowego katalogu:","mkdir"),
("Usuwanie katalogu:","rmdir"),
("Tworzenie nowego pliku:","touch"),
("Identyfikacja typu pliku:","type"),
("Kopiowanie plikow:","cp"),
("Przenoszenie plikow i katalogow / zmiana nazwy pliku:","mv"),
("Usuwanie pliku:","rmv"),
("Usuniecie calego katalogu:","rmv -r"),
("Przegladanie plikow - wyswietlanie zawartosci pliku na ekranie (na standardowym wyjsciu):","cat"),
("Przegladanie plikow - wyswietlanie zawartosci pliku z opcja przewijania:","more"),
("Przegladanie plikow - wyswietlanie zawartosci pliku z opcja przewijania w obie strony:","less"),
("Otwarcie edytora nano:","nano"),
("Zmiana praw dostepu do plikow:","chmod"),
("Zmiana wlasciciela pliku:","chown"),
("Uruchomienie programu:","./"),
("Lokalizowanie pliku lub folderu:","locate"),
("Wyszukiwanie plikow i folderow","find"),
("Dopasowanie do wzoru w celu wyszukiwania plikow spelniajacych podany wzor:","grep"),
("Odczytanie ilosci znakow/linii w pliku:","wc -l"),
("Sortowanie w pliku:","sort"),
("Wyswietlanie poczatku pliku:","head"),
("Wyswietlanie konca pliku:","tail"),
("Wypisywanie tekstu:","echo"),
("Wyczyszczenie terminalu:","clear"),
("Pokazanie historii komend:","history"),
("Uruchamianie skryptu:","bash")]

# Questions about Python language.
list_of_questions_2 = [("Polecenie, ktore uzywamy, aby uruchomic interpreter Pythona, w ktorym mozemy pracowac interaktywnie:","python"),
("Polecenie, ktore uzywamy, aby uruchomic interpreter Pythona, ktory m.in. koloruje skladnie oraz podpowiada mozliwe komendy i nazwy:", "ipython"),
("Metoda, ktora dodaje x do listy:",".append(x)"),
("Metoda, ktora usuwa pierwszy x z listy:",".remove(x)"),
("Metoda, ktora usuwa i zwraca ostatni element listy:",".pop()"),
("Metoda, ktora wstawia x przed elementem o indexie i:",".insert(i,x)"),
("Metoda, ktora dodaje do konca listy dodatkowa zmienna iterowalna x:",".extend(x)"),
("Metoda, ktora zwraca ilosc wystapien x w liscie:",".count(x)"),
("Metoda, ktora zwraca index pierwszego wystapienia x w liscie:",".index(x)"),
("Metoda, ktora sortuje liste rosnaco:",".sort()"),
("Metoda, ktora sortuje liste w odwroconym porzadku:",".reverse()"),
("Funkcja, ktora zwraca ilosc elementow:","len()"),
("Funkcja, ktora zwraca obiekt, bedacy odwrocona sekwencja:","reversed()"),
("Funkcja, ktora zwraca kopie posortowanej rosnaco listy:","sorted(lista)"),
("Funkcja, ktora zwraca kopie listy w odwrotnym porzadku:","sorted(lista,reverse=True)"),
("Funkcja, ktora zwraca obiekt zawierajacy indeksy i elementy sekwencji:","enumerate()")]

# All questions from all topics.
list_of_all_questions = list_of_questions_1 + list_of_questions_2



def ask_questions_from_list(list_of_questions):
    random.shuffle(list_of_questions) # Mixing order of questions.
    wrong_answers_questions = [] # List in which we save bad answers with their good answers and answers of the user.
    points = 0 # Final score of the user.
    amount_of_questions = len(list_of_questions) # Amount of questions, this variable will be used to print the final score.
     
    # Loop used to asking questions from list_of_questions. 
    for question,answer in list_of_questions:
        try:
            time.sleep(1)
            print(question)
            time.sleep(1)
            user_answ = input("Twoja odpowiedz: \n")
            if user_answ.lower().replace(" ","") == answer.lower().replace(" ",""): # Zapobieganie uzyciu w odpowiedzi duzych, malych liter lub spacji 
                time.sleep(1)
                print("Dobrze! Zdobyles punkt!\n")
                points += 1
                continue
            else:
                time.sleep(1)
                print("Zle! Poprawna odpowiedz, to: {}.\n".format(answer))
                wrong_answers_questions.append((question,answer,user_answ))
                continue
        except:
            time.sleep(1)
            print("Zle! Poprawna odpowiedz, to: {}.\n".format(answer))
            wrong_answers_questions.append((question,answer,user_answ))
            continue

    # Printing the score results.
    print("Twoj wynik, to: {}%.\n".format(str(int(points/amount_of_questions*100))))
    time.sleep(1)
    # Printing wrong answers with good answers.
    print("Bledne odpowiedzi, wraz z prawidlowymi odpowiedziami:")
    for q,a,user_answ in wrong_answers_questions:
        time.sleep(1)
        print((q[:len(q)-1] + "?"), "Prawidlowa odpowiedz: " + a + "\n" , "Twoja odpowiedz: {}.".format(user_answ))

# Program support.
decision = input("""Co chcesz zrobic? \n 1. Odpowiedziec na pytania z okreslonego tematu. \n 2. Odpowiedziec na wszystkie moduly. \n """)
if decision == str(1):
    topic = input("""Wybierz temat: \n 1. Wprowadzenie do Linuxa. \n 2. Wprowadzenie do Pythona. \n """)
    if topic == str(1):
        ask_questions_from_list(list_of_questions_1)
    elif topic == str(2):
        ask_questions_from_list(list_of_questions_2)
elif decision == str(2):
    ask_questions_from_list(list_of_all_questions)