############# Main file #############
from read_n_processing import read_n_processing_data
from score_n_ranking import remove_unfit_candidate, ranking


# keyword use to find the right candidate
keyword = "seeking human resources"#"Aspiring human resources" # another keyword: “seeking human resources”

# acceptable candidate probability used to eliminate unfit candidate
Threshold = 0.6

# analyze data option
analyze = False

# read and processing data
candidate_dict = read_n_processing_data("data/potential-talents - Aspiring human resources - seeking human resources.csv", keyword, analyze)

# remove candidate with probability below the threshold
re_candidate_dict = remove_unfit_candidate(candidate_dict, Threshold)

#ranked_score = get_cosine_similarity_score(candidate_dict, keyword)
ranking(re_candidate_dict)



