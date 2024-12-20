# Global Happiness Dashboard
## Dashboard Link : https://world-happiness-report-analysis-for-the-years-2015-to-2019-cbf.streamlit.app

## Overview
This project is a data visualization and analytics dashboard that explores global happiness and economic trends. It utilizes the **World Happiness Report** dataset to derive insights for governments, NGOs, and researchers. The dashboard is built using **Streamlit**, offering interactive visualizations and intuitive filters for exploration.

---

## Features
### Streamlit Dashboard
1. **🌟 Key Performance Indicators (KPIs):**
   - Average Happiness Score
   - Country with the Highest GDP
   - Average Life Expectancy
   - Number of Countries in the Dataset

2. **🥇 Top 10 Happiest Countries:**
   - Interactive horizontal bar charts using Plotly.

3. **🔗 Correlation Heatmap:**
   - Explore relationships between factors like GDP, Social Support, and Life Expectancy.

4. **💰 GDP vs Happiness Score:**
   - Scatter plot showcasing the relationship between economic strength and well-being.

5. **🎯 Insights & Recommendations:**
   - Recommendations for governments and NGOs based on trends and correlations.

### Data Cleaning & Preparation
- Standardized column names for consistency.
- Removed irrelevant columns such as "Lower Whisker," "Upper Whisker," and "Lower Interval."
- Combined datasets from 2015 to 2019 into a unified DataFrame.
- Filled null values with default values for seamless analysis.
- Exported cleaned dataset as `World_happiness_report.csv`.

---

## Data Cleaning
The project involves the integration of five datasets (2015-2019). Key steps:
- Standardized column names for consistency.
- Dropped irrelevant columns.
- Merged datasets into one comprehensive file with an additional `Year` column.
- Identified and filled null values.
- Conducted exploratory data analysis (EDA) to ensure data quality.

Key visualizations during data cleaning:
- Distribution of Happiness Scores.
- Average Happiness Score by Year.
- Correlation between Happiness and factors like GDP, Life Expectancy, and Social Support.

---

## Visualizations
### Key Insights:
1. **Distribution Analysis:**
   - Histogram to analyze the spread of happiness scores.

2. **Trend Analysis:**
   - Bar plots showing the average happiness score by year.

3. **Correlation Analysis:**
   - Heatmaps to reveal relationships between factors.

4. **Country-Specific Insights:**
   - Top 10 happiest countries each year.
   - Countries with low life expectancy or social support.

5. **Recommendations:**
   - Identified high-GDP, low-happiness countries to address policy gaps.

---

## Technologies Used
- **Python**: Data manipulation and analysis.
- **Pandas**: Data cleaning and aggregation.
- **Seaborn & Matplotlib**: Data visualization during EDA.
- **Plotly**: Interactive visualizations in Streamlit.
- **Streamlit**: Web-based dashboard application.


---

## Files
1. **`main.py`**:
   - Main Streamlit app.
2. **`cleaning.py`**:
   - Script for cleaning and preparing the dataset.
3. **`World_happiness_report.csv`**:
   - Cleaned dataset used in the app.
4. **`World Happiness Report Analysis (EDA).ipynb`**:
   - EDA and visualization of Cleaned dataset.
5. **`2015.csv,2016.csv,2017.csv,2018.csv,2019.csv`**:
   - The dataset has been initially cleaned and organized in Excel,
     and then used for further exploratory data analysis (EDA)

---

## Usage
### For Developers:
- Explore the dashboard locally by running `main.py`.
- Use the cleaned dataset for further analysis.

### For Users:
- Use the interactive dashboard to gain insights into happiness trends.
- Adjust filters to analyze specific years or countries.

---

## Insights
### Governments:
- Invest in health systems for regions with low life expectancy but high GDP.
- Address social inequalities to improve overall well-being.

### NGOs:
- Focus on countries with low scores in Social Support and Generosity.
- Target healthcare and social support improvements for maximum impact.

---

## Contributors
- **Ismail Pasha**  
- **Devesh Ghai**

---

## Acknowledgments
- **Data Source**: https://www.kaggle.com/datasets/unsdsn/world-happiness
- Libraries: Streamlit, Pandas, Plotly, Seaborn, Matplotlib

---

