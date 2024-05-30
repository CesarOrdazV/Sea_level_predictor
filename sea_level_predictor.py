import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')

    # Create scatter plot
    plt.subplots(figsize=(16,9))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue')

    # Create first line of best fit
    slope1, intercept1, r1, p1, se1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = intercept1 + slope1 * x1
    plt.plot(x1, y1, c='green')

    # Create second line of best fit
    df_recent = df.copy()
    df_recent = df_recent[df_recent['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = intercept2 + slope2 * x2
    plt.plot(x2, y2, c='red')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()