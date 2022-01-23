import json
import requests

def get_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data

def create_data(data):
    listings = []
    for item in data['results']:
        listing = {}
        listing['title'] = item['title']
        listing['price'] = item['price']
        listing['img'] = item['img']
        listing['mintAddress'] = item['mintAddress']
        listings.append(listing)
    return listings, item['collectionName']

def main():
    json_file = "/tmp/files/me_nft_collections.json"
    
    with open(json_file, 'r') as r_jf:
        json_data = json.load(r_jf)
    
    url = "https://api-mainnet.magiceden.io/rpc/getListedNFTsByQuery?q=%s"
    query = {
        '$match': {
            'collectionSymbol': ''
            },
            '$sort': {
                'createdAt': -1
            },
            '$skip': 0,
            '$limit': 20
        }

    for item in json_data:
        query['$match'] = {'collectionSymbol': item['collectionName']}
        result_data = get_data(url % json.dumps(query))
        data, collection = create_data(result_data)

        for item in data:
            print(collection, item['price'], item['title'], "https://magiceden.io/item-details/{mintAddress}".format(mintAddress=item['mintAddress']))

        json_file = "/tmp/files/me_nfts_{collection}_recents.json".format(collection = collection)
        with open(json_file, 'w') as w_jf:
            json.dump(data, w_jf)

main()