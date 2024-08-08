from itemadapter import ItemAdapter
from scrape_product import settings
from scrape_product.items import ProductItem
from scrapy import Spider


class ScrapeProductPipeline:
    
    def process_item(self, item:ProductItem, spider:Spider) -> ProductItem:
        """
        Proccess the item and return the modified item
        
        
        Args:
            item (scrapy.item): take the item and process them
            spider (scrapy.Spider): 


        Returns:
            item (scrapy.item): return the modified item
        """
        
        adapter = ItemAdapter(item=item)
        
        adapter['price_inc_vat'] = self.euro_to_pkr(adapter['price_inc_vat'])
        adapter['tags'] = self.convert_str_to_list(adapter['tags'])
        
        return item
    
    
    
    def euro_to_pkr(self, value:str) -> float: 
        """
        Take the price in euro and convert it into pkr, also remove the euro symbol if present
        
        
        Args:
            value (str): a string value of euro


        Returns:
            float: return the convert value
        """
        
        return float(value.replace("£", "")) * settings.EURO_IN_PKR
        
        
        
    def convert_str_to_list(sef, tags:str)-> list[str]:
        """
        Splits a comma-separated string into a list of non-empty, stripped and lowercase tags.
        
        
        Args:
            tags (str): a tags string separated by comma
            
            
        Returns:
            list[str] : A list of cleaned and non-empty tags.
        """
        
        return [tag.strip().lower()  for tag  in tags.split(",") if len(tag.strip()) > 0]
    
    
    
    