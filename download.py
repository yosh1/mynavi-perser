# coding: utf-8

from selenium import webdriver
from time import sleep

import password


ENTRY_USER_LIST_URL = "https://baito.mynavi.jp/client/entry/EntryUserList.do?searchConditionReadStatus=1"


def main():
    # Chromeをシークレットウィンドウで開く
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # 指定URLにアクセス
    driver.get(ENTRY_USER_LIST_URL)

    # ログイン
    element = driver.find_element_by_name('accountCd')
    element.send_keys(password.USER)
    element = driver.find_element_by_name('password')
    element.send_keys(password.PASSWORD)
    element = driver.find_element_by_id('loginButton')
    element.click()

    # ダウンロードボタンクリック
    element = driver.find_element_by_class_name('downloadEntries')
    element.click()

    # ダウンロード完了まで待つ
    sleep(10)


if __name__ == "__main__":
    main()
