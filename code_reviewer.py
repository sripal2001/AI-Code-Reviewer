import google.generativeai as genai  

# Set up Google Gemini
genai.configure(api_key="AIzaSyDr2vLKo30a9WliW_j0j3sbnUx1QM1Da2o")

def review_code(code_snippet, language="Python"):  # Default is Python if no language is given
    prompt = f"Review the following {language} code for errors, best practices, and improvements:\n{code_snippet}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text




# Example: Checking a simple code
sample_code = "def hello():\n    print('Hello, World!')"
print(review_code(sample_code))
