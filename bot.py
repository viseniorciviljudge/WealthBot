import os
import requests

# Ab hum key yahan nahi likhenge, system se mangwayenge
API_KEY = os.getenv("GROQ_API_KEY") 

def get_ai_script():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    prompt = "Write a 1-sentence powerful wealth secret hook for a YouTube Short. No emojis, just text."
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    res = requests.post(url, json=data, headers=headers)
    json_data = res.json()
    
    if 'choices' in json_data:
        return json_data['choices'][0]['message']['content']
    else:
        print("Error from Groq:", json_data)
        return "Wealth is a mindset, not just a number."

viral_text = get_ai_script()

manim_template = f"""
from manim import *
class WealthBotScene(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        txt = Text("{viral_text}", color=GOLD, font_size=36).scale(0.8)
        self.play(Write(txt))
        self.play(txt.animate.set_color(YELLOW).scale(1.1))
        self.wait(2)
"""

with open("main.py", "w") as f:
    f.write(manim_template)

print(f"✅ Success! AI Topic: {viral_text}")

