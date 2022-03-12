import requests


# get data from API
def extract_data_from_api():
    data = []
    base_url = "https://itunes.apple.com/search"
    response = requests.get(base_url, params={"term": "the beatles", "country": "us", "limit": 200})
    response = response.json()
    for i in range(200):
        data.append(response['results'][i])
    return data


# test function
if __name__ == '__main__':
    data = extract_data_from_api()
    print(data)
