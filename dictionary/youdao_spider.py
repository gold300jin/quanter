import requests
from bs4 import BeautifulSoup


class youdaoSpider():

    web_url = u'http://dict.youdao.com/search?keyfrom=dict.top&q='
    result = {
    }

    def __init__(self, word):
        self.word = word

    def get_result(self):
        r = requests.get(self.web_url + self.word)
        r.raise_for_status()
        self.prase_html(r.text)

    def prase_html(self, html):
        soup = BeautifulSoup(html)
        root = soup.find(id='results-contents')
        keyword = root.find(class_='keyword')

        basic = root.find(id='phrsListTab')
        if basic:
            trans = basic.find(class_='trans-container')
            if trans:
                self.result['basic'] = {}
                for tran in trans.find_all('li'):
                    print(str(tran.string))
                self.result['basic']['explains'] = [str(tran.string) for tran in trans.find_all('li')]


if __name__ == '__main__':
    test = youdaoSpider('black')
    test.get_result()
