# # 6
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'application/json, text/plain, */*',
    'device': 'pc'
}
page_count = int(input("ВВедите нужное количество страниц: "))
json_dict = {}

for i in range(1, page_count + 1):
    url = f"https://lalafo.kg/kyrgyzstan/kvartiry/arenda-kvartir/posutochnaya-arenda-kvartir?page={page_count}"
    r = requests.get(url, headers=headers)
    data = r.json()
    json_dict.update(data)

with open('lalafo_data.json', 'w', encoding='UTF-8') as file:
    json.dump(json_dict, file, indent=2, ensure_ascii=False)
with open('lalafo_data.json', 'r') as fr:
    dictData = json.load(fr)

for i in range(0, 44):
    mobile = dictData['items'][i]['mobile'] #мобильный
    price = dictData['items'][i]['price']
    adress = dictData['items'][i]['params'][0]['value']
    image = dictData['items'][i]['images'][0]['thumbnail_url']
    link = dictData['items'][i]['url']
    print(mobile)
