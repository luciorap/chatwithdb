# Load the database with langchain
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db = SQLDatabase.from_uri("sqlite:///chinook.db")

# Set env var OPENAI_API_KEY or load from a .env file
import config
import os
os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY

# Create the LLM
from langchain.llms import OpenAI
llm = OpenAI(temperature=0, verbose=True,model='gpt-3.5-turbo')

# Create the Chain
chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Formatting Response
formato = """
Data: a question from the user:
create a sqlite3 query
review the results
returns the data
If you have to make any clarification or return any text, always be in English
# {question}
"""

# Function to make the query

def question(input_user):
    cons = formato.format(question = input_user)
    result = chain.run(cons)
    return(result)