import langchain_helper as lch
import streamlit as st
from annotated_text import annotated_text


left, mid, _right = st.columns(3)
with left:
   st.image("./image1.gif")

st.title(":pushpin: PaperFly")
annotated_text(
    ("Made by", "Guryuvraj Singh"),
)

st.caption("Welcome to PaperFly, the ultimate destination for students, researchers, and writers seeking the perfect title for their essays and theses. At PaperFly, we understand that a compelling title is not just a formality—it's the gateway to your work, offering the first glimpse into your thought process and the essence of your research or narrative." )

st.caption("Our innovative platform harnesses the power of advanced algorithms to generate unique, relevant, and engaging titles tailored to your specific content and academic discipline. Whether you're crafting a critical essay, a scientific research paper, or an elaborate thesis, IdeaSpark offers a seamless experience to elevate your works first impression.")


with st.sidebar:
    with st.form("my_form"):
        writing_type = st.selectbox("What is eassay type?", ("Research Paper", "Essay", "Report", "Article"))
        theme = st.text_area(label="What is your theme?", max_chars=15)



        st.text("What do you want?")
        op1 = st.checkbox('A Suitable Title')
        op2 = st.checkbox('Brief Outline')
        op3 = st.checkbox('Resources')

        submitted = st.form_submit_button("Submit")

addons = ""
if op1:
    addons += "A suitable title, "

if op2:
    addons += "a brief outline what can i write, "

if op3:
    addons += "2 urls of resources that i can include, "

if submitted:
    st.text("I will suggest: ")
    response = lch.generate_pet_name(writing_type, theme,addons)
    st.text(response['res'])




# if animal_type == "Cat":
#     pet_color = st.sidebar.text_area(label = "What color is your cat", max_chars=15)

# if animal_type == "Dog":
#     pet_color = st.sidebar.text_area(label = "What color is your Dog", max_chars=15)
    
# if animal_type == "Cow":
#     pet_color = st.sidebar.text_area(label = "What color is your cow", max_chars=15)
    
# if animal_type == "Bird":
#     pet_color = st.sidebar.text_area(label = "What color is your bird", max_chars=15)
    
# if pet_color:
#     st.text("I will suggest: ")
#     response = lch.generate_pet_name(animal_type, pet_color)
#     st.text(response['pet_name'])