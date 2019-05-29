# Predicting the Success of Retail Establishments in New York
Final project for UCU Summer School 2018. Supervisor Dr. Anastasios Noulas.
Inspired by Urban Data Science course we have created the model to predict the Success of Retail Establishments.
Most of the features engineering was done based on paper. We used open data of Foursquare and New York Yellow taxi in order to extract:
* Geographical features: 
  * Density
  * Neighbors entropy
  * Competitiveness.
  
![alt text](https://github.com/trokhymovych/Retail-establishment/blob/master/Screen%20Shot%202018-08-06%20at%2012.15.26%20AM.png?raw=true)
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
                          
![alt text](https://github.com/trokhymovych/Retail-establishment/blob/master/Screen%20Shot%202018-08-06%20at%2012.34.00%20AM.png?raw=true) 

XGBoost classifier performs the best. We assume that it is because it suffers less from highly correlated features than algorithms based on gradient descent. 

![alt text](https://github.com/trokhymovych/Retail-establishment/blob/master/Screen%20Shot%202018-08-06%20at%2012.34.08%20AM.png?raw=true) 

And here is example of predicting the best top10 spots for Subway Fast Food chain in NY:

![alt text](https://github.com/trokhymovych/Retail-establishment/blob/master/Screen%20Shot%202018-08-06%20at%2012.34.24%20AM.png?raw=true) 

The full presentation of the project you can find here: [link to the presentation](https://github.com/trokhymovych/Retail-establishment/blob/master/Project_25_NY.pdf)




