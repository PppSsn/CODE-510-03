target = 72  # กำหนดค่าเป้าหมาย

guesses = 0  # จำนวนครั้งที่ทาย
while True:
    guess = int(input("Guess the number (0-100): "))  # รับค่าทายจากผู้ใช้

    # ตรวจสอบว่าตัวเลขที่ทายอยู่ในช่วงที่กำหนดหรือไม่
    if guess < 0 or guess > 100:
        print("Sorry, your guess is out of range")
        continue

    guesses += 1  # เพิ่มจำนวนครั้งที่ทาย

    # ตรวจสอบว่าทายตัวเลขถูกต้องหรือไม่
    if guess == target:
        print("Congratulations, your guess is correct. Total number of guesses is:", guesses)
        break
    elif guess < target:
        print("Sorry, your guess is too low")
    else:
        print("Sorry, your guess is too high")
