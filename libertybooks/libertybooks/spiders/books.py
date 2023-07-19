import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["www.libertybooks.com"]
    start_urls = ["https://www.libertybooks.com/urdu-books?limit=100"]

    def parse(self, response):
        for book in response.css("div.product-details.col-lg-7.col-md-7.col-sm-7.col-xs-7 div.caption"):
            try:
                book_name = book.css("h4 a::text").get()
            except:
                book_name = None

            try:
                book_link = book.css("h4 > a::attr(href)").get()
            except:
                book_link = None

            try:
                author_name = book.css("p.author::text").get()
            except:
                author_name = None

            try:
                author_profile = book.css("> a::attr(href)").get()
            except:
                author_profile = None

            try:
                price = book.css("span.price-tax::text").get()
            except:
                price = None

            yield {
                'book_name': book_name,
                'book_link': book_link,
                'author_name': author_name,
                'author_profile': author_profile,
                'price': price
            }
        next_page = response.css('ul.pagination > li:nth-child(10) a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
