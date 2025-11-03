import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, label='Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = list(range(1880, 2051))
    line_all_data = [slope * year + intercept for year in years_extended]
    
    plt.plot(years_extended, line_all_data, 'r-', label='Best Fit Line (All Data)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent_extended = list(range(2000, 2051))
    line_recent_data = [slope_recent * year + intercept_recent for year in years_recent_extended]
    
    plt.plot(years_recent_extended, line_recent_data, 'g-', label='Best Fit Line (Since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()