from serpapi import GoogleSearch
import json

def run_search(params):
    search = GoogleSearch(params)
    response = search.get_dict()
    return response

def read_serpapi_key():
    serp_api_key = None
    try:
        with open('serpapi.key', 'r') as f:
            serp_api_key = f.readline().strip()
    except:
        raise IOError('serpapi.key file not found')

    if not serp_api_key:
        raise KeyError('SerpApi key not found')
    
    return serp_api_key

def run_query(search_terms):
    key = read_serpapi_key()
    params = {
        'engine': 'duckduckgo',
        'q': search_terms,
        'cc': 'US',
        'api_key': key,
    }

    search = GoogleSearch(params);
    response = search.get_dict()
    results = None
    if 'organic_results' in response:
        results  = response['organic_results']

    return results

def main():
    params = {
        "engine": "duckduckgo",
        "q": "Tango With Django",
        "cc": "US",
        "api_key": config.SERP_API_KEY,
    }

    response = run_search(params)
    print(response)
    print('-------------')
    for k,v in response.items():
        print(k)
    
    with open('search.json', 'w') as f:
        json.dump(response, f)

if __name__ == '__main__':
    main()
