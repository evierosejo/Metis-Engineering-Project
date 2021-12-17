import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import streamlit as st
from datetime import datetime

st.write(
'''
## Supreme Court: Entitled to its Opinions
The U.S. Supreme Court was created with the intention of impartiality, a 
branch of government that tamped down politics and human biases and dedicated itself to 
interpretating the Constitution. However, is the Supreme Court truly nonpartisan?
In a time when the decision of Roe v. Wade may be overturned, this question rings even louder. 

## Party Politics

The graph below shows how many judge appointments were made under presidents since this country's founding.
''')

justices = pd.read_csv('/Users/evelynjohnson/Desktop/METIS/Engineering/project/justices.csv')

appointing_presidents = ['Donald Trump', 'Barack Obama', 'William Clinton',
       'George Bush', 'Ronald Reagan', 'Gerald Ford',
       'Franklin Roosevelt', 'Herbert Hoover', 'Calvin Coolidge',
       'Woodrow Wilson', 'Theodore Roosevelt',
       'William McKinley', 'Grover Cleveland', 'Benjamin Harrison',
       'Abraham Lincoln', 'James Buchanan', 'Franklin Pierce',
       'Millard Fillmore', 'John Tyler', 'Andrew Jackson',
       'Thomas Jefferson', 'James Monroe', 'James Madison',
       'George Washington']

pres_appointments = pd.DataFrame(columns=['President', 'Judge Appointments'])
idx = 0
for pres in appointing_presidents:
    rows = justices.loc[justices['Appointing President'] == pres]
    count = rows['Appointing President'].count()
    pres_appointments.loc[idx] = [pres, count]
    idx += 1

fig = px.bar(pres_appointments, 
             x = 'Judge Appointments',
             y='President',
             orientation='h',
            title='Distribution of Number of Presidential Judge Appointments'
            )

st.plotly_chart(fig, use_container_width=True)

opinions = pd.read_csv('/Users/evelynjohnson/Desktop/METIS/Engineering/project/opinions.csv')
def get_years(df):
    years = sorted(opinions.year_delivered.unique().tolist())

    cases_per_year = pd.DataFrame(columns=['Year', 'Number of Cases'])
    idx=0
    for year in years:
        count = opinions.Case.where(opinions.year_delivered == year).count()
        cases_per_year.loc[idx] = [year, count]
        idx += 1
    
    return cases_per_year

amount_of_cases = get_years(opinions)

st.write(
'''
## Opinions
The graph below shows the number of opinions delivered per year. Interestingly, the amount of opinions delivered per year 
has significantly decreased since 1968. 
''')

line_chart = px.line(amount_of_cases, x="Year", y="Number of Cases", title='Opinions Delivered Over Time')
st.plotly_chart(line_chart, use_container_width=True)

currentYear = datetime.now().year
input_year= st.number_input(label='Enter a year between 1968 and {}'.format(currentYear), min_value=1968, max_value=currentYear)
st.write('The subjects that most commonly showed up in', input_year, 'in U.S. Supreme Court Opinions are:')





