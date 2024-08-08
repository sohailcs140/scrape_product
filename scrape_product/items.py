from scrapy import Item, Field
from scrape_product import settings

def euro_to_pkr_serializer(value:str) -> float:
    """
    Take the price in euro and convert it into pkr, also remove the euro symbol if present
    
    
    Args:
        value (str): a string value of euro


    Returns:
        float: return the convert value
    """
    
    return round(float(value.replace("£", "")) * settings.EURO_IN_PKR, 3)
    


class ProductItem(Item):
    
    tags = Field()
    rs_stock_no = Field()
    mfr_part_no = Field()
    brand = Field(serializer=str.lower)
    price_exc_vat = Field(serializer=lambda value : f"PKR {euro_to_pkr_serializer(value)}")
    price_inc_vat = Field(serializer=lambda value:"{0} {1}".format("PKR", round(value, 3)))
    stock = Field()
    image = Field()