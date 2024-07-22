# Amazon-Web-Scraper

## **Summary**

The Amazon Web Scraper is a python tool that extracts information from Amazon product pages, this includes product name, price, rating, number of reviews, and availability. The extracted data is then saved into a CSV file for further analysis or record-keeping




### **Features**
- Extracts product name, price, rating, number of reviews, and availability from Amazon product pages
- Saves the extracted data into a CSV file
- Utilizes BeautifulSoup for HTML parsing and requests for HTTP requests
- Emplos user-agent headers to avoid being blocked by Amazon servers

  
### **Requirements**
- Python 3.x
- BeautifulSoup4
- requests
- lxml

### **Installation**
1. Clone the repository:
   ```
   git clone https://github.com/Kunal-Kokate/Amazon-Web-Scraper.git
   cd Amazon-Web-Scraper
   ```
2. Install the required libraries:
   ```
   pip install beautifulsoup4 requests lxml
   ```
3. Create a urls.txt file in the project directory and add the Amazon product URLs you want to scrape, one per line.

   
### **Usage**
1. RUn the script:
   ```
   python AmazonWebScraper.py
   ```
2. The script will read the URLs from the urls.txt file and extract the required information for each product
3. The extracted data will be saved in result.csv
4. You can add more URLs to the urls.txt file and the program will extract and saves those in result.csv while not deleting the previous ones

