from http import cookies
import scrapy
from scrapy import Spider
from scrapy.http import FormRequest


class TestingArgs(Spider):
    name = 'testing_args'

    def __init__(self, category=None, *args, **kwargs):
        super(TestingArgs, self).__init__(*args, **kwargs)
        print("******")
        print(category)
        print("******")


    def start_requests(self):
        login_url = 'http://quotes.toscrape.com/login'
        yield scrapy.Request(login_url, callback=self.login)

    
    def login(self, response):
        yield {}


               