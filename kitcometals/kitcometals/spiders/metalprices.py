import scrapy


class MetalpricesSpider(scrapy.Spider):
    name = "metalprices"
    allowed_domains = ["www.kitco.com/market"]
    start_urls = ["http://www.kitco.com/market/"]

    def parse(self, response):
        # for item in response.xpath("//div[@class='table_container
        # spot_price']//td[contains(@id, 'PT')]").getall():
        for row in response.xpath("//div[@class='table_container spot_price']//tr"):
            yield {
                "metal": row.xpath("td[1]//text()").get(),
                "date": row.xpath("td[2]//text()").get(),
                "time": row.xpath("td[3]//text()").get(),
                "bid": row.xpath("td[4]//text()").get(),
                "ask": row.xpath("td[5]//text()").get(),
                "change": row.xpath("td[6]//text()").get(),
                "change_per": row.xpath("td[7]//text()").get(),
                "low": row.xpath("td[8]//text()").get(),
                "high": row.xpath("td[9]//text()").get(),
            }
