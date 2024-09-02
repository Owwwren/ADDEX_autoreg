from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Login.login import login_peg, clear_login_peg

from config import init_driver, check_find_element, find_element_and_registr, for_find_element


def addex_script(source_driver, target_page, debug=False, capcha=False,
                 class_name=None, element_name=None,
                 class_button_reg=None, element_button_reg=None,
                 elemetn_error_reg=None, class_error_reg=None,
                 email=None, login=False,
                 password1=None, password2=None,
                 user_name=None, first_name=None, nickname=None,
                 click_about=None,
                 protection=None, target_protection=None):
    #Импортирование драйвера
    driver = init_driver(source_driver, debug=debug)

    #Подключение к странице
    driver.get(target_page)

    # for_find_element(driver, debug=debug, capcha=capcha,
    #                 class_name=class_name, element_name=element_name,
    #                 class_button_reg=class_button_reg, element_button_reg=element_button_reg,
    #                 elemetn_error_reg=elemetn_error_reg, class_error_reg=class_error_reg,
    #                 email=email, login=login,
    #                 password1=password1, password2=password2,
    #                 user_name=user_name, first_name=first_name, nickname=nickname,
    #                 click_about=click_about,
    #                 protection=protection, target_protection=target_protection)






    time.sleep(1)

    #Поиск и проверка элемента на странице
    if check_find_element(driver, debug=debug, class_name=class_name, element_name=element_name) == True:
        find_element_and_registr(driver, debug=debug,
                             class_name=class_name, element_name=element_name,
                             email=email, login=login,
                             password1=password1, password2=password2,
                             user_name=user_name, first_name=first_name, nickname=nickname,
                             click_about=click_about)
        while True:
            if capcha == True:
                WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
            find_element_and_registr(driver, debug=debug,
                                    class_name='By.CSS_SELECTOR', element_name='.buttons .header__auth')
            time.sleep(5)
            if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name='error_text') == False:
                print("Успешная регистрация!")
                break
            if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name='error_text') == True:
                clear_login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=password2,
                        user_name=user_name, first_name=first_name, nickname=nickname)
                login_peg(driver, debug=debug, email=email, login=login,
                        password1=password1, password2=password2,
                        user_name=user_name, first_name=first_name, nickname=nickname)

    elif check_find_element(driver, debug=debug, class_name=class_name, element_name=element_name) == False:
        print("Возможна у сайта защита от БОТОВ. Попытка обхода защиты, ожидайте 60 секунд.")
        time.sleep(60)
        if check_find_element(driver, debug=debug, class_name=class_name, element_name=element_name) == True:
            find_element_and_registr(driver, debug=debug,
                                class_name=class_name, element_name=element_name,
                                email=email, login=login,
                                password1=password1, password2=password2,
                                user_name=user_name, first_name=first_name, nickname=nickname,
                                click_about=click_about)
            while True:
                if capcha == True:
                    WebDriverWait(driver, timeout=180).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".captcha-solver-info"), text_="Капча решена!"))
                find_element_and_registr(driver, debug=debug,
                                        class_name='By.CSS_SELECTOR', element_name='.buttons .header__auth')
                time.sleep(5)
                if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name='error_text') == False:
                    print("Успешная регистрация!")
                    break
                if check_find_element(driver, debug=debug, class_name='By.CLASS_NAME', element_name='error_text') == True:
                    clear_login_peg(driver, debug=debug, email=email, login=login,
                            password1=password1, password2=password2,
                            user_name=user_name, first_name=first_name, nickname=nickname)
                    login_peg(driver, debug=debug, email=email, login=login,
                            password1=password1, password2=password2,
                            user_name=user_name, first_name=first_name, nickname=nickname)
        else:
            print('Стоит защита которую БОТ не может обойти')









        # description
        # Мы
        # зафиксировали
        # подозрительный
        # трафик, исходящий
        # из
        # вашей
        # сети.