#Example_of_modelling_an_asset_via_yfinance
from matplotlib import pyplot
import yfinance as yf

ticker = "NVDA"
data = yf.download(ticker, period="5d")
data.reset_index(inplace=True)

pyplot.ylabel("Price")
pyplot.xlabel("Date")
pyplot.title("NVDA")

pyplot.plot(data["Date"], data["Adj Close"], c="orange", linewidth=2)
pyplot.show()