# Wenyu She

import pyautogui
import time
from datetime import datetime
import webbrowser
from selenium import webdriver

# settings:
auto = True
row = 1
col = 4
item = [400 + row*130, 300 + col*130]


def find_and_click(images, conf, seconds):
    x = 0
    click = True
    while image(images, conf) == None:
        print(1)
        x += 1
        if x > seconds:
            click = False
            break
    if click:
        pyautogui.click(image(images, conf))
        time.sleep(0.1)


def image(target, conf):
    coordinates = None
    count = 0
    while coordinates == None and count < 5:
        coordinates = pyautogui.locateCenterOnScreen(target, grayscale=True, confidence=conf)
        count += 1
    return coordinates


def select_item():
    while image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\previous_item.png", .9) != None:
        time.sleep(0.4)
        pyautogui.click(430, 370)
        time.sleep(0.4)
    pyautogui.click(item)


def shirt_size():
    pyautogui.moveTo(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_add_cart.png", .8))
    pyautogui.click(pyautogui.move(0, -40))
    pyautogui.press(["down", "down", "down", "enter"])


def main():
    if auto:
        while True:
            if datetime.now().minute == 8 and datetime.now().second == 00:
                # (replace), comment method depending on item
                select_item()
                break
    while True:
        if image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_add_cart.png", .8) != None:
            # replace method depending on item
            shirt_size()
            pyautogui.click(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_add_cart.png", .8))
            break
    while image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_checkout.png", .8) == None:
        print(1)
    pyautogui.click(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_checkout.png", .8))
    find_and_click(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_card.png", .9, 15)
    pyautogui.click(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_visa.png", .9))
    pyautogui.click(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_cvv.png", .9))
    time.sleep(0.05)
    # input CVV:
    pyautogui.write("  ")
    time.sleep(0.05)
    pyautogui.click(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_terms.png", .9))
    time.sleep(0.1)
    pyautogui.scroll(-100)
    time.sleep(0.2)
    pyautogui.click(image(r"C:\Users\mail4\PycharmProjects\Supreme_Bot\sup_pay.png", .8))


if __name__ == '__main__':
    main()


