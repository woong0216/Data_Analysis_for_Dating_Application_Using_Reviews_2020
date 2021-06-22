# Data Analysis for Dating Application Using Reviews

## Background
- Social dating services have steadily grown in size since 1994 in the United States, with a variety of social dating apps emerging.
- As of 2016, 170 companies are growing in Korea, with an estimated market size of 200 to 50 billion and more than 3.3 million members.
- There are many studies that use consumer reviews as a way to analyze important factors.

## Propose
- We would like to identify the research flow of existing marketing with respect to online text as a factor affecting corporate performance.
- The review allows us to look at the overall response through the distribution of positive/negative, but we want to supplement the existence of limitations in identifying specific information.
- With the rapid growth of dating apps in recent years, there is still a lack of relevant review research and frequent changes in dating app sales rankings, but there is no clear reason for the relationship of variation
- We want to find out the difference between apps that have risen in the ranking and apps that have fallen in the domestic dating app spending rankings through factor analysis using review data.
- It is intended to enable benchmarking by analyzing whether consumers are positive or negative about certain functions of apps.

## Dataset
- Crawling Dating Application (Google Appstore Review Crawling.py)

![Dataset](https://user-images.githubusercontent.com/63955072/122874577-1e1ccf80-d36e-11eb-8e14-9d2d2493561b.PNG)

- Dating Application Rating

![Rating](https://user-images.githubusercontent.com/63955072/122874753-52908b80-d36e-11eb-9740-ce1036aaab17.PNG)

- Dating Application Trend Analysis

![Dating Application](https://user-images.githubusercontent.com/63955072/122874889-87044780-d36e-11eb-8931-c21f1a0513ee.PNG)

## Method
- Data Keywords Extraction
> Extracting through TF-IDF (TF-IDF.py) <br/> 

![TF-IDF](https://user-images.githubusercontent.com/63955072/122875364-20335e00-d36f-11eb-9b32-d156b39d045e.PNG)

- Extract Weighted value multiplied by TF-IDF value and STAR value (Weight value + TF-IDF.py)
> ex) Positive Review <br/>

![Positive 1](https://user-images.githubusercontent.com/63955072/122881729-6c35d100-d376-11eb-993a-729e079f9089.png)

> ex) Negative Review <br/>

![Negative 1](https://user-images.githubusercontent.com/63955072/122881767-78ba2980-d376-11eb-9d3f-05be9159e7ee.png)

- Co-occurrence Matrix
> Review * Word Matrix --> Word * Word Matrix (Co-occurrence.py) <br/>

![co-occurrence](https://user-images.githubusercontent.com/63955072/122882257-f716cb80-d376-11eb-931f-9b5f30444aa4.PNG)

## Analysis
- Draw Data Network 
> ex) '심쿵+위피' Positive before 2019 <br/>

![Positive before 2019](https://user-images.githubusercontent.com/63955072/122882706-6bea0580-d377-11eb-9773-8d61e41a73f0.png)

> ex) '심쿵+위피' Negative before 2019 <br/>

![Negative before 2019](https://user-images.githubusercontent.com/63955072/122882649-5f65ad00-d377-11eb-9c81-7302bbc1d2bb.png)

- Data Analysis 
> '심쿵+위피' before 2019 <br/>

>> Positive <br/>
>>> Connectivity (real-time, interface) <br/>
>>> Information (region, distance, evaluation) <br/>
>>> Matching (introduction, variety, marking, neighborhood, recommendation) <br/>

>> Negative
>>> Appearance differentiation (Bronze(rate)) <br/>
>>> Anxiety (affair, theft, fraud) <br/>
>>> Discomfort (tricky, deleted, rejected, managed, cumbersome, inquiring) <br/>

> '심쿵+위피' after 2019 <br/>

>> Positive <br/>
>>> Reality (promise, first time, sound quality, call, conversation) <br/>
>>> Manageability (fiction, delete, manage, member) <br/>
>>> Convenience (optimization, neighborhood, friends, connection, contact, sharing, reason, weekend, proximity) <br/>

>> Negative <br/>
>>> Discrimination (gold(rate), diamond(rate), pushover) <br/>
>>> Waste of time (greetings, short answer, replies, waste of time, cheating) <br/>
>>> Over-advertising (review, advertising, facebook) <br/>
>>> Inconvenience (approval, restriction, age, management) <br/>

> '글램+당연시+아만다+정오' before 2019 <br/>

>> Positive <br/>
>>> Freemium (heart, candy, charging, ribbon) <br/>
>>> Maintenance (ghost member, management, error) <br/>
>>> Informality (region, distance, evaluation) <br/>
>>> Matching (introduction, variety, display, neighborhood, recommended) <br/>

>> Negative <br/>
>>> Entry barriers (matching, photography) <br/>
>>> Customer service (joking, inquiring, answering) <br/>
>>> Overpaid systems (payment induction, beggars, impossible) <br/>
>>> Security (stealing, accounting, suspension) <br/>
>>> Unsatisfactory appearance (men's face, men's pushover) <br/>

> '글램+당연시+아만다+정오' after 2019 <br/>

>> Positive <br/>
>>> Reduced pay (candy, payment, free, cash) <br/>
>>> Content diversification (content, type, variety) <br/>
>>> Matchability (region, proximity, reason, encounter, opportunity) <br/>
>>> Membership type diversity (members, age, gender ratio, similarity, faith) <br/>

>> Negative <br/>
>>> Overpaid system (payment inducement, beggars, cash) <br/>
>>> Satisfaction for cost (purchase, refund) <br/>
>>> Maintenance (ghost member, account, server, administration, connection, error) <br/>

## Conclusion
- Interpretation
> Dating apps with rising sales: Trying to reduce the inconvenience users feel about ghost membership. <br/>
> Dating apps with falling sales: None of the selected applications are coping well with user satisfaction for the cost. <br/>

- Significance
> We weight the review score from a value over TF-IDF rather than a simple frequency Co-occurrence, and then calculate it through the Co-Occurrence value. <br/>
> We judge that we contribute to observing domain revenue variables for dating apps. <br/>
