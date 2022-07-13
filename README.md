# HjVvdFbjSUZU4qzL
Third Machine Learning Project

Background:

As a talent sourcing and management company, we are interested in finding talented individuals for sourcing these candidates to technology companies. Finding talented candidates is not easy, for several reasons. The first reason is one needs to understand what the role is very well to fill in that spot, this requires understanding the client’s needs and what they are looking for in a potential candidate. The second reason is one needs to understand what makes a candidate shine for the role we are in search for. Third, where to find talented individuals is another challenge.

The nature of our job requires a lot of human labor and is full of manual operations. Towards automating this process we want to build a better approach that could save us time and finally help us spot potential candidates that could fit the roles we are in search for. Moreover, going beyond that for a specific role we want to fill in we are interested in developing a machine learning powered pipeline that could spot talented individuals, and rank them based on their fitness.

We are right now semi-automatically sourcing a few candidates, therefore the sourcing part is not a concern at this time but we expect to first determine best matching candidates based on how fit these candidates are for a given role. We generally make these searches based on some keywords such as “full-stack software engineer”, “engineering manager” or “aspiring human resources” based on the role we are trying to fill in. These keywords might change, and you can expect that specific keywords will be provided to you.

Assuming that we were able to list and rank fitting candidates, we then employ a review procedure, as each candidate needs to be reviewed and then determined how good a fit they are through manual inspection. This procedure is done manually and at the end of this manual review, we might choose not the first fitting candidate in the list but maybe the 7th candidate in the list. If that happens, we are interested in being able to re-rank the previous list based on this information. This supervisory signal is going to be supplied by starring the 7th candidate in the list. Starring one candidate actually sets this candidate as an ideal candidate for the given role. Then, we expect the list to be re-ranked each time a candidate is starred.

Data Description:

Attributes:
id : unique identifier for candidate (numeric)

job_title : job title for candidate (text)

location : geographical location for candidate (text)

connections: number of connections candidate has, 500+ means over 500 (text)

Output (desired target):
fit - how fit the candidate is for the role? (numeric, probability between 0-1)

Keywords: “Aspiring human resources” or “seeking human resources”

Download Data:

https://docs.google.com/spreadsheets/d/117X6i53dKiO7w6kuA1g1TpdTlv1173h_dPlJt5cNNMU/edit?usp=sharing

Goal(s):

Predict how fit the candidate is based on their available information (variable fit)

Success Metric(s):

Rank candidates based on a fitness score.

Re-rank candidates when a candidate is starred.

Bonus(es):

We are interested in a robust algorithm, tell us how your solution works and show us how your ranking gets better with each starring action.

How can we filter out candidates which in the first place should not be in this list?

Can we determine a cut-off point that would work for other roles without losing high potential candidates?

Do you have any ideas that we should explore so that we can even automate this procedure to prevent human bias?

EDA:
- The data provided indicated we have to use unsupervised method since there are no training sample provided
- The keyword used match with the candidate job title
- candidate with more connection will be rank higher
- connection column include both character and number, remove character and convert it from string to digit (number)
- candidate can have more than 1 job title
- in the keyword did not mention the location of the job. If location is mention it would help in the ranking process

  First 10 data in the dataset:
  id                                          job_title  ... connection fit
0   1  2019 C.T. Bauer College of Business Graduate (...  ...         85 NaN
1   2  Native English Teacher at EPIK (English Progra...  ...      500+  NaN
2   3              Aspiring Human Resources Professional  ...         44 NaN
3   4             People Development Coordinator at Ryan  ...      500+  NaN
4   5    Advisory Board Member at Celal Bayar University  ...      500+  NaN
5   6                Aspiring Human Resources Specialist  ...          1 NaN
6   7  Student at Humber College and Aspiring Human R...  ...         61 NaN
7   8                               HR Senior Specialist  ...      500+  NaN
8   9  Student at Humber College and Aspiring Human R...  ...         61 NaN
9  10  Seeking Human Resources HRIS and Generalist Po...  ...      500+  NaN

[10 rows x 5 columns]
Shape of data (in (row:column) format):  (104, 5)
               id  fit
count  104.000000  0.0
mean    52.500000  NaN
std     30.166206  NaN
min      1.000000  NaN
25%     26.750000  NaN
50%     52.500000  NaN
75%     78.250000  NaN
max    104.000000  NaN

RangeIndex: 104 entries, 0 to 103
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   id          104 non-null    int64  
 1   job_title   104 non-null    object 
 2   location    104 non-null    object 
 3   connection  104 non-null    object 
 4   fit         0 non-null      float64
dtypes: float64(1), int64(1), object(3)
memory usage: 4.2+ KB


Algorithm:
- In this project I used NLP (natural language processing) to find similarity between
the keyword and candidate's job title. This will provide a similarity score between 
each candidate with the keyword.
- After calculating the probability score, I added connection as a factor to rank candidate.
- Setting a threshod value to eliminate inrelevance candidate, a threshod of 0.5 to 0.7 will eliminate candidate with less than the threshold (shortlisted)
- I used fit_score - (1/number_of_connections +10) because the more connection a candidate have the less reduction from the original score is. I add 10 to number_of_connections to make sure there is no 0 connection that lead to 0 division and candidate with 1 connection will cause the function to be 1 this might reduce the point of the candidate significantly

area to be impoved: add location to keyword to only select candidate within the job posting location


Resources:
- EDA:
  https://www.geeksforgeeks.org/what-is-exploratory-data-analysis/

- K-mean
  https://www.geeksforgeeks.org/k-means-clustering-introduction/

- Cosine Similarity
  https://studymachinelearning.com/cosine-similarity-text-similarity-metric/

- Ranking algorithms
  https://towardsdatascience.com/ranking-algorithms-know-your-multi-criteria-decision-solving-techniques-20949198f23e