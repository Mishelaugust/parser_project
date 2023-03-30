
import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()
def collect_datas(cat_type=2):

    offset = 0
    batch_size = 60
    results = []
    count = 0
    
    while True:#меняет ссылку на запросы
        for item in range(offset, offset + batch_size, 60):
            
            #отправляем запрос
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type={cat_type}&withStack=true'
            response = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )
            
            offset += batch_size
            
            data = response.json()
            
            # if data.get('error') == 2:
            #     return 'Data were collected'
             #получаем данные
            items = data.get('items')
            

            for i in items:#забираем позиции, что удовлетворяют наши потребности
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')
                    
                    results.append(
                        {
                            'название': item_full_name,
                            '3d': item_3d,
                            'скидка': f'{item_over_price}%',
                            'цена': f'{item_price}$',
                            'цена со скидкой' : f'{item_price+((item_price*item_over_price)/100)}'

                        }
                    )
                    
        count += 1
        print(f'Page #{count}')


        if len(items) < 60:
            break
    
    
    with open(f'data{cat_type}.txt', 'w', encoding='utf-8') as f: json.dump(results, f, ensure_ascii=False)   
    
    with open(f'result{cat_type}.json', 'w', encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)
    
    
#def main():
    #print(collect_datas())
    
    
#if __name__ == '__main__':
 #   main()


# def collect_datas(cat_type=2):
# #     response = requests.get(url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=60&sort=botFirst&type=2&withStack=true',
# #     headers={'user-agent':f'{ua.random}'}
# #     )

# #     with open('text_result','w',encoding="utf-8") as file:
# #         json.dump(response.json(), file,indent=4,ensure_ascii=False)
#     offset = 0
#     size_parts = 60
#     results = []

#     while True:
#         for item in range(offset,offset+size_parts, 60):#меняет ссылку на запросы
#             url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={item}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type={cat_type}&withStack=true'
#             respons = requests.get(#отправляем запрос
#                 url=url,
#                 headers={'user-agent':f'{ua.random}'}
#             )

#             offset += size_parts

#             #получаем данные
#             data = respons.json()
#             Items = data.get('items')
            
#             for i in Items:#забираем позиции, что удовлетворяют наши потребности
#                 if i.get('overprise') is not None and i.get('overprise') < -10:
#                     item_name = i.get('fullName')
#                     link_3d = i.get('3d')
#                     price = i.get('price')
#                     over_price  = i.get('overprice')

#                     results.append(
#                         {
#                             'название': item_name,
#                             '3d': link_3d,
#                             'скидка' : over_price,
#                             'цена скина' : price
#                         }

#                     )
                    
#         if len(Items) < 60:
#             break

#     #print(results)
#     with open('otchyot.json','w',encoding="utf-8") as file:
#         json.dump(results, file,indent=4,ensure_ascii=False) 





# def main():
#     collect_datas()
    

# if __name__ == '__main__':
#     main()