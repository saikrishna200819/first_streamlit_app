import streamlit

streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text(' 🐔 Hard-boiled free range-egg')

streamlit.text('🥑🍞 Avacoado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#importing data from a CSV file which is in S3 bucket and setting fruit column as index
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


# display the table on the page.
streamlit.dataframe(fruits_to_show)

#############################################################

#streamlit.header("Fruityvice Fruit Advice!")

#imported requests library and gettiing data from fruityvice website into our app
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

# we used normalize to normalize the data
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display it in the table form
#streamlit.dataframe(fruityvice_normalized)

##################################################################

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

################################################
###

#don't run anything past here while we troubleshoot
streamlit.ctop()

import snowflake.connector

##my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
##my_cur = my_cnx.cursor()
##my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
##my_data_row = my_cur.fetchone()
##streamlit.text("Hello from Snowflake:")
##streamlit.text(my_data_row)


####################################

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)

#####################################################

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")
#############################

fruit_added = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding:', fruit_added)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_added)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)



