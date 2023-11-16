import scrapy
import os

class ExampleSpider(scrapy.Spider):
    name = "example"
    page = 0

    # This is the what we're searching for on google scholar

    # Start the initial request (Scrapy's internal function)
    def start_requests(self):
        '''
        this link is for 10 results per page. doesn't work for 20 results per page right now, returns  
        a 503 status code.
        '''
        base_url = "https://scholar.google.com/scholar?start={}&q=%22{}%22&hl=en&as_sdt=0,5".format(self.page, self.query)
        return [scrapy.Request(base_url, callback=self.parse)]
    
    
    def construct_url(self):
        return "https://scholar.google.com/scholar?start={}&q=%22{}%22&hl=en&as_sdt=0,5".format(self.page, self.query)

    '''
    Write the article title along with links in articles.csv and
    write the [CITATION]s in citations.csv. Some search results aren't
    actual research papers, they are just shown as text with [CITATION].
    '''
    def parse(self, response):
        data =[]
        print(response.request.headers.get('User-Agent'))
        size_before_writing = os.path.getsize("articles.csv") + os.path.getsize("citations.csv")

        with open("articles.csv", "a") as f:
            with open("citations.csv", "a") as c:
                for res in response.css("h3.gs_rt"):
                    try:
                        article_title = "".join(res.css("a *::text").getall())
                        article_link = res.css("a::attr(href)").get()
                        data.append({'title': article_title, 'link': article_link})
                        
                        # DB storage
                        #paper = Paper(title=article_title, link=article_link)
                        #paper.save()
                        #

                        f.write(article_title + " - " + article_link + "\n")
                    except:
                        c.write("".join(res.css("*::text").getall()) + "\n")
       
        size_after_writing = os.path.getsize("articles.csv") + os.path.getsize("citations.csv")

        '''
        Comparing file sizes before and after writing data to the files. Stop sending requests
        if the filesize doesnt change, meaning that there is no more data on the current page.
        (Used this approach because even if the page doesn't have any relevant content, it still
        is a valid webpage and the response status code is 200 so this is one of the ways to know
        if all data has been scraped.)
        # '''
        if size_before_writing < size_after_writing:
            self.page+=10
            return [scrapy.Request(self.construct_url(), callback=self.parse)]
