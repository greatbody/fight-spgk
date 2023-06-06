import requests
import threading
import random, string

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'sec-ch-ua-mobile': '?0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

def thread_func(number: int):
    print('This is thread {} running'.format(number))
    while True:
        try:
            response = requests.get('http://shangpenggaoke.cn/cn/?.minghui.org', headers=headers)
            if response.status_code != 200:
                print('Thread {} got status code {}, Message:\n{}'.format(number, response.status_code, response.text))
        except Exception as e:
            print('Thread {} have error message {}'.format(number, e))

if __name__ == "__main__":
    print('start module')
    for i in range(50):
        x = threading.Thread(target=thread_func, args=(i,))
        x.start()
