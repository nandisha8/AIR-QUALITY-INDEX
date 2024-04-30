import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv('data_date.csv')
# Define precaution suggestions based on AQI values
def suggest_precautions(aqi):
    if aqi < 50:
        return 'Air quality is good. No precautions needed.'
    elif aqi < 100:
        return 'Air quality is moderate. Sensitive groups should consider reducing prolonged outdoor exertion.'
    elif aqi < 150:
        return 'Air quality is unhealthy for sensitive groups. Children and people with lung disease should avoid strenuous outdoor activities.'
    elif aqi < 200:
        return 'Air quality is unhealthy. Everyone should avoid prolonged outdoor exertion; sensitive groups should stay indoors.'
    elif aqi < 300:
        return 'Air quality is very unhealthy. Everyone should avoid prolonged outdoor exertion; sensitive groups should avoid all outdoor exertion.'
    else:
        return 'Air quality is hazardous. Everyone should avoid any outdoor exertion; stay indoors and reduce activity levels.'

# Apply the function to get precaution suggestions for each row
data['precaution'] = data['aqi_value'].apply(suggest_precautions)

# Plot AQI values for each country
plt.figure(figsize=(15, 10))
for country in data['country'].unique():
    country_data = data[data['country'] == country]
    sns.lineplot(x='date', y='aqi_value', data=country_data, label=country)

plt.xlabel('Date')
plt.ylabel('AQI_Value')
plt.title('AQI Values Over Time for Different Countries')
plt.legend(title='Country')
plt.show()

# Print precautions for the last date in the dataset for each country
latest_data = data.sort_values(by='date', ascending=False).drop_duplicates(subset='country', keep='first')
for index, row in latest_data.iterrows():
    print(f"{row['country']} on {row['date']}: AQI {row['aqi_value']}. Precaution: {row['precaution']}")