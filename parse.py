# coding: utf-8

from bs4 import BeautifulSoup


def main():
    html_data = getLocalHTML("sample/sample.html")
    soup = BeautifulSoup(html_data, "html.parser")
    tr_tag = soup.find_all("tr")
    name_list = []
    for tr in tr_tag:
        td_tag = td_dotline(tr)
        if td_tag:
            name_list.append(parse_data(td_tag))

    print(name_list)


def td_dotline(tag):
    return tag.find_all("td", class_="dotline")


def parse_data(tag):
    return [tg.text.strip() for tg in tag]


def getLocalHTML(filename):
    file = open(filename)
    return file


if __name__ == "__main__":
    main()
