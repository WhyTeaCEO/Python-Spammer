import pyautogui, time

word = input('Enter Word: ')

interval = float(input('Enter interval(seconds): '))

times = int(input('How many times would you like to spam: '))

time.sleep(3)

for i in range(times):
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(interval)

print('Done')

time.sleep(3)