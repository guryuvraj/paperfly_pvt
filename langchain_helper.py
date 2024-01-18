from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def generate_pet_name(writing_type, theme, addons):
    llm = OpenAI(temperature=0.7)
 
    prompt_template_name = PromptTemplate(
        input_variables = ['writing_type', 'theme', 'addons'],
        template = "I want to write a {writing_type} on {theme}.suggest me {addons} for this. Tell in few lines."
    )
    name_chain = LLMChain(llm=llm, prompt = prompt_template_name,output_key = "res")
    response = name_chain({'writing_type': writing_type, 'theme': theme, 'addons': addons})
    return response

if __name__ == "__main__":
    print(generate_pet_name("cow","black"))