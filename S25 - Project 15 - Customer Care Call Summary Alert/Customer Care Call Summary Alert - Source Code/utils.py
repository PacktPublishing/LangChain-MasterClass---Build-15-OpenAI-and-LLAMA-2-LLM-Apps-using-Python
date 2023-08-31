import whisper
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper
import os

# get from https://platform.openai.com/
os.environ["OPENAI_API_KEY"] = "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"

# get from https://nla.zapier.com/docs/authentication/ after logging in):
os.environ["ZAPIER_NLA_API_KEY"] = "sk-ak-dV0owIyoCEbQJVzZv5F1S5JG77"


def email_summary(file):


    # large language model
    llm = OpenAI(temperature=0)

    # Initializing zapier
    zapier = ZapierNLAWrapper()
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

    # The agent used here is a "zero-shot-react-description" agent. 
    # Zero-shot means the agent functions on the current action only — it has no memory. 
    # It uses the ReAct framework to decide which tool to use, based solely on the tool's description.
    agent = initialize_agent(toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)


    # specify a model, here its BASE
    model = whisper.load_model("base")

   

    # transcribe audio file
    result = model.transcribe(file)
    print(result["text"])

    # Send email using zapier
    agent.run("Send an Email to sharathraju489@gmail.com via gmail summarizing the following text provided below : "+result["text"])


