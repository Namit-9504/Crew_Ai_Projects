from crewai_tools import YoutubeChannelSearchTool

# specify our tool to target our search results
#yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="@krishnaik06") # we can give any youtube channel name here
 
# Given parameters needs to be specified for use of ollama based llms
tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    ),
    youtube_channel_handle="@krishnaik06"
)