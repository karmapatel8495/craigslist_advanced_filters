import pandas as pd
import amazon_get
import string
import time
import csv

import nltk
from nltk.corpus import stopwords
import pandas as pd

titles_df = pd.read_csv("titles.csv")
title_list = titles_df["Title"]
craigslist_url_list = titles_df["Link"]
pos_tokens_list = []

for title in title_list:
    title_tokens = nltk.word_tokenize(title)
    pos_tokens = nltk.pos_tag(title_tokens)
    pos_tokens_list.append(pos_tokens)

# gives output sentences which won't have the pos tags given in input parameters
def tag_filter(tag_list, pos_tokens_list):
    final_token_list = []
    for tokens in pos_tokens_list:
        tokens_no_tag = []
        for token_details in tokens:
            if token_details[1] not in tag_list:
                tokens_no_tag.append(token_details[0])
        final_token_list.append(tokens_no_tag)
    return final_token_list

# combine tokens to sentences
def tokens_to_sentences(tokens_list):
    final_sentence_list = []
    for tokens in tokens_list:
        final_sentence_list.append(" ".join(tokens))
    return final_sentence_list

pronoun_tags_list = ["PRP", "PRP$", "WP", "WP$"]
no_pronoun_list = tokens_to_sentences(tag_filter(pronoun_tags_list, pos_tokens_list))

stopwords_tokens_list = stopwords.words("english")
no_stopwords_list = tokens_to_sentences(tag_filter(stopwords_tokens_list, pos_tokens_list))

stopwords_and_pronoun_tags_list = pronoun_tags_list + stopwords_tokens_list
no_stopwords_no_pronouns_list = tokens_to_sentences(tag_filter(stopwords_and_pronoun_tags_list, pos_tokens_list))

# export to csv
titles_df["no_pronouns"] = no_pronoun_list
titles_df["no_stopwords"] = no_stopwords_list
titles_df["no_stopwords_no_pronouns"] = no_stopwords_no_pronouns_list
titles_df.to_csv("nlp.csv")

