from modules.cursorModule import cursor
from api_keys import DB_name
import mysql.connector # For connecting to dataset
from mysql.connector import errorcode # Used in error checking on table creation.

def create_tables():
    cursor.execute ("USE {}".format(DB_name))
    try:        # Create the temp table first (no reason)
        cursor.execute("""CREATE TABLE `tweepy_cashtags_temp` (
        `tweet_id` BIGINT NOT NULL,
        `tweet_id_str` varchar(255),
        `tweet_text_short` text,
        `created_at` varchar(255),
        `derived_URL` varchar(255),
        `source` varchar(255),
        `truncated` varchar(255),
        `in_reply_to_screen_name` varchar(255),
        `in_reply_to_status_id` varchar(255),
        `in_reply_to_user_id` varchar(255),
        `is_quote_status` varchar(255),
        `retweet_count` varchar(255),
        `tweet_language` varchar(255),
        `user_id` BIGINT,
        `user_id_str` varchar(255),
        `name` varchar(255),
        `screen_name` varchar(255),
        `location` varchar(255),
        `derived_account_url` varchar(255),
        `profile_link` varchar(255),
        `user_description` varchar(255),
        `protected` varchar(255),
        `verified` varchar(255),
        `followers_count` BIGINT,
        `friends_count` BIGINT,
        `listed_count` BIGINT,
        `favourites_count` BIGINT,
        `statuses_count` BIGINT,
        `date_user_created` varchar(255),
        `user_utc_offset` varchar(255),
        `user_time_zone` varchar(255),
        `geo_enabled` varchar(255),
        `user_lang` varchar(255),
        `contributors_enabled` varchar(255),
        `is_translator` varchar(255),
        `default_profile` varchar(255),
        `default_profile_image` varchar(255),
        `favorite_count` BIGINT,
        `parsed_user_mentions_id` varchar(255),
        `parsed_user_mentions_screen_name` varchar(255),
        `possibly_sensitive` varchar(255),
        `url_in_tweet` varchar(255),
        `hashtags` varchar(255),
        `cashtags` varchar(255),
        `tweepy_search_term` varchar(255),
        PRIMARY KEY (`tweet_id`)
        ) ENGINE = InnoDB
        """)
        print ("Created table: 'tweepy_cashtags_temp' successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print ("Table 'tweepy_cashtags_temp' already exists.")
        else:
            print (err.msg)

        # Create the main cashtag table
    try:
        cursor.execute("""CREATE TABLE `tweepy_cashtags_main` (
        `tweet_id` BIGINT NOT NULL,
        `tweet_id_str` varchar(255),
        `tweet_text_short` text,
        `created_at` varchar(255),
        `derived_URL` varchar(255),
        `source` varchar(255),
        `truncated` varchar(255),
        `in_reply_to_screen_name` varchar(255),
        `in_reply_to_status_id` varchar(255),
        `in_reply_to_user_id` varchar(255),
        `is_quote_status` varchar(255),
        `retweet_count` varchar(255),
        `tweet_language` varchar(255),
        `user_id` BIGINT,
        `user_id_str` varchar(255),
        `name` varchar(255),
        `screen_name` varchar(255),
        `location` varchar(255),
        `derived_account_url` varchar(255),
        `profile_link` varchar(255),
        `user_description` varchar(255),
        `protected` varchar(255),
        `verified` varchar(255),
        `followers_count` BIGINT,
        `friends_count` BIGINT,
        `listed_count` BIGINT,
        `favourites_count` BIGINT,
        `statuses_count` BIGINT,
        `date_user_created` varchar(255),
        `user_utc_offset` varchar(255),
        `user_time_zone` varchar(255),
        `geo_enabled` varchar(255),
        `user_lang` varchar(255),
        `contributors_enabled` varchar(255),
        `is_translator` varchar(255),
        `default_profile` varchar(255),
        `default_profile_image` varchar(255),
        `favorite_count` BIGINT,
        `parsed_user_mentions_id` varchar(255),
        `parsed_user_mentions_screen_name` varchar(255),
        `possibly_sensitive` varchar(255),
        `url_in_tweet` varchar(255),
        `hashtags` varchar(255),
        `cashtags` varchar(255),
        `tweepy_search_term` varchar(255),
        PRIMARY KEY (`tweet_id`)) ENGINE = InnoDB """)
        print("Table 'tweept_cashtags_main' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print ("Table 'tweepy_cashtags_main' already exists.")
        else:
            print (err.msg)

if __name__ == "__main__":
    create_tables()