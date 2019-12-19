# predicting_data_trends
Using Time series analysis/ARIMA for total stock data

The analysis report (.docx) is specifically targeted at people with limited technical background, with technical terms reduced and more illustrative examples provided. The report targets the importance of Data Visualisation.

The Python code (.py file) reuses some parts of code from the Internet, sources of which are commented in the file.


What I learnt
1) Data wrangling (I just manually edited the file for some mistakes, but overall the data doesn't have any NULL value and stuffs). The uploaded data is the edited version.
2) Choosing model: most of the basic algorithms that I learnt cannot be applied to this dataset, but seeing that the data is time-dependant, I choose time series analysis (even though I haven't learnt that online or in class yet)
3) Coding in Python, especially working libraries, datetime parsing and stuffs (most of the libraries are not yet covered in class)
4) Use Google & StackOverFlow faster (:>), impossible without these bc I haven't done a time series analysis yet.
5) Writing a report, this is equivalent to communicating results to a business/non-technical person. Apparently Data Visualisation is the simplest to use and understand for them.

Personal suggestion for improvements:
1) Data wrangling needs further practice to automate the process (e.g. using boolean slicing, methods for data cleaning). Other data transformations on the dataset can be use like taking log, square root,... which may help to improve the model.
2) Considering any other possible models to implement
3) Understanding Python code faster
4) Using classifiers to evaluate results. I didn't use any of them in the code, e.g. AIC, RSE, RSS
5) Learn the Maths behind the algorithms: something-fuller Test, ARIMA, stationary models for time series and their properties -> ST3233
