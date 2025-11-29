import gradio as gr
from main import run_mh_agent

def chat_response(message, history):
    response = run_mh_agent(message)
    return response

ui = gr.ChatInterface(
    fn=chat_response,
    title="💙 Mental Health Support Agent",
    description="A gentle, supportive AI that provides emotional comfort.",
)

if _name_ == "_main_":
    ui.launch()