from crewai import Agent
from tools import tool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


## Creating a Researcher

blog_researcher = Agent(
    role="Blog Researcher From Youtube Videos",
    goal = "Get the relevant information of video for the topic {topic} from youtube channels;",
    verbose = True,
    memory = True,
    backstory=(
        "Expert in understanding the video content related to the machine learning data science and generative ai"
    ),
    tools=[tool],
    allow_delegation=True # it means that we are trasfering our work to next level
)


## Creating a Blog Writer with YT Tool(Trascriber)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from youtube channels",
    verbose = True,
    memory = True,
    backstory=(
        """ With a flair for simplifying complex topics , you craft
        engaging narratives that captivate and educate , bringing new discoveries to light
        in an accessible manner.
        """
    ),
    tools=[tool],
    allow_delegation=False
)