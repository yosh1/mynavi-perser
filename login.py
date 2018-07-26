# coding: utf-8

from bs4 import BeautifulSoup
import requests

import password

LOGIN_URL = "https://baito.mynavi.jp/client/login/client.do"


def main():
    session = requests.Session()
    print(login(session))


def login(session):
    payload = {
        'jsToken': '__MynaviJavaScriptToken__',
        'accountCd': password.USER,
        'password': password.PASSWORD
    }

    request = session.get(LOGIN_URL)
    soup = BeautifulSoup(request.text)
    bean = soup.find(attrs={'name': '__bean'}).get('value')
    payload['__bean'] = bean

    request = session.post(LOGIN_URL, data=payload)
    soup = BeautifulSoup(request.text)
    return soup


if __name__ == '__main__':
    main()
