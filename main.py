import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load Data
data = pd.read_csv('World_happiness_report.csv')

# Title
st.title("🌍 Global Insights Dashboard")
st.subheader("🚀 Explore Happiness and Economic Trends Across Countries")

# Sidebar Filters
st.sidebar.title("Filters")

# Dropdown for Year
year = st.sidebar.selectbox("📅 Select Year", sorted(data['Year'].unique()))
filtered_data = data[data['Year'] == year]

# Dropdown for Countries with "Select All" functionality
def country_selector(label, options):
    """
    A dropdown-like multiselect with a 'Select All' option in the sidebar.
    
    Args:
        label (str): The label for the dropdown.
        options (list): The list of options to display.
    
    Returns:
        list: The selected options.
    """
    select_all = st.sidebar.checkbox(f"Select All {label}", value=True)
    if select_all:
        return options
    else:
        return st.sidebar.multiselect(label, options, default=options)

# Filter by Countries
countries = sorted(filtered_data['Country'].unique())
selected_countries = country_selector("Countries", countries)

# Filter data by selected countries
filtered_data = filtered_data[filtered_data['Country'].isin(selected_countries)]

# Display filtered data
st.write(filtered_data)

# KPIs
st.subheader("📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

# Calculate metrics
avg_happiness = filtered_data['Happiness Score'].mean()
highest_gdp_country = filtered_data.loc[filtered_data['Economy (GDP per Capita)'].idxmax(), 'Country']
highest_gdp = filtered_data['Economy (GDP per Capita)'].max()
avg_life_expectancy = filtered_data['Health (Life Expectancy)'].mean()
num_countries = filtered_data['Country'].nunique()

# Display KPIs
with col1:
    st.metric(label="🌟 Avg Happiness Score", value=f"{avg_happiness:.2f}")

with col2:
    st.metric(label="💰 Highest GDP (Country)", value=f"{highest_gdp_country} ")

with col3:
    st.metric(label="🌍 Avg Life Expectancy", value=f"{avg_life_expectancy:.2f}")

with col4:
    st.metric(label="📈 Number of Countries", value=num_countries)

# Section 1: Top 10 Happiest Countries
st.subheader("🥇 Top 10 Happiest Countries")
top10 = filtered_data.nlargest(10, 'Happiness Score')

# Improved Visualization: Horizontal Bar Chart (Plotly)
fig_top10 = px.bar(
    top10,
    x='Happiness Score',
    y='Country',
    orientation='h',
    color='Happiness Score',
    title=f"Top 10 Happiest Countries in {year}",
    color_continuous_scale='Blues'
)
st.plotly_chart(fig_top10, use_container_width=True)

# Section 2: Correlation Heatmap
st.subheader("🔗 Correlation Heatmap")
st.write("Understand how key factors relate to happiness.")

selected_cols = ['Happiness Score', 'Economy (GDP per Capita)', 'Social support', 'Health (Life Expectancy)']
corr = filtered_data[selected_cols].corr()

# Visualization 2: Heatmap (Seaborn)
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax, cbar_kws={'shrink': 0.8})
st.pyplot(fig)

# Section 3: GDP vs Happiness Score
st.subheader("💰 GDP per Capita vs Happiness Score")
st.write("Explore the relationship between economic strength and well-being.")


# Visualization 3: GDP vs Happiness Score
st.subheader("GDP per Capita vs Happiness Score")
st.scatter_chart(data=filtered_data, x='Economy (GDP per Capita)', y='Happiness Score', color='Year')


# Section 4: Insights for NGOs and Governments
st.subheader("🎯 Insights & Recommendations")
st.write("""
- **Governments**:  
   Invest in health systems, especially in regions with low life expectancy but high GDP.  
   Address inequalities to uplift overall well-being.  

- **NGOs**:  
   Focus on regions with lower happiness scores despite high social support.  
   Target healthcare and Social support for maximum impact.  
""")

# Footer: 
st.markdown("---")
st.markdown("📝 **Developed by Ismail Pasha & Devesh Ghai** | Data from: [World Happiness Report]")
