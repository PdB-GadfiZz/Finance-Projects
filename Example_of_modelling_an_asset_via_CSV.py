#Example of modelling an asset via CSV
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\pdebo\OneDrive\Bureau\Example-CSV-data.csv")

plt.ylabel('Price')
plt.xlabel('Dates')
plt.title('Example Equity Analysis')

plt.plot(data['Dates'], data['Adj Close'], c='orange', linewidth=2) # Arguments for plotting
plt.xticks(ticks=range(0, len(data['Dates']), 50), rotation=45)
plt.show()