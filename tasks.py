from crewai import Task
from tools import tool
from agents import blog_researcher,blog_writer

# 1st researcher task

task1= Task(
    description=(
        "Indentify the video {topic}. Get deatiled information about the video from the YouTube channel "
    ),
    expected_output='A comprehensive 3 Paragraphs Long report based on the {topic}  of video content',
    tools=[tool],
    agent=blog_researcher
)

# 2nd writer task
task2= Task(
    description=(
        "get the information from the youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the info from the youtube channel video on the topic {topic} and create the content for my blog',
    tools=[tool],
    agent=blog_writer,
    async_executor=False, # It is used to work sequentially  TRUE= Parallel execution
    Output_file = "new-blog-post.md"  # Output File 
)