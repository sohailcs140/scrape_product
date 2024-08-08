import scrapy
from scrape_product.items import ProductItem

class ProductSpiderSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ["uk.rs-online.com"]
    start_urls = ["https://uk.rs-online.com/web/p/disposable-respirators/2012391"]

    
    def parse(self, response:scrapy.http.Response):
        """
        Extracts product information from the given response and yields a ProductItem.


        Args:
            response (scrapy.http.Response): The HTTP response object that contains the HTML data from the website.


        Yields:
            ProductItem: An item containing the product details extracted from the response 
        """


        yield ProductItem(**self.parse_product(response))
        
    
    
    def parse_product(self, response:scrapy.http.Response) -> dict:
        
        """
        Take the response object , scrape the product detail and return it as a dict
        
        
        Args: response object
        
        
        Returns:
            dict: return the scrape product as a dict
        """
        
        base_element = response.xpath("//dl[contains(@data-testid, 'key-details-desktop')]")[0]
        stock_0 = response.xpath("//div[contains(@data-testid, 'stock-status-0')]/text()").get()
        stock_1 = response.xpath("//div[contains(@data-testid, 'stock-status-1')]/text()").get()
        stock_2 = response.xpath("//div[contains(@data-testid, 'stock-status-2')]/text()").get()
        
        return {
            'brand':base_element.xpath("//dd")[2].css("::text").get(),
            'rs_stock_no':base_element.xpath("//dd")[0].css("::text").get(),
            "mfr_part_no":base_element.xpath("//dd")[1].css("::text").get(),
            "price_exc_vat":response.xpath("//p[contains(@data-testid, 'price-exc-vat')]/text()").get(),
            "price_inc_vat":response.xpath("//p[contains(@data-testid, 'price-inc-vat')]/text()").get(),
            "stock":int(stock_0) + int(stock_1) + int(stock_2),
            "image":response.xpath("//img[contains(@data-testid, 'gallery-fallback-image')]/@src").get(),
            "tags": response.xpath("//div[contains(@data-testid, 'long-description')]/h1/text()").get()
        }
    