import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class MailsSpider(CrawlSpider):
    name = 'mails'
    allowed_domains = ['aral.de', 'shell.de', 'totalenergies.de', 'jet-tankstellen.de', 'avia.de']
    start_urls = [
        'https://www.aral.de/de/global/',
        'https://www.shell.de/',
        'https://www.totalenergies.de/',
        'https://www.jet-tankstellen.de/',
        'https://www.avia.de/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'kontakt|impressum|about|unternehmen')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        emails = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text))
        for email in emails:
            if 'bootstrap' not in email and 'example' not in email:
                yield {
                    'URL': response.url,
                    'Email': email
                }



# how to run this file : scrapy crawl mails -o emails.csv