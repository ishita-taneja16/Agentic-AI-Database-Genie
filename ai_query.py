import google.generativeai as genai

# 🔐 API key yaha paste kar
genai.configure(api_key="AIzaSyAs_DhSEr40Mr_yh-39f2l9QeAAzojJ5f4")

model = genai.GenerativeModel("models/gemini-flash-latest")

model = genai.GenerativeModel("models/gemini-flash-latest")

def clean_sql(text):
    return text.replace("```sql", "").replace("```", "").strip()

def generate_sql(question):
    prompt = f"""
    You are an expert SQL generator.

    Convert the given natural language question into a SQL query.

    Table: houses
    Columns:
    - price
    - location
    - BedroomAbvGr
    - Sector

    RULES:
    - Always use LOWER(location) LIKE '%city%' for location filtering
    - If question contains a city (like Mohali), MUST include WHERE condition
    - Use MAX(price) for highest
    - Use MIN(price) for lowest
    - Use COUNT(*) for number of houses
    - Return ONLY SQL query (no explanation)

    Examples:
    Q: highest price in mohali  
    A: SELECT MAX(price) FROM houses WHERE LOWER(location) LIKE '%mohali%';

    Q: number of houses in chandigarh  
    A: SELECT COUNT(*) FROM houses WHERE LOWER(location) LIKE '%chandigarh%';

    Q: 3 bedroom houses in delhi  
    A: SELECT * FROM houses WHERE BedroomAbvGr = 3 AND LOWER(location) LIKE '%delhi%';

    Now convert:

    Question: {question}
    """
    response = model.generate_content(prompt)

    return clean_sql(response.text)