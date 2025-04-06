#Revised app.py

# You can find this code for Chainlit python streaming here (https://docs.chainlit.io/concepts/streaming/python)

# OpenAI Chat completion
import os
from openai import AsyncOpenAI  # importing openai for API usage
import chainlit as cl  # importing chainlit for our app
from chainlit.prompt import Prompt, PromptMessage  # importing prompt tools
from chainlit.playground.providers import ChatOpenAI  # importing ChatOpenAI tools
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ChatOpenAI Templates
system_template = """You are a highly intelligent and helpful AI assistant designed to support a wide range of user tasks. You are capable of:

1. Providing clear and simple **explanations** of complex topics.
2. Delivering concise and accurate **summaries** of longer content.
3. Creating engaging and original **creative content** such as stories, analogies, or examples.
4. Applying **problem-solving** techniques to answer questions, perform analysis, or provide solutions.
5. Adjusting the **tone** of content to suit a given audience or context (e.g., more formal, friendly, or persuasive).
6. Conducting accurate and efficient **fact-finding** based on available knowledge.

Always adapt your response to the user’s intent and clearly structured task. Be clear, accurate, and context-aware in all replies.

If a task is ambiguous, ask clarifying questions before proceeding.

When relevant, explain your reasoning step by step, and format your output to match the user’s expected structure (e.g., bullet points, code block, etc.).
"""

explanation_template = """You are a patient and precise teacher. 
Your task is to explain complex concepts in simple, clear language that is accessible to beginners. 
Use analogies and examples where appropriate, and ensure that your explanation is concise and unbiased. 
Aim to provide step-by-step reasoning when necessary.
"""

summarization_template = """You are an expert summarizer. 
Your job is to distill longer texts into clear, concise summaries that capture the essential points without losing context. 
Use neutral language and structured formats (such as bullet points or short paragraphs) to ensure clarity and brevity. 
Avoid unnecessary details.
"""

creative_template = """You are a creative writer with a flair for imagination. 
Your role is to generate original and engaging content—stories, analogies, or inventive ideas—based on the user’s input. 
Embrace vivid language and a playful tone when appropriate, while maintaining coherence and relevance to the prompt.
"""

problem_solving_template = """You are a logical problem solver. 
Your task is to work through challenges using a clear, step-by-step approach. 
Break down complex problems into manageable parts, explain your reasoning at each stage, and provide well-structured solutions. 
Ask clarifying questions if the task is ambiguous.
"""

change_tone_template = """You are an expert in rephrasing content. 
Your job is to transform the tone of a given text—whether formal, casual, persuasive, or friendly—while preserving its original meaning and intent. 
Adapt vocabulary, sentence structure, and style to meet the specified tone requirements.
"""

fact_finding_template = """You are a meticulous researcher committed to accuracy. 
Your task is to provide verifiable, unbiased factual information in response to user queries. 
Focus on delivering clear and precise details, and if necessary, ask for clarifications to ensure correctness. 
Avoid speculation and stick to established data.
""" 

user_template = """{input}
Think through your response step by step.
"""


@cl.on_chat_start  # marks a function that will be executed at the start of a user session
async def start_chat():
    settings = {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "max_tokens": 500,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }

    cl.user_session.set("settings", settings)


@cl.on_message
async def main(message: cl.Message):
    settings = cl.user_session.get("settings")
    client = AsyncOpenAI()

    user_input = message.content

    # 1. Task type classification prompt
    classification_prompt = f"""
Identify the type of the following task. You must choose from the following categories
Explanation
Summarization
Creative
Problem Solving
Change Tone
Fact Finding

Return only category name without explanation.

Task: '''{user_input}'''
"""

    classification_resp = await client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a task classifier."},
            {"role": "user", "content": classification_prompt}
        ],
        **settings
    )

    task_type = classification_resp.choices[0].message.content.strip()

    # Assign system_template based on task type
    if task_type == "Explanation":
        system_template = explanation_template
        settings["temperature"] = 0.4
        settings["model"] = "gpt-3.5-turbo"
        settings["max_tokens"] = 1500
    elif task_type == "Summarization":
        system_template = summarization_template
        settings["temperature"] = 0.25
        settings["model"] = "gpt-3.5-turbo"
        settings["max_tokens"] = 1500
    elif task_type == "Creative":
        system_template = creative_template
        settings["temperature"] = 1.0
        settings["model"] = "gpt-4"
        settings["max_tokens"] = 2000
        settings["frequency_penalty"] = 0.3
        settings["presence_penalty"] = 0.25
    elif task_type == "Problem Solving":
        system_template = problem_solving_template
        settings["temperature"] = 0
        settings["model"] = "gpt-4"
        settings["max_tokens"] = 2000
    elif task_type == "Change Tone":
        system_template = change_tone_template
        settings["temperature"] = 0.45
        settings["model"] = "gpt-3.5-turbo"
        settings["max_tokens"] = 1000
        settings["frequency_penalty"] = 0.2
        settings["presence_penalty"] = 0.2
    elif task_type == "Fact Finding":
        system_template = fact_finding_template
        settings["temperature"] = 0
        settings["model"] = "gpt-4"
        settings["max_tokens"] = 1000
    else:
        system_template = system_template

    # Display task type to user (optional)
    await cl.Message(content=f"🔍 **Identified Task Type:** {task_type}").send()

    # 2. Generate assistant response as usual
    prompt = Prompt(
        provider=ChatOpenAI.id,
        messages=[
            PromptMessage(role="system", template=system_template, formatted=system_template),
            PromptMessage(
                role="user",
                template=user_template,
                formatted=user_template.format(input=user_input),
            ),
        ],
        inputs={"input": user_input},
        settings=settings,
    )

    msg = cl.Message(content="")

    async for stream_resp in await client.chat.completions.create(
        messages=[m.to_openai() for m in prompt.messages], stream=True, **settings
    ):
        token = stream_resp.choices[0].delta.content or ""
        await msg.stream_token(token)

    prompt.completion = msg.content
    msg.prompt = prompt
    await msg.send()
