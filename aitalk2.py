import streamlit as st
import json
from aibackend2 import models, get_chat_response_from_gpt
from PIL import Image
import datetime

with open('initial_instruction.json', 'r', encoding='utf-8') as file:
    instruction = json.load(file)[0]

# 定义页面
st.set_page_config(layout="wide")
st.title("🤖 千金书——掌上智能神医")

model_id = st.sidebar.selectbox(label = '请选择您偏好的医疗对话基模型',
    options = [key for key,value in models.items()],
    help = '推荐默认模型',
    index=1)
 
image = Image.open('logo.jpg')
st.sidebar.image(image)

if 'date_time' not in st.session_state:
        st.session_state.date_time = None
st.session_state.date_time = datetime.datetime.now() 
st.sidebar.date_input('日期', st.session_state.date_time.date())    # 显示日期
st.sidebar.time_input('时间', st.session_state.date_time.time())    # 显示时间 

st.sidebar.markdown('<br>', unsafe_allow_html=True)
st.session_state.tag = st.sidebar.button('开发者、基模型、微调权重、数据集和计算资源介绍')

if st.session_state.tag:
    model_id = None
    st.markdown("### 基模型")
    st.markdown("-"*100)
    st.markdown("-"*100)
    st.markdown("### LoRA模型权重")
    st.markdown("-"*100)
    st.markdown("-"*100)
    st.markdown("### 数据集")
    st.markdown("-"*100)
    st.markdown("-"*100)
    st.markdown("### 计算资源需求")
    st.markdown("-"*100)
    st.markdown("-"*100)
    
    button1 = st.button('返回')

st.sidebar.markdown('<br>'*3, unsafe_allow_html=True) 
# 默认可保存对话上下文
# "点击“清空所有对话”按钮后将清空上下文
buttonClean = st.sidebar.button("清理会话历史", key="clean")

if model_id:
    if buttonClean:
        st.session_state.messages = [{'role':"assistant", 'content':instruction}]

    # 初始化会话
    if "messages" not in st.session_state:
        st.session_state.messages =[{'role':"assistant", 'content':instruction}]


    # 显示历史会话内容
    for message in st.session_state.messages:
        st.chat_message(message['role']).write(message['content'])

    prompt = st.chat_input()
    if prompt:
        # 将用户提示词储存在会话中，并显示在对话栏中
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        # 调用后端大模型生成接口，并存储和显示大模型的输出
        with st.spinner("AI正在思考中，请稍等..."):    
            response = get_chat_response_from_gpt(st.session_state.messages, models[model_id])
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)



