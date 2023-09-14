import requests
from bs4 import BeautifulSoup
import pprint



def gather_information(page):
    res = requests.get(f'https://news.ycombinator.com/?p={page}')
    return BeautifulSoup(res.text, 'html.parser')

def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k:k['votes'], reverse = True)
def create_custom_hn(array, page):
    hn = array
    soup = gather_information(page)
    links = soup.select('.titleline')
    subtext = soup.select(".subtext")
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].a.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points} )
    return sort_stories_by_votes(hn)

def search_multiple_pages(start, finish):
    array = []
    for i in range(start, finish+1):
        array = create_custom_hn(array, i)
    return array

pprint.pprint(search_mu
