import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Cleaning and File reading.
# To integrate the five files, we began by evaluating each in Excel to better understand the data structure and content. Upon analysis, we discovered that all files shared identical columns, with a few exceptions: some files added irrelevant columns such as Lower Whisker, Upper Whisker, and Lower Interval. To streamline the dataset, we removed the superfluous columns directly from Excel.

# Additionally, we discovered anomalies in column names across the files. For example, Happiness Score was sometimes written as Happiness.score. To solve this, we cleaned up the data and standardized the column names in Excel to increase readability and consistency.

# As the data set is given separately for 5 different years,
# we will load each dataset and concatenate them as they have same columns but for different years


# Load Datasets path.
file_path = {'2015':'2015.csv',
            '2016':'2016.csv',
            '2017':'2017.csv',
            '2018':'2018.csv',
            '2019':'2019.csv'}

#Function for loading each dataset.
def load_data(file_path):
    data_frames=[]
    for year,path in file_path.items():
        df = pd.read_csv(path)
        df['Year'] = int(year)
        data_frames.append(df)
    return pd.concat(data_frames, axis = 0)

#Combining all data
happiness_df = load_data(file_path)

#Displaying the combined data.
happiness_df=happiness_df.reset_index()
happiness_df=happiness_df.drop(columns = 'index')
happiness_df

#checking for null values
null_values = happiness_df.isnull().sum()
null_values

happiness_df.dtypes

happiness_df.columns

#fill the null values
happiness_df=happiness_df.fillna(0)

#Summarize statistics
stats =happiness_df.describe().drop(columns='Year')
stats

#Summarize statistics
stats =happiness_df.describe().drop(columns='Year')
stats

#Happiness score per year of each country.
Happiness_score=happiness_df.groupby(['Year','Country'])['Happiness Score'].sum()

# Distribution of Happiness score over the five years.

plt.figure(figsize=(10, 6))
sns.histplot(happiness_df['Happiness Score'], kde=True, color='skyblue')
plt.title('Distribution of Happiness Scores')
plt.xlabel('Happiness Score')
plt.show()

# Average Happiness Score by Year

Avg_Happiness_score=happiness_df.groupby('Year')['Happiness Score'].mean()
print(Avg_Happiness_score)

plt.figure(figsize=(10, 6))
sns.barplot(data=happiness_df, x="Year", y="Happiness Score")
plt.title('Average Happiness Score Over Years')
plt.show()

sns.scatterplot(x=happiness_df['Happiness Score'],y=happiness_df['Economy (GDP per Capita)'], hue="Year",data= happiness_df )
plt.show()

sns.scatterplot(x=happiness_df['Happiness Score'],y=happiness_df['Health (Life Expectancy)'], hue="Year", data= happiness_df )
plt.show()

sns.scatterplot(x=happiness_df['Happiness Score'],y=happiness_df['Social support'], hue="Year",data= happiness_df )
plt.show()

happiness_df.corr(numeric_only = True)

selected_columns = ['Happiness Score', 'Economy (GDP per Capita)', 'Social support', 'Health (Life Expectancy)']
plt.figure(figsize=(10, 8))
correlation_matrix = happiness_df[selected_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

#### Relationship happiness scores and features like GDP, social support, and life expectancy.
### As per the correlation score and the scatterplots for each we can say they have a strong positive relation, showcasing an increase with increase in the other.

#Top 10 Happy Countries overall in 5 years
Happiness_score_10=happiness_df.groupby(['Year','Country'])['Happiness Score'].sum().sort_values(ascending =False).head(10)
Happiness_score_10.plot(kind='bar',edgecolor = 'black')
plt.show()
print(Happiness_score_10)

# Top 10 happiest countries for each year

top_10_countries = (happiness_df.groupby("Year").apply(lambda x: x.nlargest(10, 'Happiness Score')))
#The nlargest(10, 'Happiness Score') method selects the top 10 rows from x based on the column 'Happiness Score'.

print("Top 10 Happiest Countries Each Year:",'\n')
print(top_10_countries[['Country', 'Happiness Score']])

top_10_countries.set_index('Country')['Happiness Score'].plot(kind='bar',edgecolor = 'black', figsize= (12,8))
plt.show()

# Calculate the mean contribution of factors for each year
years = [2019, 2018, 2017, 2016, 2015]
factor_contributions = {}

for year in years:
    factor_contributions[year] = happiness_df[happiness_df['Year'] == year][[
        'Economy (GDP per Capita)', 'Social support', 'Health (Life Expectancy)',
        'Freedom', 'Trust (Government Corruption)', 'Generosity'
    ]].mean()

# Create subplots for all years
plt.figure(figsize=(20, 5))  # Adjust figure size for better visibility

for i, year in enumerate(years, 1):
    plt.subplot(1, 5, i)
    factor_contributions[year].plot(kind='bar', color='teal')
    plt.title(f'Factors Contribution to Happiness ({year})')
    plt.ylabel('Mean Value')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

## 1. Insights for NGOs
### NGOs focus on factors related to social well-being, such as Social Support, Generosity, and Healthy Life Expectancy. The goal is to identify countries with low scores in these areas and provide recommendations.

# Average social support, generosity, and healthy life expectancy by country
ngo_factors = happiness_df.groupby('Country')[['Social support', 'Generosity', 'Health (Life Expectancy)']].mean()

# Sort countries by the lowest average scores for social support and healthy life expectancy
low_social_support = ngo_factors.sort_values('Social support').head(10)
low_life_expectancy = ngo_factors.sort_values('Health (Life Expectancy)').head(10)

print("Top 10 Countries with Lowest Social Support:")
print(low_social_support)

print("\nTop 10 Countries with Lowest Healthy Life Expectancy:")
print(low_life_expectancy)

# Visualization: Low social support countries
low_social_support.plot(kind='barh', y='Social support', legend=False, color='orange', figsize=(8, 5))
plt.title('Countries with Lowest Social Support')
plt.xlabel('Social Support Score')
plt.ylabel('Country')
plt.show()

# Visualization: Low healthy life expectancy countries
low_life_expectancy.plot(kind='barh', y='Health (Life Expectancy)', legend=False, color='teal', figsize=(8, 5))
plt.title('Countries with Lowest Healthy Life Expectancy')
plt.xlabel('Healthy Life Expectancy')
plt.ylabel('Country')
plt.show()

# Countries with high Social support but low happiness
high_social_low_happiness = happiness_df[(happiness_df['Social support'] > 1) & (happiness_df['Happiness Score'] < 5)]
print("Countries with High Social Support but Low Happiness:")
print(high_gdp_low_happiness[['Country', 'Social support', 'Happiness Score']])


## 2. Insights for Governments
### Governments are typically more interested in broader economic and societal factors like GDP per Capita, Happiness Score, and the correlation between these factors. The focus is to identify key drivers of happiness for policy planning.

# Correlation between key factors and happiness score
gov_factors = happiness_df[['Happiness Score', 'Economy (GDP per Capita)', 'Health (Life Expectancy)']].corr()

print("Correlation Between Key Factors and Happiness Score:")
print(gov_factors['Happiness Score'])

# Visualization: Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(gov_factors, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Key Factors')
plt.show()

# Countries with high GDP but low happiness (potential policy gaps)
high_gdp_low_happiness = happiness_df[(happiness_df['Economy (GDP per Capita)'] > 1) & (happiness_df['Happiness Score'] < 5)]
print("Countries with High GDP but Low Happiness:")
print(high_gdp_low_happiness[['Country', 'Economy (GDP per Capita)', 'Happiness Score']])

# Visualization: High GDP vs Low Happiness
plt.figure(figsize=(8, 5))
sns.scatterplot(data=happiness_df, x='Economy (GDP per Capita)', y='Happiness Score', hue='Year', palette='viridis')
plt.title('GDP per Capita vs Happiness Score')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.axhline(5, color='red', linestyle='--', label='Low Happiness Threshold')
plt.legend()
plt.show()

# Getting the cleaned and combined data set for streamlit app.
happiness_df.to_csv('World_happiness_report.csv', index=False)


