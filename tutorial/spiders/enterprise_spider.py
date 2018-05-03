import scrapy


class EnterpriseSpider(scrapy.Spider):
    name = "enterprise"
    allowed_domains = ["tianyancha.com"]
    start_urls = [
        "https://www.tianyancha.com/search?key=%E5%A4%A7%E8%BF%9E%E6%99%BA%E8%83%BD%E8%AE%BE%E5%A4%87"
    ]

    def parse(self, response):
        filename = "enterprise"
        with open(filename, 'wb') as f:
            f.write(response.body)
