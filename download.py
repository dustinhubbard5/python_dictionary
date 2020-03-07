import requests
example_dictionaries = { "1": {"id":"jg_chemical-toxicity-and-the-baby-bust_2-20", "url":"https://www.gmo.com/globalassets/articles/viewpoints/2020/jg_chemical-toxicity-and-the-baby-bust_2-20.pdf", "pub_date":"2020-03-07", "add_date":"2020-03-07", "type":"PDF"},
                "2": {"id":"Looking-for-Easy-Games-in-Bonds", "url":"https://www.bluemountaincapital.com/wp-content/uploads/2019/04/Looking-for-Easy-Games-in-Bonds.pdf", "pub_date":"2020-03-07", "add_date":"2020-03-07", "type":"PDF"},}
for key,dictionary in example_dictionaries.items():
    print(dictionary)
    url = dictionary['url']
    file_name = dictionary['id']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    response = requests.request("GET", url,headers=headers)
    with open(dictionary['id']+'.pdf', 'wb') as outfile:
        outfile.write(response.content)