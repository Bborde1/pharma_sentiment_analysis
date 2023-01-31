import pandas as pd
import requests
import tweepy

def construct_twitter_url(search_terms=["pharma"]) -> str:
    complete_url = ",".join(search_terms)
    return complete_url

def get_twitter_data():
    twt_df = pd.read_csv()
    return twt_df