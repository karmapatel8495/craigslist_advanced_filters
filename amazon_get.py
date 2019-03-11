from bs4 import BeautifulSoup
import requests
from collections import namedtuple

base_url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='


def organic_results(results):
    for res in results:
        sponsored_tag = res.find('h5')
        if sponsored_tag and sponsored_tag.string == 'Sponsored':
            continue
        else:
            yield res


def get_amazon_results(keywords, base_url=base_url, max_results=5):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    url = base_url + '+'.join(keywords)
    amzn_page = requests.get(url, headers=headers, timeout=5)
    amzn_page.raise_for_status()

    full_soup = BeautifulSoup(amzn_page.content, 'lxml')

    no_result = full_soup.find('div', id='centerPlus').find('h1', id='noResultsTitle')
    if no_result:
        print('No results found!')
        return "NO RESULTS FOUND"

    Result = namedtuple('Result', ['res_url', 'res_title'])
    res_list = []

    result_box = full_soup.find('ul', id="s-results-list-atf")
    all_results = result_box.find_all('li')
    len(all_results)

    for num, result in enumerate(organic_results(all_results)):
        result_tag = result.find('a', class_=('a-link-normal s-access-detail-page '
                                                  's-color-twister-title-link a-text-normal'))
        res_url = result_tag['href']
        res_title = result_tag['title']
        res_list.append(Result(res_url, res_title))
        if (num + 1) >= max_results:
            break

    return res_list


if __name__ == 'main':
    print('PS4: Results\n')
    print(get_amazon_results(['PS4'], base_url, max_results=3))

    print('Leica M3 Body\n')
    print(get_amazon_results(['Leica', 'M3', 'Body'], base_url, max_results=3))

    print('Magic Chef Stove Knobs And Back Plates\n')
    print(get_amazon_results(['Magic', 'Chef', 'Stove', 'Knobs', 'And', 'Back', 'Plates'],
                             base_url,
                             max_results=3))

# keywords = ['PS4']
# keywords = ['Leica', 'M3', 'Body']
# keywords = ['Unlocked', 'Samsung', 'Galaxy', 'S7']
# keywords = ['Salzburg', 'Music', 'Center', 'Not', 'just', 'a',
#             'record', 'player', 'play', 'tapes', 'CD%27s', 'Plus']
# keywords = ['Magic', 'Chef', 'Stove', 'Knobs', 'And', 'Back', 'Plates']

print(get_amazon_results(['PS4'], base_url, max_results=3))
print(get_amazon_results(['Leica', 'M3', 'Body'], base_url, max_results=3))
