import streamlit as st  
from code_reviewer import review_code  

st.title("AI Code Reviewer")  
code_input = st.text_area("Paste your code here:", height=200)  
language = st.selectbox("Select Programming Language", ["Python", "Java", "C++", "JavaScript"])  
review = review_code(code_input, language)  # Pass it to the function



if st.button("Review Code"):
    review = review_code(code_input, language)
    st.markdown("### Review Results:")
    st.markdown(f"```diff\n{review}\n```")  # This adds color formatting


