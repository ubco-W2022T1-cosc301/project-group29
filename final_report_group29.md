# COSC 301 Project Group 29

## Introduction


---

## Exploratory Data Analysis



---

## Question 1 + Results

Concerned for weather changes, I picked a data set which records weather statistics from Estes Park, Colorado over ten years. I will attempt to spot the existence and regularity of worrying climate changes on dew point by investigating possible drastic changes of dewpoint and dewpoint depressions over ten years and try to explain why they are happening.

![](./images/a1_t4_lmplot.png)

### Fig 1

This plot describes the Pair Wise Relationship between Dewpoint Depression and Average Humidity each Month at Estes Park, Colorado from 2010 to 2020. Columns are for average humidity in %, and rows are for dewpoint depression in F.

All the plots have approximately the same linear approximation expcept for are a few expecial cases. Month 3 from 2011, Month 4 from 2011, Month 9 from 2011, and Month 2 from 2012 simply does not have sufficient (less than 5) data collected to support meaningful analysis. In all other month, averge dewpoint depression range from around 0 F to 40 F, and average humidity ranges from around 20% to 80%. 

All the distributions evenly spread along a staight line, suggesting the two variables have a netaive linear correlation. They have approximately the same x intercept and y intercept, suggesting average humidity and dewpoint depressions remains the roughly the same behavior over different year.

Hence, when humidity is low, the dewpoint depression gets high, then more cooling is needed to reach saturation, and the air becomes drier. In a park, it may mean its trees are easier to catch fire. 

![](./images/a1_t4_joint.png)

### Fig 2

This plot focus on the display bivariate and univariate relationships of Average Dewpoints (F) (column) and Range of Dewpoints (F) (row) at Estes Park, Colorado from 2010 to 2020.

Averge Dewpoint is very close to normal distributino with center at around 20 F and one standard deviation around 15 F. Range of Dewpoint is also very close to normal distribution with center at around 80 F and one standard deviation around 10 F.

There are two clusters in the graph. One is where average dewpoint is around 10 to 20 F, dewpoint range is around 50 to 80F, the other is one is where verage dewpoint is around 30 to 40 F and dewpoint range is around 80 to 100. From the observation of average dewpoint changes over month, we can see that the bottom left cluster happens during winter, and the top right corner happens during summer.

Generally, higher average dewpoint correspond to higher range of dewpoint, and higher range of dewpoints show up in summer more than it does in winter. This is signifcant because a high range of of dewpoint may correspond to a sharp change of dewpoint. As Fig 1 we conclude that humidity ranges doesn't change much over the year, it correspond to a possiblity of sharp change in dewpoint yet a small change in temperature, in which case the place become what is called a dewpoint front which tightly connects to severe cimate.

![](./images/a1_t4_ridge.png)

### Fig 3

The last plot describes Dewpoint Depressions Variations by Year at Estes Park, Colorado. 

The plot provides ridgeline plot on dewpoint depression, rows for years (2010-2019 top to bottom), columns for dewpoint depression (-20 to 80 F left to right). Ridgeline hue for Month (January Lightest, December Darkest).

Here are the things noticable:

2010's summer has a very high dewpoint depression cluster at around 40, which correspond to a relative low of humidity in June the entire month. May 2012 and March 2018 has peaked at around 70. It is interesting though, highest dewpoint depression in other years shows up in December.

Looking over the dewpoint depression range, 2016 shows up to be the year with the lowest range of dewpoint depression, about 0 to 60 F. Its range is approximately 20 F less that others. Also in this year, distributions of dewpoint depressions of different month are overlapping each other. A low range change, and similar distribution of dewpoint depression throughout, suggests that 2016 is a year with least driness fluction year. It should be more pleasant than other years at the park.

### Results

At Estes Park, Colorado, dewpoint depression has a negative correlation with average humidity. During any time of the year, days with lower average humidity, air need to release more heat to reach saturation and are therefore catch fire more easily.

Average Dewpoint and range of dewpoint clusters at summer and winter at two differnt points, generally, they have a positive correlation. As average dewpoints at summer are generally higher, so is range of dewpoints. Hence, in summers at the Park, it is more like to experience drastic change in dewpoint to become dewpoint front, where severe weather could happen.

With most moderate dewpoint depression range and change, 2016 is, after analysis, the most pleasant year at the Park from 2010 to 2020.

## Question 2 + Results



## Question 3 + Results



---

## Conclusion