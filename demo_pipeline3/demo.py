import requests


def demo():
    res = requests.get('http://www.baidu.com')
    print(res.content)


if __name__ == '__main__':
    demo()