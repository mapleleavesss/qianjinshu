import os
from openai import OpenAI

# load .env for OPENAI_API_KEY / 加载 .env 到环境变量，其中包含OPENAI_API_KEY
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# configure OpenAI client/ 配置 OpenAI 服务
client = OpenAI()

# define dict for all AI models / 定义大模型ID和对应的实际名称
models = {"GPT4": "gpt-4-turbo-preview", "GPT3.5": "gpt-3.5-turbo"}
# models = {"GPT3.5": "gpt-3.5-turbo"}

# call OpenAI chat completioin API / 调用GPT大模型对话生成接口
def get_chat_response_from_gpt(messages, model):
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return response.choices[0].message.content
