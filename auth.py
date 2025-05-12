import praw
def authenticate():
    reddit = praw.Reddit(
        client_id='qpR2ONyL1A8iD8mJN8VZuQ',
        client_secret='cf0wSQ4bznH22cOmbAc-8D-Gnv7-Mg',
        user_agent='your_user_agent'
    )
    return reddit