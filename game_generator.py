# game_generator.py
# Install the OpenAI package
try:
    import openai
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
    import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key or use environment variables for security

def generate_game_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a game developer who writes complete Python games using user ideas."},
            {"role": "user", "content": f"Create a simple Python game based on: {prompt}"}
        ],
        max_tokens=800,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
