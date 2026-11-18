This project investigates whether a cross-sectional momentum strategy can generate risk-adjusted excess returns relative to a passive S&P 500 investment. The strategy ranks a universe of exchange-traded funds based on historical performance, selects the three highest-ranking assets and rebalances monthly. Its perfomance will be evaluated using historical backtesting, transaction costs and out-of-sample validation.

We hypothesize that momentum strategy outperforms the vanilla S&P 500 Investment by reacting to value changes, constantly optimising for the best case scenario for the investment.

To investigate our question further, we consider the adjusted prices of 10 exchange-traded funds from Yahoo finance, with a wide range of sectors that they come from. These include SPY (State Street SPDR S&P 500 ETF Trust), QQQ (Invesco QQQ Trust, Series 1), IWM (iShares Russell 2000 ETF), EFA (iShares MSCI EAFE ETF), EEM (iShares MSCI Emerging Markets ETF), TLT (iShares 20+ Year Treasury Bond ETF), IEF (iShares 7-10 Year Treasury Bond ETF), GLD (SPDR Gold Trust), DBC (Invesco DB Commodity Index Tracking Fund) and VNQ (Vanguard Real Estate ETF).

The technology used for this analysis includes a stack of Python, standard data analysis libraries in Python such as numpy and pandas, as well as Yfinance for the data sourcing. More details on the exact specifications can be found in the requirements.txt file.

Currently, the development is at early phase, having concluded data collection and pre-processing, as well as exploratory analysis.