# Input your API Keys and then rename this file to "api_keys.py"

apikey = "AAA" 
apikeysecret = "AAA"
access_token = "AAA"
access_token_secret = "AAA"

rapidapi_key = "BBB" 
twitter_app_auth = {
    'consumer_key': 'AAA',
    'consumer_secret': 'AAA'}
#Note: "consumer_key" and "consumer_secret" were the former names for "API key" and "API Secret".



#### Enter your MySQL database configuration here ####
DB_name = 'traderint' # Name of local database. Used for database creation and connection.

# Configuration for connecting to an existing database. 
config = {
'user': 'root',
'password': 'PASSWORD',
'host' : 'localhost',
'database' : DB_name}

# Configuration for new databases, this is run when no database currently exists.
createDBconfig = {
    'user': 'root',
    'password': 'PASSWORD',
    'host' : 'localhost'}