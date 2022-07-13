import pandas as pd
# function to remove item or candidate with score lower then the threshold
def remove_unfit_candidate(dict, threshold):
    count = 0
    items = len(dict)
    for i in range(1,items):
        if dict[i].fit < threshold:
            dict.pop(i)
            count+=1
    print(f"with threshold {threshold}, total of {count} candidate(s) was/were removed")
    print(f"There are {len(dict)} left")
    return dict

# method for ranking candidate
def ranking(candidates_dict):
    id = []
    rank_score = []
    fit_score = []
    for i in candidates_dict:
        fit_score.append(candidates_dict[i].fit)
        id. append(candidates_dict[i].id)
        rank_score.append(average_score(candidates_dict[i].fit, candidates_dict[i].connections))
    data = {'candidate_id': id, 'candidate_fit_score': fit_score, 'fit_score_connections_base': rank_score}
    df = pd.DataFrame(data)
    df['rank'] = df['fit_score_connections_base'].rank(method='max')
    print(df)

def average_score(score1, score2):
    # score 2 represent connection
    score2 = 1 / (score2 + 10)
    # having more connection will result in minimal reduction
    return score1 - score2