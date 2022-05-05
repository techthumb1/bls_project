
# Time Series Analysis with Exponential Smoothing
A powerful alternative approach to forecasting time series data

## Exponential Smoothing

Exponential smoothing has been around for some time and is still considered one of the more powerful methods due to its capability of covering a long range of time accurately and efficiently.

There are three types of exponential smoothing techniques that we have to choose from:
- [Single (Simple) Exponential Smoothing (SES)](https://en.wikipedia.org/wiki/Exponential_smoothing#Single_exponential_smoothing)
- [Double Exponential Smoothing (DES)](https://en.wikipedia.org/wiki/Exponential_smoothing#Double_exponential_smoothing)
- [Triple Exponential Smoothing (TES)](https://en.wikipedia.org/wiki/Exponential_smoothing#Triple_exponential_smoothing)

## Single Exponential Smoothing

SES is likely to be used when we are forecasting data that does not incorporate or rely on a trend. SES is primarily used for forecasting univariate time series data.

The SES model uses a weighted average of the current value and the previous value.The weight is determined by the smoothing parameter, `alpha`. The higher the value of `alpha`, the more weight is given to the current value.The lower the value of `alpha` the more weight is given to the previous value.

## Double Exponential Smoothing

Double Exponential Smoothing is a more advanced version of SES. It suports forecasting trends by using two weights, `alpha` and `beta`, where `beta` is an additional smoothing factor that controls weight decay.

The two types of trends that can be incorporated into the DES model are _additive_ and _multiplicative_.

- **Additive Trends**: The additive trend is the sum of the previous values with a linear trend.
- **Multiplicative Trends**: The multiplicative trend is the product of the previous values with an exponential trend. 

In addition to the above methods, we could also provide a _Dampening_ factor that will reduce the influence of the trend, with _Phi_(p) as our coefficient.

- **Additive Dampening**: The additive trend is the sum of the previous values with a linear trend.
- **Multiplicative Dampening**: The multiplicative trend is the product of the previous values with an exponential trend.


## Triple Exponential Smoothing (Holt-Winters)

Triple Exponential Smoothing adds more support by incorporating a third weight, `gamma`, which is used to control the influence of the seasonal trend. So, like the other two methods, _additiive_ and _mulitplicative_ processes will apply here as well.

- **Addtitive Seasonality**: The additive trend is the sum of the previous values with a linear trend.
- **Multiplicative Seasonality**: The multiplicative trend is the product of the previous values with an exponential trend.


## Working with the Data

The dataset is one out of a project series that I am working on involving economical factors such as _consumer price index, consumer spending, employment, and employee wages_.
