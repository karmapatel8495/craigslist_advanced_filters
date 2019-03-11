# Craigslist - Enhancing User Experience

Report: https://www.dropbox.com/s/hdw17t56z51374m/Craigslist%20-%20Enhancing%20User%20Experience.docx?dl=0

```
#python #scrapy #sklearn #machineLearning #webScraping #beautiful #NLP
```

## Abstract

Craigslist is one of the bigger seller-buyer marketplaces in the world. It serves more than 20 billion page-views per month making it 11th most visited website in the country. It has more than 49.4 million unique monthly visitors across the States. With more than 80 million new classified advertisements each month, Craigslist is the leading classifieds service in any medium. But over years, users are becoming more and more skeptical in buying electronics products from Craigslist. 
<br>

## Proposal

The main reason fueling this skepticism is an exponential increase in the variety of electronics products available in the market. With the onset of so many options for smartphones and other electronics and the increase in used products sellers on websites like Amazon and eBay, Craigslist is no longer the only player in the market. Websites like Amazon and eBay have well designed in-depth filters and tagging system backed with really intelligent Machine Learning models running in the background. 
<br>
Compared to these websites, Craigslist needs some really good classifiers and prediction models to compete effectively. But firstly, where exactly is Craigslist lagging behind. Most of the advertisements in the smartphones category are misclassified and lacks useful product information. It is very difficult for users to properly figure out what is the exact model of smartphone in most of the advertisements. Because of the lack of smart tagging, they can’t search for any particular smartphone model they have in mind. This makes the search activity very tedious for them. To add to the annoyance, there will be advertisements by repair shops and accessories sellers even when the user is interested in buying a smartphone.
<br>
Because of all these issues on Craigslist, there is a high chance that the user will end up going to Amazon or eBay websites. This is where our product comes in. Our utility is designed to detect any kind of misclassified advertisements using predictive models and advanced Natural Language Processing. Employing some machine learning algorithms, our utility will be able to exactly figure out if the advertisement is actually that of a phone or of some accessory or phone repair shop.
<br>
Moving on from the automated aspects of e-Commerce, what is one thing which these online websites try to implement to make the buying experience realistic? User reviews and ratings! Whenever we think of buying something, the first validation which comes to our mind is to consult our friends, who have already used it and ask them about how a particular product is. That is exactly what the other half of our utility does. By applying some Natural Language Processing, we extract the product information and use it to find the link of the same product from Amazon. Then using some web scraping techniques, we extract the user reviews and product ratings to help our buyers make an informed decision on whether the product meets their requirements. In this way, we strive to increase the customer satisfaction rating for Craigslist. 

## Steps to run code:

Our code is divided into three parts:
 - Code to Scrap from Craigslist: Craigslist code is in folder craigslist_demo. Crawler can be run using scarpy crawl cellphone
 - Classification model: Model.py file contains code for classification.
 - Amazon_Product_Link and amazon_get: These are the python codes we used to get Amazon product link from given title.
