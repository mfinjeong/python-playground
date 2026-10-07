import random
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def loading(text):
    print(text, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()

def bar(value):
    filled = int(value / 100 * 20)
    return "█" * filled + "░" * (20 - filled)

clear()

print("=" * 45)
print("          FRIENDSHIP CALCULATOR")
print("=" * 45)

name1 = input("\nNama pertama : ")
name2 = input("Nama kedua   : ")

print("\nJawab dengan angka 1 - 5")
print("1 = nggak sama sekali")
print("2 = jarang")
print("3 = kadang")
print("4 = sering")
print("5 = banget")

questions = [
    "Sering ngobrol?",
    "Punya humor yang sama?",
    "Nyaman ngobrol hal random?",
    "Sering melakukan sesuatu bareng?",
    "Saling membantu kalau ada masalah?",
    "Bisa saling roasting tanpa baper?",
    "Punya selera musik yang mirip?",
    "Tetap ngobrol walau lama nggak ketemu?",
    "Saling percaya?",
    "Bisa menyelesaikan masalah tanpa ribut?"
]

answers = []

for i, question in enumerate(questions, 1):
    while True:
        try:
            answer = int(input(f"\n{i:02}. {question}\n> "))
            if 1 <= answer <= 5:
                answers.append(answer)
                break
            print("Pilih angka 1 sampai 5.")
        except ValueError:
            print("Masukkan angka.")

loading("\nMenghitung")
loading("Mencocokkan")
loading("Menganalisis")

score = round((sum(answers) / 50) * 100)
score = max(0, min(100, score + random.randint(-3, 3)))

conversation = round((answers[0] + answers[2] + answers[7]) / 15 * 100)
humor = round((answers[1] + answers[5]) / 10 * 100)
activity = round((answers[3] + answers[6]) / 10 * 100)
trust = round((answers[4] + answers[8] + answers[9]) / 15 * 100)
chaos = random.randint(20, 100)

clear()

print("=" * 45)
print("              RESULT")
print("=" * 45)

print(f"\n{name1}  +  {name2}")
print(f"\nFriendship : {score}%")
print(bar(score))

print("\nConversation")
print(f"{conversation}%  {bar(conversation)}")

print("\nHumor")
print(f"{humor}%  {bar(humor)}")

print("\nActivities")
print(f"{activity}%  {bar(activity)}")

print("\nTrust")
print(f"{trust}%  {bar(trust)}")

print("\nChaos")
print(f"{chaos}%  {bar(chaos)}")

print("\n" + "-" * 45)

if score >= 90:
    print("LEGENDARY DUO")
    print("Kalian udah kayak satu paket.")

elif score >= 80:
    print("BEST FRIEND MATERIAL")
    print("Chemistry kalian kuat.")

elif score >= 70:
    print("SOLID FRIENDS")
    print("Cocok dan cukup nyaman satu sama lain.")

elif score >= 60:
    print("GOOD FRIENDS")
    print("Lumayan solid.")

elif score >= 45:
    print("CASUAL FRIENDS")
    print("Masih cocok buat ngobrol sesekali.")

elif score >= 30:
    print("IT'S COMPLICATED")
    print("Kadang cocok, kadang beda server.")

else:
    print("WHO ARE YOU TWO?")
    print("Kalian yakin saling kenal?")

if chaos >= 85:
    print("\nWARNING: duo ini terlalu berbahaya.")

if humor >= 85:
    print("Kemungkinan punya banyak inside joke.")

if trust >= 85:
    print("Trust level tinggi.")

print("\n" + "=" * 45)
input("Enter untuk keluar...")