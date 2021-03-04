from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/nancymathur/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    scrape_mars_data = {}

    url = "'https://mars.nasa.gov/news/'"
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Collect all of the news titles on the web page
    title = soup.find("div", class_='list_text')
    news_title = title.find("div", class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    
    scrape_mars_data["News title"] = news_title
    scrape_mars_data["News Paragraph"] = news_p
    # Visit the url for JPL Featured Space Image
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Click link that says full image
    browser.links.find_by_partial_text('FULL IMAGE').click()

# Sleep for few seconds to allow for page to load
    time.sleep(3)

    # Click link that says more info
    browser.links.find_by_partial_text('more info').click()
    # Sleep for few seconds to allow for page to load
    time.sleep(3)
    # Click link for the image
    browser.links.find_by_partial_text('.jpg').click()
    # Grab the browser url
    img_url = browser.url
    # Print the url of the image
    featured_image_url = 'https://www.jpl.nasa.gov' + img_url
    scrape_mars_data["image url"] = featured_image_url)

    # Visit the Mars Weather twitter account
    mars_url = 'https://twitter.com/marswxreport?lang=en'
    return listings

    # Get response from url
    response = requests.get(mars_url)

    # Create Beautiful Soup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape the latest Mars weather tweet from the page
    mars_tweet = soup.find_all('div', class_="js-tweet-text-container")
    latest_mars_tweet = mars_tweet[0].text
    print(latest_mars_tweet)

    # Save the tweet text for the weather report as a variable called mars_weather.
    for tweet in mars_tweet: 
        mars_weather = tweet.find('p').text
        if 'Sol' and 'pressure' in mars_weather:
            print(f"mars_weather = {mars_weather}")
            break
        else: 
            pass

    scrape_mars_data["weather"] = mars_weather


    #Visit the Mars Facts webpage 
    facts_url = 'https://space-facts.com/mars/'

    # Read all tables on page
    tables = pd.read_html(facts_url)

    # Display tables
    tables

    df = tables[0]
    df = df.rename(columns={0:'Mars Planet Profile', 1:''})
    df = df.iloc[1:]
    df.set_index('Mars Planet Profile', inplace=True)

    # Create variable with html table
    scrape_mars_data["table"]= df.to_html()

  
    # Get hemispheres url
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)  

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemispheres = soup.find_all('h3')

    hemisphere_image_urls = []

    for hemisphere in hemispheres:
        browser.links.find_by_partial_text(hemisphere.text).click()
        browser.links.find_by_text('Sample').click()
        time.sleep(2)
        
        hemisphere_image_urls.append({'title': hemisphere.text, 'image_url': browser.windows[1].url})
        
        browser.windows[1].close()
        browser.back()
        
    browser.quit()
    
    scrape_mars_data["hemispheres"] = hem_img_urls

    return scrape_mars_data
