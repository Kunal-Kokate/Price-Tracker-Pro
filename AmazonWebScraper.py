# Amazon Web Scraper
# by Kunal Kokate and help from Google, Stack Overflow

#importing the libraries we will need 
from bs4 import BeautifulSoup 
import requests

def main(URL):
    # Creating and opening a CSV file to store the data, and adding to it for later
    File = open("result.csv", 'a')

    # declared Header and added a user agent. This ensures that the target website we are going to web scrape 
    # doesn’t consider traffic from our program as spam and finally get blocked by them. 
    HEADERS = ({'User-Agent': 
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15',
                'Accept-Language': 'en-US, en;q=0.5'})

    # here we are making the http request
    webpage = requests.get(URL, headers=HEADERS)

    # we are creating the soup object that contains all the data
    soup = BeautifulSoup(webpage.content, 'lxml')

    # getting the product title
    try:
        title = soup.find('span', attrs={'id': 'productTitle'})
        title_value = title.string
        title_string = title_value.strip().replace(',', '')
    except AttributeError:
        title_string = 'N/A'
    print('Product Title: ', title_string)

    # saving the product title in the file
    File.write(f"{title_string},")

    # getting the price
    try:
        price = soup.find("span", attrs = {'class':'aok-offscreen'}).string.strip().replace(',', '')
    except AttributeError:
        price = "N/A"
    print('Product Price = ', price)

    # saving the product price in the file
    File.write(f"{price},")

    # getting the product rating
    try:
        rating = soup.find("i", attrs = {'class':'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
        except: 
            rating = "N/A"
    print('Overall Rating = ', rating)

    # saving the rating in the file
    File.write(f"{rating},")

    #getting the review count
    try:
        review_count = soup.find("span", attrs = {'id':'acrCustomerReviewText'}).string.strip().replace(',', '')
    except AttributeError:
        review_count = "N/A"
    print('Total Reviews = ', review_count)

    # saving the review count in the file
    File.write(f"{review_count},")

    # getting the availability status
    try:
        available = soup.find("div", attrs = {'id':'availability'})
        available = available.find('span').string.strip().replace(',', '')
    except AttributeError:
        available = "N/A"
    print('Availability = ', available)

    # saving the availability in the file
    File.write(f"{available},\n")

    #closing the file
    File.close()

# reading the urls.txt file which contains the amazon links, and then runs each link in the main function
if __name__ == '__main__':
    file = open('urls.txt', 'r')
    for links in file.readlines():
        main(links)