import requests, json
from bs4 import BeautifulSoup

''' <item>
        <title>...</title>
        <link>...</link>
        <pubDate>...</pubDate>
        <comments>...</comments>
        <description>...</description>
    </item>
'''

# helper func for saving scraped list
def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)


# scraping function
def hackernews_rss():
    article_list = []
    try:
        r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')        
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            article = {
                'title': title,
                'link': link,
                'published': published
                }
            article_list.append(article)
        return save_function(article_list)
        
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)



print('Starting scraping')
hackernews_rss()
print('Finished scraping')

