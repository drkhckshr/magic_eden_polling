import json
import requests

def get_data(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    return data

def create_data(endpoints):
    listings = []
    for endpoint in endpoints:
        data = get_data(endpoint['url'])
        listing = {}
        listing['title'] = data['results']['title']
        listing['price'] = data['results']['price']
        listing['img'] = data['results']['img']
        listing['url'] = endpoint['url']
        listings.append(listing)
    return listings

def main():
    json_file = "/tmp/files/me_nfts.json"
    
    with open(json_file, 'r') as r_jf:
        json_data = json.load(r_jf)
    
    data = create_data(json_data)

    print(data)

    with open(json_file, 'w') as w_jf:
        json.dump(data, w_jf)

main()