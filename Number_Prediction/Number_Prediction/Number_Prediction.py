import random

is_range_valid = True

while is_range_valid:
    lower_bound = int(input("Araligin tabanini belirleyin: "))
    upper_bound = int(input("Araligin tavanini belirleyin: "))
    if lower_bound > upper_bound:
        print("Mantiksal hata: taban, tavandan buyuk olamaz. Lutfen tekrar belirleyin.")
    elif upper_bound == lower_bound:
        print("Mantiksal hata: taban ve tavan birbirine esit olamaz. Lutfen tekrar belirleyin.")
    elif upper_bound > lower_bound:
        is_range_valid = False
    else:
        print("Gecersiz giris. Lutfen tavan ve tabani tekrar belirleyin.")

random_number = random.randint(lower_bound, upper_bound)
is_guess_correct = True
attempt_counter = 1
print("Rastgele sayi olusturuldu.")
guess = int(input("Sayiyi tahmin etmeye calisin: "))

while is_guess_correct:
    if guess == random_number:
        print("Tebrikler!", guess, "sayisini", attempt_counter, "adimda dogru tahmin ettiniz!")
        is_guess_correct = False
    elif guess < random_number:
        attempt_counter += 1
        print(guess, "sayisindan daha yuksek bir sayi tahmin edin:")
        guess = int(input())
    elif guess > random_number:
        attempt_counter += 1
        print(guess, "sayisindan daha kucuk bir sayi tahmin edin:")
        guess = int(input())
    else:
        guess = int(input("Gecersiz ifade girdiniz, lutfen sayi giriniz: "))

