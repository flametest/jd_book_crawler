from scrapy.spider import Spider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from JDCrawler.items import JdcrawlerItem

class BookSpider(Spider):
	"""docstring for BookSpider"""
	name = "book_price"
	allowed_domains = ["jd.com"]
	start_urls = [
	"http://book.jd.com/"
	]
	rules = [Rule(SgmlLinkExtractor(allow=['item.jd.com/\d+']), 'parse')]

	def parse(self, response):
		sel = Selector(response)
		book = JdcrawlerItem()
		book["book_title"] = sel.xpath("//div[@id='name']/h1/text()[1]").extract()
		book["isbn_no"] = sel.xpath("//ul/li[@id='summary-isbn']/div[@class='dd']/text()").extract()
		book["book_price"] = sel.xpath("//div[@class='dd']/strong/text()").extract()
		return book
