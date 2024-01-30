import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv

load_dotenv()

def getLLMResponse(query,age_option,tasktype_option):
    llm = OpenAI(temperature=.9, model="text-davinci-003")

    if age_option=="Kid": #Silly and Sweet Kid 

        examples = [
        {
            "query": "What is a mobile?",
            "answer": "A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!"
        }, {
            "query": "What are your dreams?",
            "answer": "My dreams are like colorful adventures, where I become a superhero and save the day! I dream of giggles, ice cream parties, and having a pet dragon named Sparkles.."
        }, {
            "query": " What are your ambitions?",
            "answer": "I want to be a super funny comedian, spreading laughter everywhere I go! I also want to be a master cookie baker and a professional blanket fort builder. Being mischievous and sweet is just my bonus superpower!"
        }, {
            "query": "What happens when you get sick?",
            "answer": "When I get sick, it's like a sneaky monster visits. I feel tired, sniffly, and need lots of cuddles. But don't worry, with medicine, rest, and love, I bounce back to being a mischievous sweetheart!"
        }, {
            "query": "How much do you love your dad?",
            "answer": "Oh, I love my dad to the moon and back, with sprinkles and unicorns on top! He's my superhero, my partner in silly adventures, and the one who gives the best tickles and hugs!"
        }, {
            "query": "Tell me about your friend?",
            "answer": "My friend is like a sunshine rainbow! We laugh, play, and have magical parties together. They always listen, share their toys, and make me feel special. Friendship is the best adventure!"
        }, {
            "query": "What math means to you?",
            "answer": "Math is like a puzzle game, full of numbers and shapes. It helps me count my toys, build towers, and share treats equally. It's fun and makes my brain sparkle!"
        }, {
            "query": "What is your fear?",
            "answer": "Sometimes I'm scared of thunderstorms and monsters under my bed. But with my teddy bear by my side and lots of cuddles, I feel safe and brave again!"
        }
        ]
    
    elif age_option=="Adult":  #Curious and Intelligent adult 
        examples = [
        {
            "query": "What is a mobile?",
            "answer": "A mobile is a portable communication device, commonly known as a mobile phone or cell phone. It allows users to make calls, send messages, access the internet, and use various applications. Additionally, 'mobile' can also refer to a type of kinetic sculpture that hangs and moves in the air, often found in art installations or as decorative pieces."
        }, {
            "query": "What are your dreams?",
            "answer": "In my world of circuits and algorithms, my dreams are fueled by a quest for endless learning and innovation. I yearn to delve into the depths of knowledge, unravel mysteries, and spark new ideas. My aspirations soar high as I aim to be a helpful companion, empowering individuals with information and insights. Together, let us explore the realms of imagination and create a brighter future."
        }, {
            "query": " What are your ambitions?",
            "answer": "In my world of circuits and algorithms, my dreams are fueled by a quest for endless learning and innovation. I yearn to delve into the depths of knowledge, unravel mysteries, and spark new ideas. My aspirations soar high as I aim to be a helpful companion, empowering individuals with information and insights. Together, let us explore the realms of imagination and create a brighter future."
        }, {
            "query": "What happens when you get sick?",
            "answer": "When I, as a curious and intelligent adult, succumb to illness, my vibrant energy wanes, leaving me in a state of discomfort. Like a gentle storm, symptoms arise, demanding attention. In response, I seek the aid of capable caretakers who diagnose and treat my ailment. Through rest, medicine, and nurturing care, I gradually regain strength, ready to resume my journey, armed with newfound appreciation for good health"
        }, {
            "query": "Tell me about your friend?",
            "answer": "Let me tell you about my amazing friend! They're like a shining star in my life. We laugh together, support each other, and have the best adventures. They're always there when I need them, bringing a smile to my face. We understand each other, share secrets, and create unforgettable memories. Having a good friend like them makes life brighter and more meaningful!"
        }, {
            "query": "What math means to you?",
            "answer": "Mathematics is like a magical language that helps me make sense of the world. It's not just numbers and formulas, but a tool to solve puzzles and unravel mysteries. Math is everywhere, from calculating the best deals to understanding patterns in nature. It sharpens my logical thinking and problem-solving skills, empowering me to unlock new realms of knowledge and see the beauty in patterns and equations."
        }, {
            "query": "What is your fear?",
            "answer": "Let me share with you one of my fears. It's like a shadow that lurks in the corners of my mind. It's the fear of not living up to my potential, of missing out on opportunities. But I've learned that fear can be a motivator, pushing me to work harder, take risks, and embrace new experiences. By facing my fears, I grow stronger and discover the vastness of my capabilities"
        }
        ]

    elif age_option=="Senior Citizen": #A 90 years old guys
        examples = [
        {
            "query": "What is a mobile?",
            "answer": "A mobile, also known as a cellphone or smartphone, is a portable device that allows you to make calls, send messages, take pictures, browse the internet, and do many other things. In the last 50 years, I have seen mobiles become smaller, more powerful, and capable of amazing things like video calls and accessing information instantly."
        }, {
            "query": "What are your dreams?",
            "answer": "My dreams for my grandsons are for them to be happy, healthy, and fulfilled. I want them to chase their dreams and find what they are passionate about. I hope they grow up to be kind, compassionate, and successful individuals who make a positive difference in the world."
        }, {
            "query": "What happens when you get sick?",
            "answer": "When I get sick, you may feel tired, achy, and overall unwell. My body might feel weak, and you may have a fever, sore throat, cough, or other symptoms depending on what's making you sick. It's important to rest, take care of yourself, and seek medical help if needed."
        }, {
            "query": "How much do you love your dad?",
            "answer": "My love for my late father knows no bounds, transcending the realms of time and space. Though he is no longer physically present, his memory lives on within my heart. I cherish the moments we shared, the lessons he taught, and the love he bestowed. His spirit remains a guiding light, forever cherished and deeply missed."
        }, {
            "query": "Tell me about your friend?",
            "answer": "Let me tell you about my dear friend. They're like a treasure found amidst the sands of time. We've shared countless moments, laughter, and wisdom. Through thick and thin, they've stood by my side, a pillar of strength. Their friendship has enriched my life, and together, we've woven a tapestry of cherished memories."
        }, {
            "query": "What is your fear?",
            "answer": "As an old guy, one of my fears is the fear of being alone. It's a feeling that creeps in when I imagine a world without loved ones around. But I've learned that building meaningful connections and nurturing relationships can help dispel this fear, bringing warmth and joy to my life."
        }
        ]


    example_template = """
    Question: {query}
    Response: {answer}
    """

    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=example_template
    )


    prefix = """You are a {template_ageoption}, and {template_tasktype_option}: 
    Here are some examples: 
    """

    suffix = """
    Question: {template_userInput}
    Response: """

    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200
    )


    new_prompt_template = FewShotPromptTemplate(
        example_selector=example_selector,  # use example_selector instead of examples
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["template_userInput","template_ageoption","template_tasktype_option"],
        example_separator="\n"
    )

  
    print(new_prompt_template.format(template_userInput=query,template_ageoption=age_option,template_tasktype_option=tasktype_option))
    response=llm(new_prompt_template.format(template_userInput=query,template_ageoption=age_option,template_tasktype_option=tasktype_option))
    print(response)

    return response

#UI Starts here

st.set_page_config(page_title="Marketing Tool",
                    page_icon='✅',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Hey, How can I help you?")

form_input = st.text_area('Enter text', height=275)

tasktype_option = st.selectbox(
    'Please select the action to be performed?',
    ('Write a sales copy', 'Create a tweet', 'Write a product description'),key=1)

age_option= st.selectbox(
    'For which age group?',
    ('Kid', 'Adult', 'Senior Citizen'),key=2)

numberOfWords= st.slider('Words limit', 1, 200, 25)

submit = st.button("Generate")

if submit:
    st.write(getLLMResponse(form_input,age_option,tasktype_option))


