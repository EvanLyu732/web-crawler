import requests
import re
from bs4 import BeautifulSoup


class Crawler:
    """
    Crawler defined
    """

    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, "html.parser")

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return "\n".join([elem.get_text() for elem in selectedElems])
        return " "

    def crawl(self):
        """
        Get pages from website home page
        """
        bs = self.getPage(self.site.url)
        targetPages = bs.findAll("a", href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs["href"]
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = "{}{}".format(self.site.url, targetPage)
                self.parse(targetPage)


class Website:
    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


reuters = Website(
    "Reuters",
    "https://www.reuters.com",
    "^(/article/)",
    False,
    "h1",
    "div.StandardArticleBody_body_ignLA",
)
crawler = Crawler(reuters)
crawler.crawl()
