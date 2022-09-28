import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


INSTAGRAM_DOMAIN = "https://www.instagram.com/"
CHROMEDRIVER = "driver\chromedriver.exe"
LOGIN_ID = "ユーザー名"
PASSWORD = "パスワード"
MIN_COUNT = 10

def create_driver(url):
    options = Options()
    # options.add_argument("--headless")
    service = Service(executable_path=CHROMEDRIVER)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver

def login(driver):
    elem_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username")))
    try:
        elem_password = driver.find_element(By.NAME, "password")
        if elem_id and elem_password:
            elem_id.send_keys(LOGIN_ID)
            elem_password.send_keys(PASSWORD)
            try:
                elem_btn = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "L3NKy       ")))
                print("ボタンの要素はあったで")
            except:
                print("ボタン要素がないで")
            actions = ActionChains(driver)
            actions.move_to_element(elem_btn)
            actions.click(elem_btn)
            actions.perform()
            time.sleep(4)
            perform_url = driver.current_url
            if perform_url.find("https://www.instagram.com/accounts/login/") == -1:
                # ログイン成功
                print(perform_url)
                return True
            else:
                # ログイン失敗
                print("ログイン失敗")
                print(perform_url)
                return False
        else:
            print("パスワードかidの要素が見つかりません")
            return False
    except:
        print("パスワード要素が見つかりません")
        return False


def click_info_save_button(driver):
    elem_info_save_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button._acan._acao._acas")))
    actions = ActionChains(driver)
    actions.move_to_element(elem_info_save_btn)
    actions.click(elem_info_save_btn)
    actions.perform()
    perform_url = driver.current_url
    time.sleep(10)
    if perform_url.find("https://www.instagram.com/accounts/onetap/?next=%2Fexplore%2Ftags%2Fwelcomeforster%2F") == -1:
        print(perform_url)
        return True
    else:
        print(perform_url)
        return False

def clink_alert_dialog(driver):
    try:
        elem_info_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button._a9--._a9_1")))
        actions = ActionChains(driver)
        actions.move_to_element(elem_info_btn)
        actions.click(elem_info_btn)
        actions.perform()
        print("後でのボタンを押しました")
        return
    except:
        print("お知らせを後でに設定できませんでした")
        return

def click_article(driver):
    elem_article_a = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.qi72231t.nu7423ey.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.bdao358l.fsf7x5fv.rse6dlih.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.srn514ro.oxkhqvkx.rl78xhln.nch0832m.cr00lzj9.rn8ck1ys.s3jn8y49.icdlwmnq._a6hd")))
    actions = ActionChains(driver)
    actions.move_to_element(elem_article_a)
    actions.click(elem_article_a)
    actions.perform()
    return 


def get_info_from_text(driver):
    name= ""
    text=""
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_a9zr")))
    except:
        print("そんな要素見つかりません")
        return name, text

    try:
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.qi72231t.nu7423ey.n3hqoq4p.r86q59rh.b3qcqh3k.fq87ekyn.bdao358l.fsf7x5fv.rse6dlih.s5oniofx.m8h3af8h.l7ghb35v.kjdc1dyq.kmwttqpk.srn514ro.oxkhqvkx.rl78xhln.nch0832m.cr00lzj9.rn8ck1ys.s3jn8y49.icdlwmnq._acan._acao._acat._acaw._a6hd")))
        text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span._aacl._aaco._aacu._aacx._aad7._aade")))
        return name, text
    except:
        return name, text

def next_article(driver):
    try:
        elm_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._aaqg._aaqh button")))
        actions = ActionChains(driver)
        actions.move_to_element(elm_button)
        actions.click(elm_button)
        actions.perform()
        print("次へボタンが押されました")
        return True
    except:
        print("次へボタンが押される前にエラーが発生しました")
        return False


if __name__ == "__main__":
    keywords=["cheesecheesecafe","bardelcloe","六花亭","benbencafe","カフェ美鈴","vmgcafe","wavesnow","jbハウス","吉和寿珈琲"]
    driver = create_driver(INSTAGRAM_DOMAIN)
    login(driver)
    click_info_save_button(driver)
    clink_alert_dialog(driver)
    #pandas用
    columns= ["ハッシュタグ","ユーザー名","テキスト"]

    info_all = {}
    count = 0

    for keyword in keywords:
        continue_flug = True
        count = 0
        df = pd.DataFrame(columns=columns)
        URL = "https://www.instagram.com/explore/tags/" + urllib.parse.quote(keyword) + "/"
        driver.get(URL)
        click_article(driver)
        while count < MIN_COUNT and continue_flug ==True:
            count = count + 1
            print(driver.current_url)
            name, text = get_info_from_text(driver)
            # print(name.text)
            # print(text.text)
            df=df.append({'ハッシュタグ': keyword, 'ユーザー名': name.text, 'テキスト': text.text}, ignore_index=True)
            time.sleep(4)
            continue_flug=next_article(driver)
        df.to_csv(f'output/{keyword}.csv')
        

    driver.quit()
