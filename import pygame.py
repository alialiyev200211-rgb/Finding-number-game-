import random

print("🎮 SON TOPISH MUSOBAQASI 🎮")
print("Kim kam urinishda topsa — o‘sha yutadi!\n")

# =========================
# 1-BOSQICH: USER TOPADI
# =========================
print("1️⃣ Bosqich: Men son o'ylayman, siz topasiz!")

number = random.randint(1, 1000)
guess = 0
user_attempts = 0

while guess != number:
    guess = int(input("Son kiriting: "))
    user_attempts += 1

    if guess > number:
        print("⬇️ Undan kichikroq")
    elif guess < number:
        print("⬆️ Undan kattaroq")
    else:
        print(f"🎉 Topdingiz! {user_attempts} ta urinishda.\n")

# =========================
# 2-BOSQICH: KOMPYUTER TOPADI
# =========================
print("2️⃣ Bosqich: Endi siz son o'ylang (1-1000), men topaman 😎")
input("Tayyor bo'lsangiz Enter bosing...")

low = 1
high = 1000
comp_attempts = 0

while True:
    guess = (low + high) // 2
    comp_attempts += 1

    print(f"🤖 Menimcha: {guess}")
    feedback = input("Javob (k = katta, kch = kichik, t = to'g'ri): ")

    if feedback == "t":
        print(f"🎉 Men topdim! {comp_attempts} ta urinishda.\n")
        break
    elif feedback == "k":
        high = guess - 1
    elif feedback == "kch":
        low = guess + 1

# =========================
# NATIJA
# =========================
print("🏁 NATIJA:")

print(f"👤 Siz: {user_attempts} ta urinish")
print(f"🤖 Kompyuter: {comp_attempts} ta urinish")

if user_attempts < comp_attempts:
    print("🏆 Siz yutdingiz!")
elif user_attempts > comp_attempts:
    print("🤖 Kompyuter yutdi!")
else:
    print("🤝 Durrang!")
