import pynput, pyautogui, time

message = (input("Message: "))
jumlah = int(input("Jumlah spam: "))
waktu = int(input("Selang waktu: "))

time.sleep(5)
for spam in range(jumlah):
    time.sleep(waktu)
    pyautogui.typewrite(message)
    pyautogui.press("enter")