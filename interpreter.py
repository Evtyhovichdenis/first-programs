import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'YjY0YTdkOWEtYTEwMi00MWUxLTgzYjMtNGY3MGY3NTY4MTcyOmU1NmEzYWFmOTU5YTQ2ZGM4MjQ1MTg2YzY5NWIxOTE2'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

if auth.status_code == 200:
    token = auth.text

    while True:
        word = input('Введите слово для перевода: ')
        if word:
            headers_translate = {'Authorization': 'Bearer ' + token}
            params = {
                'text': word,
                'srcLang': 1049,
                'dstLang': 1031
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Не найдено вариантов для перевода')
else:
    print('Error!')
