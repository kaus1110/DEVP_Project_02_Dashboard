#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns


# In[4]:


# Load the data

def load_data():
    data = pd.read_csv('honeyproduction.csv')
    return data

df = load_data()


# In[5]:


# Title for the dashboard
st.title('Honey Production Dashboard')


# In[6]:


# Summary Statistics
st.subheader('Summary Statistics')
total_prod_avg = df['totalprod'].mean()
yield_avg = df['yieldpercol'].mean()
price_avg = df['priceperlb'].mean()
st.write(f"Average Total Production: {total_prod_avg:,.0f} pounds")
st.write(f"Average Yield Per Colony: {yield_avg:.2f} pounds")
st.write(f"Average Price Per Pound: ${price_avg:.2f}")


# In[7]:


# Time Series Analysis
st.subheader('Time Series Analysis')
fig, ax = plt.subplots()
ax = sns.lineplot(x='year', y='totalprod', data=df, estimator='sum', ci=None)
ax.set_title('Total Honey Production Over Years')
st.pyplot(fig)


# In[8]:


fig, ax = plt.subplots()
ax = sns.lineplot(x='year', y='yieldpercol', data=df, estimator='mean', ci=None)
ax.set_title('Average Yield Per Colony Over Years')
st.pyplot(fig)


# In[9]:


fig, ax = plt.subplots()
ax = sns.lineplot(x='year', y='priceperlb', data=df, estimator='mean', ci=None)
ax.set_title('Average Price Per Pound Over Years')
st.pyplot(fig)


# In[10]:


# State-wise Analysis
st.subheader('State-wise Analysis')
fig, ax = plt.subplots()
ax = sns.barplot(x='state', y='totalprod', data=df, estimator=sum, ci=None)
ax.set_title('Total Honey Production by State')
plt.xticks(rotation=90)
st.pyplot(fig)


# In[11]:


# Comparative Analysis
st.subheader('Comparative Analysis')
comp_states = st.multiselect('Select States for Comparison', df['state'].unique())
df_comp = df[df['state'].isin(comp_states)]
fig, ax = plt.subplots()
ax = sns.lineplot(x='year', y='totalprod', hue='state', data=df_comp)
ax.set_title('Comparative Total Production Over Years')
st.pyplot(fig)


# In[12]:


# Interactive Filters
st.subheader('Interactive Filters')
selected_states = st.multiselect('Select States', df['state'].unique())
selected_years = st.multiselect('Select Years', sorted(df['year'].unique()))
df_filtered = df[df['state'].isin(selected_states) & df['year'].isin(selected_years)]
st.write(df_filtered)

REPORT


Objectives of the Honey Production Dashboard Report:- 

1-Data Visualization and Insight Generation: To provide a comprehensive visual representation of the honey production dataset, facilitating easier understanding and insight generation regarding trends, patterns, and anomalies within the data.

2-Interactive Data Exploration: To offer an interactive platform that enables stakeholders to explore various aspects of honey production data across different states and years, allowing for dynamic data filtering and customized analysis.

3-Trend Analysis Over Time: To analyze and visualize the trends in honey production, yield per colony, and price per pound over different years, aiding in understanding how these key metrics have evolved historically.

4-Comparative State Analysis: To enable a comparative view of honey production across different states, helping to identify regional differences, leading producers, and the impact of local factors on production.

5-Market Insight: To provide insights into the economic aspects of honey production, including production values and market prices, offering valuable information for market analysis and decision-making.

6-User-Friendly Interface for Non-Technical Users: To create an accessible and user-friendly interface that allows non-technical users, such as honey producers, business owners, and researchers, to easily navigate and extract meaningful information from the data.

7-Facilitate Data-Driven Decision Making: To assist stakeholders in the agriculture or honey production industry, as well as policymakers and researchers, in making informed, data-driven decisions based on the insights gathered from the dashboard.

8-Educational Purpose: To serve as an educational tool for individuals interested in learning about agricultural trends, specifically in the context of honey production, through interactive data exploration and visualization.

These objectives aim to make the honey production data more accessible, understandable, and useful for a variety of users, from industry stakeholders to researchers and educators.


1. Summary Statistics:- 

    Purpose: Offers a quick overview of the dataset by showing average values for key metrics.
    Insights:
        1-Average Total Production: Provides an insight into the typical production scale of honey in the dataset.
        2-Average Yield Per Colony: Indicates the average efficiency of honey production per colony.
        3-Average Price Per Pound: Offers an overview of the general market price for honey.
        4-Analyzing the average Total Production could reveal whether the dataset predominantly consists of large-scale                  commercial honey producers or smaller, local beekeepers. This distinction could have implications for understanding the          composition of the honey industry.
        5-Delving into the variability of the Average Price Per Pound might unveil trends or patterns, such as seasonal                   fluctuations or responses to external market forces, helping stakeholders anticipate and adapt to market dynamics.
        
Managerial Implication:- 
        1-For managers overseeing larger commercial honey production, this insight helps gauge the scale at which competitors or           collaborators operate. Smaller-scale producers may use this information to benchmark against industry averages.
        2-For beekeepers and honey producers, understanding this metric can guide efforts to improve production efficiency.               Managers can explore strategies to optimize colony health, resource utilization, and honey extraction processes to               increase yield.
        3-Managers can use this information to set competitive pricing strategies. It's crucial for making informed decisions on           pricing products in alignment with market trends. Monitoring changes in the average price per pound over time can help           anticipate market shifts and adjust pricing strategies accordingly.
        4- Managers should stay agile in response to market dynamics. Understanding price fluctuations helps in strategic                  planning, allowing for adjustments to production volumes, marketing efforts, or diversification of product offerings.
        

2. Time Series Analysis

    Purpose: Visualizes how key metrics have evolved over time.
    Insights:
      1-Total Honey Production Over Years: Shows trends in honey production, highlighting increases or decreases over the years.
      2-Average Yield Per Colony Over Years: Indicates changes in the efficiency of honey production.
      3-Average Price Per Pound Over Years: Tracks the fluctuation in honey prices, which can be indicative of market demands, inflation, or other economic factors.
      4-Long-term Trends: Examining the Total Honey Production Over Years might reveal cyclical patterns, indicating the                 influence of environmental factors, climate change, or agricultural practices on honey production. Such insights could           guide sustainable practices in the industry.
      5-Price Dynamics: Tracking the Average Price Per Pound Over Years could provide insights into economic factors affecting           the honey market. For example, spikes in prices might be linked to increased demand, while consistent decreases might           signal oversupply.
      
Managerial Implications:- 
      1-Managers can use this information to anticipate periods of high demand and plan production schedules accordingly.               Identifying cyclical patterns helps in resource allocation and strategic decision-making.
      2- managers can use this data to assess the impact of changes in beekeeping practices, technology adoption, or                      environmental conditions on efficiency. Continuous improvement initiatives can be implemented based on these insights.
      3-Managers can adjust pricing strategies in response to market trends. Insights into price dynamics can inform decisions           related to inventory management, promotional activities, and market positioning.
      4-Managers can make informed decisions on market positioning, production volumes, and product differentiation based on an         understanding of market dynamics. They can also identify opportunities or challenges arising from shifts in supply and           demand.

3. State-wise Analysis

    Purpose: Allows for a comparison of total honey production across different states.
    Insights:
      1-Identifies leading and lagging states in honey production.
      2-Can be used to spot regional trends or the impact of local policies and environmental conditions on honey production.
      3-Regional Disparities: Beyond identifying leading and lagging states, a more detailed examination could reveal regional           disparities in honey production efficiency. This could be linked to climate variations, land use practices, or local             regulatory environments.
      4-Understanding the impact of local policies on honey production in different states could inform policymakers on the             effectiveness of existing regulations and guide the formulation of new policies to support the industry.
      
Managerial Implications:- 
      1-Managers can focus on optimizing production processes and adopting best practices from leading states. Lagging states           may benefit from targeted support, training programs, or interventions to improve production efficiency.

      2-Managers can adapt strategies based on regional factors. For example, understanding the impact of climate variations can         inform decisions related to beekeeping practices, while insights into local policies can guide compliance efforts
      3-Managers can implement targeted initiatives to address specific challenges in regions with lower production efficiency.         This may involve providing additional resources, training, or technology transfer to support beekeepers in overcoming           regional constraints
      4-Managers can use this information to evaluate the effectiveness of existing regulations and formulate new policies that         align with the needs and challenges faced by beekeepers in different states. Policies may be tailored to address                 specific regional dynamics

4. Comparative Analysis

    Purpose: Enables the user to select specific states for a detailed comparative analysis over time.
    Insights:
        1-Understand how selected states compare against each other in terms of honey production.
        2-Identify patterns or anomalies specific to certain states.
        3-Identifying Outliers: Looking at a detailed comparative analysis could help identify outliers among states. For                 instance, a state with consistently high honey production despite unfavorable conditions might offer valuable insights           into best practices that could be shared with other states.
        4-Comparing states over time may reveal cyclical patterns or synchronized trends that could be attributed to broader               regional factors affecting the honey industry.
        
Managerial Implications:- 
        1-Managers can tailor their focus to specific states of interest, allowing for more targeted insights. This flexibility           enables a deeper understanding of factors influencing honey production in selected regions
        2-Managers can identify states that consistently outperform or underperform compared to others. This insight can guide             the development of strategies to replicate successful practices or address challenges faced by specific states.
        3-Managers can investigate states with exceptional performance to uncover best practices. Sharing these practices with             other states can contribute to overall industry improvement. Similarly, addressing challenges faced by specific states           may involve targeted support and interventions
        4-Managers can explore the impact of regional factors such as climate, land use practices, or economic conditions on               honey production. Understanding these influences can inform regional-specific strategies and resource allocation

5. Interactive Filters

    Purpose: Provides a dynamic way to filter the data based on state and year selections.
    Insights:
        1-Offers customized views of the data based on user selection.
        2-Helps in conducting a focused analysis on specific years or states.
        3-User-Specific Insights: As users interact with the filters, they may discover nuances specific to their interests. For          example, selecting a specific state and year might uncover localized events or conditions influencing honey production.
        4-Predictive Analytics: The interactive filters could also be used for predictive analytics, allowing users to project             future trends based on historical data and filter scenarios to understand potential outcomes under different                     conditions.
        
Managerial Implications:- 
        1-Managers can explore specific subsets of the data that align with their research questions or areas of interest. This           flexibility enhances the ability to focus on relevant details and draw targeted insights
        2-Managers can zoom in on critical periods or regions, allowing for in-depth analysis and decision-making. This focused           approach is particularly valuable when investigating trends, challenges, or opportunities within specific contexts.
        3-Managers and stakeholders can tailor their exploration based on individual priorities. This user-centric approach               facilitates the discovery of localized events, market dynamics, or environmental conditions influencing honey                   production.
        4-Managers can use this feature for scenario planning, simulating the potential impact of different variables on future           honey production. This can aid in strategic decision-making and risk managementReferences/ Source:- 1-Kaggle 
                     2-ChatGPT
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




