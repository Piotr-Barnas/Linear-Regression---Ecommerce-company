Project done during realising "Python for Data Science and Machine Learning Bootcamp" course on udemy.com

1. Description of data

I took csv file attached to this course, which contained Ecommerce company data such as:

* customer info
  - email
  - address
  - color avatar

* numerical value columns
  - Avg. Session Length: average session of in-store style and clothing advice sessions)
  - Time on App: average time spent on App in minutes
  - Time on Website: average time spent on Website in minutes
  - Length of Membership: how many years the customer has been member

2. Description of problem

Depending on following data decide whether company should focuse on develop their app or their website (what gives higher benefit)

3. Description of solution

For analizes I used such libreries of python 3.6 as Pandas, NumPy, Seaborn and sklearn module.

At the very beginning I've checked basic infos, its size, min, max, type, quartiles etc. Then I've made two jointplots: first - compering Time on Website and Yearly Amount Spent,
second - compering Time on App and also Yearly Amount Spent. Observation (only depending on the plots): second chart was better correlated.

Next step - pairplot (scatter plots of every column with each column, histograms on diagonal). Observation:Lenth of Membership and Yearly Amount Spent is the most coreelated pair

After that I've split data for a variable x equal to the numerical features of the customers and a variable y equal to the "Yearly Amount Spent" column and then split them both
into training and testing sets, with ratio 70 to 30. I've called linear regression model method, fitted traning data and predict values for testing x set. When I've already had this
values I've calculated errors: MAE, MSE, RMSE, made histogram of residuals of real y testing set and predicted y values with its density plot on it and also made scatter plot of 
predicted values and real y testing set. So I've checked model's correctness and it passed the test.

Last step was making data frame presenting coeffecient of each column. That gave me clear way to compare what brings bigger profit, because it showed me that:

* A 1 minute increase in "Time on App" (all others features fixed) is associated with an increase of 38.59$ in "Yearly Amount Spent"

* A 1 minute increase in "Time on Website" (all others features fixed) is associated with an increase of 0.19$ in "Yearly Amount Spent"

4. Conclusion

Version a)
Ecommerce company should put their efforts on improving their app, because it gains a lot of more returns than website, so it's justified to tweak it.

Version b)
Ecommerce company should put their efforts on improving their website, as it almost doesn't give returns, so that in future it what catch up with app.

{It's too less informations to judge which version is proper}
