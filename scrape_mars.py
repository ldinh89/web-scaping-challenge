from splinter import Browser
from bs4 import BeautifulSoup as soup


def scrape_all():
    executable_path = {'executable_path': "\Users\luand\.wdm\drivers\chromedriver"}
    browser = Browser("chrome", executable_path= executable_path, headless=False)
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": each_link(browser)
    }

def mars_news(browser):
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    try:
        articles = soup.find("div", class="list_text")
        news_title = articles.find("div", class_="content_title").text
        news_paragraph = articles.find('div', class_="article_teaser_body").text

    except AttributeError:
        return news_title, news_paragraph
    
