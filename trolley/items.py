from __future__ import unicode_literals
from scrapy.item import Item, Field

class ShopItem(Item):
    name = Field()
    price = Field()
    extra_info = Field()