# API KEYS FOR TWEEPY. #Note: this is the v2 token under -> project 1 - traderi.

from prefect.client import Secret

apikey = Secret("apikey").get()
apikeysecret = Secret("apikeysecret").get()
access_token = Secret("access_token").get()
access_token_secret = Secret("access_token_secret").get()
rapidapi_key = Secret("rapidapi_key").get()
pw = Secret("password").get()



# INSTANTIATE THE API KEYS - NOTE: Botometer v1.6.1 needs v1.1 of twitter API keys (i think).
twitter_app_auth = {
    'consumer_key': apikey,
    'consumer_secret': apikeysecret}
# ^^^ traderi - twitter api v2 keys
#Note: to use app-only authentication, variables "access_token" and "access_token_secret" are removed
#Note2: "consumer_key" and "consumer_secret" were the former names for "API key" and "API Secret" respectively

#### Enter your MySQL database configuration here ####
DB_name = 'traderint' # Name of local database. Used for database creation and connection.

# Configuration for connecting to an existing database. 
config = {
'user': 'root',
'password': pw,
'host' : 'localhost',
'database' : DB_name}

# Configuration for new databases, this is run when no database currently exists.
createDBconfig = {
'user': 'root',
'password': pw,
'host' : 'localhost'}