import json

import requests

def main():
    URL = 'http://127.0.0.1:8000/students'

    r = requests.get(url=URL)
    data = r.json()
    print(data)

def main2():
    URL = 'http://127.0.0.1:8000/student-create'
    data = {
        'name' : 'risalat'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)
    # data = r.json()
    # print(data)
if __name__ == '__main__':
    main()
    # main2()
