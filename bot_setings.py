from Proxy.Generate import gen_proxy
from selenium import webdriver
from Proxy.Proxy_login_script import get_login_proxy
from multiprocessing import Pool
from fake_useragent import UserAgent

from Addex.handler import addex_script

import os
import time

quantity_autoreg = 2500
count = 0
execution = []
while True:
    count = count + 1
    lst = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
    execution.append(lst)
    if count == quantity_autoreg:
        break
print(execution)

#Создание опций драйвера
def get_chromdriver(use_proxy=False, login_proxy=False, debug_proxy=False,
                    captha=False, fake_useragent=False, off_webdriver=False, headless=False):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy == True: #Использование пркси вкл/выкл
        if login_proxy == False:     #proxy без логина и пороля
            chrome_options.add_argument(f"--proxy-server={gen_proxy(debug=debug_proxy)}")
        elif login_proxy == True:     #proxy с логином и поролем
            get_login_proxy(debug=debug_proxy)
            plugin_file = 'Proxy/proxy_auth_plugin.zip'
            chrome_options.add_extension(plugin_file)
    if captha == True: #Использование инструмента КАПЧА в хроме вкл/выкл
        _path = os.path.abspath("Captcha")
        chrome_options.add_argument(f'--load-extension={_path}')
    if fake_useragent == True: #Использование фэйкового user agent вкл/выкл
        chrome_options.add_argument(f'--user-agent={UserAgent().random}')
    if off_webdriver == True: #Отключение отображения WEB Driver для сайтов
        chrome_options.add_argument(f'--disable-blink-features=AutomationControlled')
    if headless == True:
        print('print')
        chrome_options.add_argument('headless')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_data(url):
    ############настройки################
    target_page = 'https://addexref.work/r/ref/111158' #'https://pr-cy.ru/technologies/ddos-guard/'   #Ссылка на сайт | если нет то None (!!!Уйдет в ошибку!!!)
    debug = True   #False
    protection = 'DDoS-GUARD'   #DDoS-GUARD, CloudFlare | если нет то None
    target_protection = None   #class расположения элемена для отслежки защиты | если нет то None

    element_name = 'hero__start' #[]
    class_name = 'By.CLASS_NAME' #[]
    login = True   #False[]
    element_button_reg = '.buttons .header__auth'
    class_button_reg = 'By.CSS_SELECTOR'
    elemetn_error_reg = 'error_text'
    class_error_reg = 'By.CLASS_NAME'

    capcha = True   #False
    email = 'email'   #class расположения ввода майла | если нет то None
    password1 = 'password1'   #class расположения ввода пароля 1 | если нет то None
    password2 = 'password2'   #class расположения ввода пароля 2 | если нет то None
    user_name = None   #class расположения ввода имяни | если нет то None
    first_name = None   #class расположения ввода фамилии | если нет то None
    nickname = None   #class расположения ввода никнейма | если нет то None
    click_about = 'agree'   #class расположения галочки | если нет то None
    ############Логика################




    try:
        if debug == True:
            print("#########################")
            print("###Режим Debug ключен!###")
            print("#########################")
            print("")
            print("")

        driver = get_chromdriver(use_proxy=True, login_proxy=False, debug_proxy=debug,
                                 captha=capcha, fake_useragent=False, off_webdriver=True, headless=False)
        driver.get(url)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        addex_script(driver, target_page=target_page, debug=debug, capcha=capcha,
                      class_name=class_name, element_name=element_name,
                      element_button_reg=element_button_reg, class_button_reg=class_button_reg,
                      elemetn_error_reg=elemetn_error_reg, class_error_reg=class_error_reg,
                      email=email, login=login,
                      password1=password1, password2=password2,
                      user_name=user_name, first_name=first_name, nickname=nickname,
                      click_about=click_about,
                      protection=protection, target_protection=target_protection)
    except Exception as ex:
         print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=5)
    p.map(get_data, execution)
    print("")
    print('БОТ завершил работу!')