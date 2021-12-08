# Metis-Engineering-Project

#### Question:
The U.S. Supreme Court was created with the intention of impartiality, a branch of government that tamped down politics and human biases and dedicated itself to  interpretating the Constitution. In this project, my goal is to develop a model that empirically investigates whether the Supreme Court's stance truly is nonpartisan. In a time when the decision of Roe v. Wade may be overturned, this question rings louder. With this project, I set out to determine whether the Supreme Court is still presiding with the intent of our founding fathers and make the results publicly accessible through deploying my NLP model to a web application. 

#### Data:
The Supreme Court opinions are scraped from [FindLaw.com](https://caselaw.findlaw.com/court/us-supreme-court) which will be stored in a SQL database with the two columns, the case's name, the date the opinion was delivered and the opinion in text format. The unit of analysis is a Supreme Court case. I will supplement this text data with data on Supreme Court justices from [Constitution Annotated](https://constitution.congress.gov/resources/supreme-court-justices/), specifically their term period, who they were appointed by, and whether they typically lean right, left or center. 

#### Tools:
All data collection, cleaning, modeling and cloud storage processes will be automated and run on a monthly basis, which is appropriate for the rate at which the Supreme Court delivers opinions. 

* BeautifulSoup for web-scraping 
* SQL for data storage
* NLTK, Gensim, skikit-learn for natural language processing and modeling
* Streamlit for model deployment

#### MVP Goal:
My MVP goal is to have the necessary data acquired and stored in a SQL database and to have built a deployable model ready for a web application. 
