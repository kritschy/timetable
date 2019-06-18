from pyquery import PyQuery as pq
import json



content = pq(url='http://stupla.osw-online.de')
content = content('body').find('center').find('table')
klasse = content("tr > td").text().split(" ")

structure = content("td:first-child")
structure = structure('a').text().split(" ")
structure = [x[:-1] for x in structure]


print(klasse)
print(structure)

result = {

    "structure": {
        k: [x for x in klasse if x.startswith(k)]
        for k in structure
    }
}

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(result, outfile, ensure_ascii=False, indent=2)
print(json.dumps(result))

def getUrl(klasse):

    url = 'http://stupla.osw-online.de/Kla1_{}.htm'.format(klasse)
    return url


for i in range(len(klasse)):
    url = getUrl(klasse[i])
