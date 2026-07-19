import google.generativeai as genai

genai.configure(api_key="AIzaSyAs_DhSEr40Mr_yh-39f2l9QeAAzojJ5f4")

models = genai.list_models()

for m in models:
    print(m.name, "->", m.supported_generation_methods)