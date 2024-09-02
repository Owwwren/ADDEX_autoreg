import random
import linecache
import re
import time

from selenium.webdriver.common.by import By

def login_peg(driver, debug=False, email=None, password1=None, password2=None, login=False, user_name=None,
              first_name=None, nickname=None, click_about=None):
    if login ==  True:
        if email != "":
            time.sleep(1)
            mode = random.randint(1, 3)
            mode_mode = random.randint(1, 4)
            #mode = 'test'
            if mode == 1:
                chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                number = 1
                length = random.randint(5, 12)
                for n in range(number):
                    gen_email = ''
                    for i in range(length):
                        gen_email += random.choice(chars)
            if mode == 2:
                line_count1 = sum(1 for line in open(r'E:\botreg\botreg\Login\user_name.txt'))
                num1 = random.randint(1, line_count1)
                part1 = linecache.getline(r'E:\botreg\botreg\Login\user_name.txt', num1)

                line_count2 = sum(1 for line in open(r'E:\botreg\botreg\Login\first_name.txt'))
                num2 = random.randint(1, line_count2)
                part2 = linecache.getline(r'E:\botreg\botreg\Login\first_name.txt', num2)

                if mode_mode == 1:
                    gen_email = re.sub("\n", '', f"{part1}{part2}")
                if mode_mode == 2:
                    number = random.randint(1, 999999)
                    gen_email = re.sub("\n", '', f"{part1}{part2}{number}")
                if mode_mode == 3:
                    gen_email = re.sub("\n", '', f"{part2}{part1}")
                if mode_mode == 4:
                    number = random.randint(1, 999999)
                    gen_email = re.sub("\n", '', f"{part2}{part1}{number}")
            if mode == 3:
                line_count = sum(1 for line in open(r'E:\botreg\botreg\Login\nickname.txt'))
                num = random.randint(1, line_count)
                part = linecache.getline(r"E:\botreg\botreg\Login\nickname.txt", num)
                if mode_mode == 1:
                    number = random.randint(1, 999999)
                    gen_email = re.sub("\n", '', f"{part}{number}")
                else:
                    gen_email = re.sub("\n", '', f"{part}")

            """Генерация поты после @"""
            mail = ''
            number = random.randint(0, 1)
            if number == 0:
                mail = 'mail.ru'
            else:
                mail = 'gmail.com'
            if mode == 'test':
                gen_email = 'testmail908'
                mail = '@mail.ru'

            """Ввод почты"""
            imput_email = driver.find_element(By.NAME, email)
            imput_email.send_keys(f'{gen_email}@{mail}')
            if debug == True:
                print("Почта успешно введина!")

        if password1 != None: #Генерация пароля
            time.sleep(1)
            chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            number = 1
            length = random.randint(8, 15)
            for n in range(number):
                password = ''
                for i in range(length):
                    password += random.choice(chars)

            #Ввод пароля 1
            imput_password = driver.find_element(By.NAME, password1)
            imput_password.send_keys(password)
            if debug == True:
                print("Пороль 1 успешно введен!")

        if password2 != None:  #Ввод пароля 2
            time.sleep(1)
            imput_password2 = driver.find_element(By.NAME, password2)
            imput_password2.send_keys(password)
            if debug == True:
                print("Пороль 2 успешно введен!")

        if user_name != None:  #Ввод имяни
            time.sleep(1)
            gen_user_name = "gen_user_name"
            imput_user_name = driver.find_element(By.NAME, user_name)
            imput_user_name.send_keys(gen_user_name)
            if debug == True:
                print("Имя успешно введено!")

        if first_name != None:  #Ввод фамилии
            time.sleep(1)
            gen_first_name = 'gen_first_name'
            imput_first_name = driver.find_element(By.NAME, first_name)
            imput_first_name.send_keys(gen_first_name)
            if debug == True:
                print("Фамилия успешно введена!")

        if nickname != None:  #Ввод никнейма
            time.sleep(1)
            gen_nickname = f"{user_name}{first_name}"
            imput_nickname = driver.find_element(By.NAME, nickname)
            imput_nickname.send_keys(gen_nickname)
            if debug == True:
                print("Нинейм успешно введен!")

        if click_about != None: # Нажатия на галоочку согласия
            time.sleep(1)
            accept_police = driver.find_element(By.NAME, click_about)
            accept_police.click()
            if debug == True:
                print("Галочка успешно нажата!")
        if login == False:
            print('Авторизация выключина')
        file = open('log.txt', 'a')
        file.write(
            f"{gen_email}@{mail} | {password} | {user_name} {first_name} | {nickname}\n")
        file.close()


def clear_login_peg(driver, debug=False, email=None, password1=None, password2=None, login=False, user_name=None,
              first_name=None, nickname=None):
    if login ==  True:
        if email != "":  #Стереть почту
            driver.find_element(By.NAME, email).clear()
            if debug == True:
                print("Почта успешно стерта!")
        if password1 != None:  #Стереть пароля 2
            driver.find_element(By.NAME, password1).clear()
            if debug == True:
                print("Пороль 1 успешно стерт!")

        if password2 != None:  #Стереть пароля 2
            driver.find_element(By.NAME, password2).clear()
            if debug == True:
                print("Пороль 2 успешно стерт!")

        if user_name != None:  #Стереть имяни
            driver.find_element(By.NAME, user_name).clear()
            if debug == True:
                print("Имя успешно стерто!")

        if first_name != None:  #Стереть фамилии
            driver.find_element(By.NAME, first_name).clear()
            if debug == True:
                print("Фамилия успешно стерта!")

        if nickname != None:  #Стереть никнейма
            driver.find_element(By.NAME, nickname).clear()
            if debug == True:
                print("Нинейм успешно стерт!")
        if login == False:
            print('Авторизация выключина')

        with open('log.txt', 'r') as f:
            lines = f.readlines()
            lines = lines[:-1]

        with open('log.txt', 'w') as f:
            f.writelines(lines)