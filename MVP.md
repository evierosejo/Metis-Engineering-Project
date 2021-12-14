## Supreme Court: It is my right to have an opinion!

The goal of this project is to deploy a web application that will enable users to better understand the politics of the Supreme Court. I have webscraped three sets of data in order to do this. I have acquired data on the justices from Constitution Annotated, the party of affiliation of the presidents who appointed those judges from The Guardian, and Supreme Court opinion text data from FindLaw, which I previously collected in a pandas DataFrame. 
  
After acquiring the data, I cleaned the data by converting all dates to datetime data types and changed the names so they are the same across all tables, e.g.: 
  * 'Adams, John Quincy' to 'John Quincy Adams'
  * 'Kennedy, John F.' to 'John F. Kennedy'
    
The DataFrames were then put into a SQL database. Next, I plan to build a interactive Streamlit web application and to automate the data collection process to occur every month.
