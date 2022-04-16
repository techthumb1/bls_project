
# Time Series Analysis with Exponential Smoothing
#### A powerful alternative approach to forecasting time series data

## Exponential Smoothing

Exponential smoothing has been around for some time and is still considered one of the more powerful methods due to its capability of covering a long range of time accurately and efficiently.

There are three types of exponential smoothing techniques that we have to choose from:
- Single (Simple) Exponential Smoothing (SES)
- Double Exponential Smoothing
- Triple Exponential Smoothing (Holt-Winters)

The dataset is one out of a project series that I am working on involving economical factors such as _consumer price index, consumer spending, employment, and employee wages_.

For this project, we will conduct a time series analysis on univariate values
Additive
Multiplicative

## Single Exponential Smoothing

SES is likely to be used when we are forecasting data that does not incorporate or rely on a trend. SES is primarily used for forecasting univariate time series data.

The SES model uses a weighted average of the current value and the previous value.The weight is determined by the smoothing parameter, $\alpha$. The higher the value of $\alpha$, the more weight is given to the current value.The lower the value of $\alpha$, the more weight is given to the previous value.

The two types of trends that can be incorporated into the SES model are additive and multiplicative.

- Additive: The additive trend is the sum of the previous values.
- Multiplicative: The multiplicative trend is the product of the previous values.

## Double Exponential Smoothing

Double Exponential Smoothing is a more advanced version of SES. It suports forecasting trends by using two weights, $\alpha$ and $\beta$, where $\beta$ is an additional smoothing factor that controls weight decay.



## Triple Exponential Smoothing (Holt-Winters)

