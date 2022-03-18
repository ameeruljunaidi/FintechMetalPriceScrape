import scrapy


class MortgageRateSpider(scrapy.Spider):
    name = "mortgage-rate"
    allowed_domains = ["www.ratehub.ca/best-mortgage-rates/5-year/fixed"]
    start_urls = ["http://www.ratehub.ca/best-mortgage-rates/5-year/fixed/"]

    def parse(self, response):
        for row in response.xpath("//div[@class='sortable-content']//tr"):
            yield {
                "rate": row.xpath("td[1]/span/span//text()").get(),
                "provider": row.xpath("td[2]/span/span[2]/span//text()").get(),
            }
