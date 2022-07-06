# using python 3.9 -> python3.9 prefect-v1.py
# doesnt need to be on python3.9. just did that so its the same as the get bot scores program.

import prefect
from prefect import task, Flow

@task
def get_bot_scores():
	logger = prefect.context.get ("logger")
	logger.info("Running the getBotScores script.")
	import getBotScores

with Flow("Trader-Int Flow") as flow:
	get_bot_scores()

# if __name__ == "__main__":
	# get_bot_scores()

# flow.register(project_name="project-traderi")
flow.run() # For running the file locally - use for development/debugging