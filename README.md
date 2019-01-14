# predicting_data_trends
Using Time series analysis/ARIMA for total stock data

The analysis report (.docx) is specifically targeted at people with limited technical background, with technical terms reduced and more illustrative examples provided. The report targets the importance of Data Visualisation.

The Python code (.py file) reuses some parts of code from the Internet, sources of whom are commented in the file.


What I learnt
1) Data wrangling (I just manually edited the file for some mistakes, but overall the data doesn't have any NULL value and stuffs). The uploaded data is the edited version.
2) Choosing model: most of the basic algorithms that I learnt cannot be applied to this dataset, but seeing that the data is time-dependant, I choose time series analysis (even though I haven't learnt that online or in class yet)
3) Coding in Python, especially working libraries, datetime parsing and stuffs (most of the libraries are not yet covered in class)
4) Use Google & StackOverFlow faster (:>), impossible without these bc I haven't done a time series analysis yet.
5) Writing a report, this is equivalent to communicating results to a business/non-technical person. Apparently Data Visualisation is the simplest to use and understand for them.

Personal suggestion for improvements:
1) Data wrangling not practiced enough, need to automate the process (e.g. using boolean slicing, learning methods for data cleaning). There are some ways to modify the dataset such as taking log, square root,... but I haven't learnt why and when we can use that.
2) Any other models to employ? In reality, you may have to fit a model, and then use that fitted data to train again. It's not easy as just applying an existing model.
3) Understanding Python code faster
4) Using classifiers to evaluate results. I didn't use any of them in the code, mostly because I haven't learnt the Maths behind the algorithms yet, e.g. AIC, RSE (I know RSS but not this). I am not really confident in my results because of that!
5) Learn the Maths behind the algorithms: something-fuller Test, ARIMA, stationary models for time series and their properties (NUS's ST3233 is a good option)
