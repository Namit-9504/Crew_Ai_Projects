from crewai import Crew , Process
from agents import blog_researcher , blog_writer 
from tasks import task1 , task2

crew = Crew(
    agents = [blog_researcher,blog_writer],
    tasks = [task1,task2],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm =100,
    share_crew = True
)


# start the task execution process 
result = crew.kickoff(inputs={'topic':"AI VS ML VS DL VS Data Science"})
print(result)