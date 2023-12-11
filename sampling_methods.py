import pandas as pd
def sample_user(df, n=1):
    users = df['user_id'].drop_duplicates().sample(n=n, random_state=1)
    return users

def sample_tweet(df, user, n=20):
    df = df[df['user_id']== user]['cleaned_tweets']
    if df.shape[0] > n:
        return df.sample(n=n, random_state=1)
    else:
        return df
    
def sample_tweet_group(df, users, n=20):
    result = pd.DataFrame({'user_id':[], 'cleaned_tweets':[]})
    for u in users:
        tweets = sample_tweet(df, u, n=20)
        tweets = pd.DataFrame(tweets).assign(user_id=u)
        result = pd.concat([result, tweets])
    return result

def sampling_and_naming(df, label, names):
    random_5 = df['user_id'].drop_duplicates().sample(n=5)
    sampled_df = df[df['user_id'].isin(random_5)].groupby('user_id').sample(n=25)
    name_map = dict(zip(random_5, [f"{label}_{name}" for name in names]))
    sampled_df['user_id'] = sampled_df['user_id'].map(name_map)
    return sampled_df