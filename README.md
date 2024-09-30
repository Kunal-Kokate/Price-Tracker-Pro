

# **Summary**

The Price Tracker Pro is a python tool that extracts information from Amazon product pages, this includes product name, price, rating, number of reviews, and availability. The extracted data is then saved into a CSV file for further analysis or record-keeping




## **Features**
- Extracts product name, price, rating, number of reviews, and availability from Amazon product pages
- Saves the extracted data into a CSV file
- Utilizes BeautifulSoup for HTML parsing and requests for HTTP requests
- Employs user-agent headers to avoid being blocked by Amazon servers

  
## **Requirements**
- Python 3.x
- BeautifulSoup4
- requests
- lxml

## **Installation**
1. Clone the repository:
   ```
   git clone https://github.com/Kunal-Kokate/Amazon-Web-Scraper.git
   cd Amazon-Web-Scraper
   ```
2. Install the required libraries:
   ```
   pip install beautifulsoup4 requests lxml
   ```
3. In the urls.txt file add some Amazon product URLs you want to scrape, one per line.

   
## **Usage**
1. Run the script:
   ```
   python AmazonWebScraper.py
   ```
2. The script will read the URLs from the urls.txt file and extract the required information for each product
3. The extracted data will be saved in result.csv
4. You can add more URLs to the urls.txt file and the program will extract and saves those in result.csv while not deleting the previous ones


## **Code Explanation**
### **Main Function**
The main function takes a URL as an argument, makes an HTTP request to the URL, and parses the HTML content using BeautifulSoup. It then extracts the product title, price, rating, number of reviews, and availability. The extracted information is printed to the console and saved into a CSV file

### **CSV File Handling**
A CSV file named result.csv is opened in append mode. The extracted data is written to this file, ensuring that new data is added without overwriting the existing data.

### **HTTP Request and Beautiful Soup**
The script uses the requests library to make an HTTP requests to the Amazon product URL. The response content is then parsed using BeautifulSoup with the lxml parser


### **Data Extraction**
The script extracts the product title, price, rating, number of reviews, and availability using BeautifulSoup's find method with appropriate HTML element attributes. If an attribute is not found, a default value of N/A is used

### **Reading URLs**
The urls.txt file is read line by line, and each URL is passed to the main function for processing


## **Example urls.txt File**
```
https://www.amazon.com/Genuine-Porsche-Black-Crest-Logo/dp/B003UNPAVS
https://www.amazon.com/fire-tv-stick-with-3rd-gen-alexa-voice-remote/dp/B08C1W5N87
https://www.amazon.com/PlayStation®5-console-slim-PlayStation-5/dp/B0CL61F39H
```

## **Example Output**
```Excel
Porsche Men's Genuine Cap with Crest	$55.99 	4.7 out of 5 stars	604 ratings	In Stock
Amazon Fire TV Stick	$21.99 with 45 percent savings	4.6 out of 5 stars	480671 ratings	In Stock
PlayStation¬Æ5 console (slim)	$494.65 	4.5 out of 5 stars	786 ratings	In Stock
```


