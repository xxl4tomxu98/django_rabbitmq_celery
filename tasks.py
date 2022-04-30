# tasks.py
from celery import Celery
import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
from celery.schedules import crontab # scheduler

# defining the app name to be used in our flag
app = Celery('tasks') 


# helper func for saving scraped list
@app.task
def save_function(article_list):
    # timestamp and filename
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename = 'articles-{}.json'.format(timestamp)
    with open(filename, 'w').format(timestamp) as outfile:
        json.dump(article_list, outfile)


# scraping function
@app.task
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
                'published': published,
                'created_at': str(datetime.now()),
                'source': 'HackerNews RSS'
                }
            article_list.append(article)
        return save_function(article_list)
        
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


# scheduled task execution
app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'tasks.hackernews_rss',
        'schedule': crontab()
    }
}