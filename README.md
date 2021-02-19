# Predicting the Success of Retail Establishments in New York
Final project for UCU Summer School 2018. Supervisor Dr. Anastasios Noulas.
Inspired by Urban Data Science course we have created the model to predict the Success of Retail Establishments.
Most of the features engineering was done based on paper. We used open data of Foursquare and New York Yellow taxi in order to extract:
* Geographical features: 
  * Density
  * Neighbors entropy
  * Competitiveness.
* Mobility Features:
  * Area popularity
  * Transition density
  * Incoming flow
  * Transition quality
  * Taxi transition density
  * Taxi incoming flow
                                                               
![Alt Text](https://media.giphy.com/media/B36TO88d3mc15nAEko/giphy.gif) ![Alt Text](https://media.giphy.com/media/7zGxu4GwfrnCYR6TGY/giphy.gif)
                                                     
As for modeling we used:
* XGBoost Regressor
* SGDRegressor
* DecisionTreeRegressor
* ElasticNet
* Lasso
* Ridge
                                  
Also, for better performance, we used hyperparameter tuning by Tree of Parzen Estimators (TPE) algorithm.
In fact, we were solving the ranking problem, based on regression predict, so we used NDCG metrics with real rank as for relevance measure. For our models we get:

The full presentation of the project you can find here: [link to the presentation](https://github.com/trokhymovych/geoconsulting/blob/master/project_25_ny.pdf)




