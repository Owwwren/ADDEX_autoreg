from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Login.login import login_peg
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Login.login import login_peg, clear_login_peg

def init_driver(source_driver=None, debug=False):
    driver = source_driver
    if debug == True:
        if driver is None:
            print('Ошибка передачи Driver!')
            return False
        else:
            print('Driver Успешно передан!')
    return driver

def check_find_element(source_driver=None, debug=False, class_name=None, element_name=None):
    driver = source_driver
    if driver is None:
        print('Driver не задан!')
        driver.close()
        driver.quit()
    else:
        if class_name == 'By.XPATH':
            try:
                element = driver.find_element(By.XPATH, element_name)
                if debug == True:
                    print(f"{class_name}. Элемент {element_name} найден!")
            except NoSuchElementException:
                if debug == True:
                    print(f"Ошибка {class_name}. Элемент {element_name} не найден!")
                return False
            return True
        elif class_name == 'By.CSS_SELECTOR':
            try:
                element = driver.find_element(By.CSS_SELECTOR, element_name)
                if debug == True:
                    print(f"{class_name}. Элемент {element_name} найден!")
            except NoSuchElementException:
                if debug == True:
                    print(f"Ошибка {class_name}. Элемент {element_name} не найден!")
                return False
            return True
        elif class_name == 'By.CLASS_NAME':
            try:
                element = driver.find_element(By.CLASS_NAME, element_name)
                if debug == True:
                    print(f"{class_name}. Элемент {element_name} найден!")
            except NoSuchElementException:
                if debug == True:
                    print(f"Ошибка {class_name}. Элемент {element_name} не найден!")
                return False
            return True
        elif class_name == 'By.ID':
            try:
                element = driver.find_element(By.ID, element_name)
                if debug == True:
                    print(f"{class_name}. Элемент {element_name} найден!")
            except NoSuchElementException:
                if debug == True:
                    print(f"Ошибка {class_name}. Элемент {element_name} не найден!")
                return False
            return True
        elif class_name == 'By.LINK_TEXT':
            try:
                element = driver.find_element(By.LINK_TEXT, element_name)
                if debug == True:
                    print(f"{class_name}. Элемент {element_name} найден!")
            except NoSuchElementException:
                if debug == True:
                    print(f"Ошибка {class_name}. Элемент {element_name} не найден!")
                return False
            return True
        elif class_name is None:
            print("Ошибка выбора класса. Не выбран класс class_name=имя_класа!")
            if element_name is None:
                print("Ошибка выбора элемента. Не выбран элемент element_name=имя_элемента!")
            return False
        else:
            print(f"Ошибка выбора класса. Класса {class_name} не существует!")
            driver.close()
            driver.quit()

def find_element_and_registr(driver, debug=False,
                             class_name=None, element_name=None,
                             email=None, login=False,
                             password1=None, password2=None,
                             user_name=None, first_name=None, nickname=None,
                             click_about=None):
    if class_name == 'By.XPATH':
        try:
            driver.find_element(By.XPATH, element_name).click()
            if debug == True:
                print(f"Успешный переход по {element_name}.")
            if login == True:
                login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=password2,
                        user_name=user_name, first_name=first_name, nickname=nickname,
                        click_about=click_about)
        except NoSuchElementException:
            if debug == True:
                print(f"Ошибка перехода ({class_name}, {element_name}) !")
            driver.close()
            driver.quit()
    elif class_name == 'By.CSS_SELECTOR':
        try:
            driver.find_element(By.CSS_SELECTOR, element_name).click()
            if debug == True:
                print(f"Успешный переход по {element_name}.")
            if login == True:
                login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=password2,
                        user_name=user_name, first_name=first_name, nickname=nickname,
                        click_about=click_about)
        except NoSuchElementException:
            if debug == True:
                print(f"Ошибка перехода ({class_name}, {element_name}) !")
            driver.close()
            driver.quit()
    elif class_name == 'By.CLASS_NAME':
        try:
            driver.find_element(By.CLASS_NAME, element_name).click()
            if debug == True:
                print(f"Успешный переход по {element_name}.")
            if login == True:
                login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=password2,
                        user_name=user_name, first_name=first_name, nickname=nickname,
                        click_about=click_about)
        except NoSuchElementException:
            if debug == True:
                print(f"Ошибка перехода ({class_name}, {element_name}) !")
            driver.close()
            driver.quit()
    elif class_name == 'By.ID':
        try:
            driver.find_element(By.ID, element_name).click()
            if debug == True:
                print(f"Успешный переход по {element_name}.")
            if login == True:
                login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=password2,
                        user_name=user_name, first_name=first_name, nickname=nickname,
                        click_about=click_about)
        except NoSuchElementException:
            if debug == True:
                print(f"Ошибка перехода ({class_name}, {element_name}) !")
            driver.close()
            driver.quit()
    elif class_name == 'By.LINK_TEXT':
        try:
            driver.find_element(By.LINK_TEXT, element_name).click()
            if debug == True:
                print(f"Успешный переход по {element_name}.")
            if login == True:
                login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=None,
                        user_name=user_name, first_name=first_name, nickname=nickname,
                        click_about=click_about)
        except NoSuchElementException:
            if debug == True:
                print(f"Ошибка перехода ({class_name}, {element_name}) !")
            driver.close()
            driver.quit()
    elif class_name is None:
        print("Ошибка выбора класса. Не выбран класс class_name=имя_класа!")
        if element_name is None:
            print("Ошибка выбора элемента. Не выбран элемент element_name=имя_элемента!")
        return False
    else:
        print(f"Ошибка выбора класса. Класса {class_name} не существует!")
        driver.close()
        driver.quit()

def bypass_protection_bot(driver, debug=False, protection=None, target_protection=None):
    if protection is None:
        print('Не указано защита сайта!')
        driver.close
        driver.quit()
    if protection == 'DDoS-GUARD':
        time.sleep(10)
        if target_protection == None:
            if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name='h-captcha') == False:
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    return False
            else:
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    time.sleep(5)
                    return True
        else:
            if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name=target_protection) == False:
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    return False
            else:
                time.sleep(10)
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    time.sleep(5)
                    return True
    if protection == 'CloudFlare':
        if target_protection == None:
            if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name='h-captcha') == False:
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    return False
            else:
                time.sleep(10)
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    time.sleep(5)
                    return True
        else:
            if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name=target_protection) == False:
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    return False
            else:
                time.sleep(10)
                if check_find_element(driver, debug=debug, class_name='By.CSS_SELECTOR', element_name='.captcha-solver-info') == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                    time.sleep(5)
                    return True
                else:
                    time.sleep(5)
                    return True
    else:
        print('БОТ не может обойти эту защиту!')
        driver.close()
        driver.quit()

def for_find_element(driver, debug=False, capcha=False,
                    class_name=None, element_name=None,
                    class_button_reg=None, element_button_reg=None,
                    elemetn_error_reg=None, class_error_reg=None,
                    email=None, login=False,
                    password1=None, password2=None,
                    user_name=None, first_name=None, nickname=None,
                    click_about=False,
                    protection=None, target_protection=None):
    langht = []
    zero = True
    while True:
        if zero == True:
            var = len(langht)
        if zero == False:
            var = len(langht) + 1
        zero = False
        langht.append(var)
        if len(langht) == len(class_name):
            break
    for num in langht:
        while True:
            reload = 0
            if check_find_element(driver, debug=debug, class_name=class_name[num], element_name=element_name[num]) == True:
                find_element_and_registr(driver, debug=debug,
                                class_name=class_name[num], element_name=element_name[num],
                                email=email, login=login[num],
                                password1=password1, password2=password2,
                                user_name=user_name, first_name=first_name, nickname=nickname,
                                click_about=click_about)
                if login[num] == True:
                    confirm_registr(driver, debug=debug, capcha=capcha,
                    class_button_reg=class_button_reg, element_button_reg=element_button_reg,
                    elemetn_error_reg=elemetn_error_reg, class_error_reg=class_error_reg,
                    email=email, login=login[num],
                    password1=password1, password2=password2,
                    user_name=user_name, first_name=first_name, nickname=nickname,
                    protection=protection, target_protection=target_protection)
                break
            else:
                if bypass_protection_bot(driver, debug=debug, protection=protection, target_protection=target_protection) == True:
                    if check_find_element(driver, debug=debug, class_name=class_name[num], element_name=element_name[num]) == True:
                        find_element_and_registr(driver, debug=debug,
                                                class_name=class_name[num], element_name=element_name[num],
                                                email=email, login=login[num],
                                                password1=password1, password2=password2,
                                                user_name=user_name, first_name=first_name, nickname=nickname,
                                                click_about=click_about)
                    if login[0] == True:
                        confirm_registr(driver, debug=debug, capcha=capcha,
                                        class_button_reg=class_button_reg, element_button_reg=element_button_reg,
                                        elemetn_error_reg=elemetn_error_reg, class_error_reg=class_error_reg,
                                        email=email, login=login[num],
                                        password1=password1, password2=password2,
                                        user_name=user_name, first_name=first_name, nickname=nickname,
                                        protection=protection, target_protection=target_protection)
                        break
                    else:
                        reload = reload + 1
                        #driver.reload
                        if reload > 2:
                            print(f'Элемента {element_name[num]} не существует!')
                            driver.close()
                            driver.quit()
                            break
                else:
                    reload = reload + 1
                    #driver.reload
                    if reload > 2:
                        print(f'Элемента {element_name[num]} не существует')
                        driver.close()
                        driver.quit()
                        break

def confirm_registr(driver, debug=False, capcha=False,
                 class_button_reg=None, element_button_reg=None,
                 elemetn_error_reg=None, class_error_reg=None,
                 email=None, login=False,
                 password1=None, password2=None,
                 user_name=None, first_name=None, nickname=None,
                protection=None, target_protection=None):
    while True:
        if capcha == True:
            WebDriverWait(driver, timeout=180).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
        find_element_and_registr(driver, debug=debug,
                                 class_name=class_button_reg, element_name=element_button_reg)
        if bypass_protection_bot(debug=False, protection=protection, target_protection=target_protection) == True:
            time.sleep(5)
            if check_find_element(driver, debug=debug, class_name=class_error_reg, element_name=elemetn_error_reg) == False:
                print("Успешная регистрация!")
                break
        if check_find_element(driver, debug=debug, class_name=class_error_reg, element_name=elemetn_error_reg) == True:
            clear_login_peg(driver, debug=debug, email=email, login=login,
                            password1=password1, password2=password2,
                            user_name=user_name, first_name=first_name, nickname=nickname)
            login_peg(driver, debug=debug, email=email, login=login,
                      password1=password1, password2=password2,
                      user_name=user_name, first_name=first_name, nickname=nickname)