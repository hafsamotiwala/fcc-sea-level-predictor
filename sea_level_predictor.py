import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Import the data from epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Actual Data', s=10)

    # 3. First line of best fit (All data: 1880 to 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(1880, 2051)
    line_all = res_all.slope * years_all + res_all.intercept
    plt.plot(years_all, line_all, color='red', label='Fits all data (1880-2050)', linewidth=2)

    # 4. Second line of best fit (Recent data: 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    line_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, line_recent, color='green', label='Fits recent data (2000-2050)', linewidth=2)

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save image and return current plot axes object for freeCodeCamp validation
    plt.savefig('sea_level_plot.png')
    return plt.gca()
