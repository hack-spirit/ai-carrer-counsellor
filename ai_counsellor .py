import os
from openai import OpenAI

# ✅ Replace this with your own OpenAI API key
client = OpenAI(api_key="sk-abc123YOURREALKEY")

# 🎯 Rule-based suggestion system
def suggest_careers(interest):
    interest = interest.lower()
    if "math" in interest or "numbers" in interest:
        return ["Data Scientist", "Statistician", "Accountant"]
    elif "art" in interest or "design" in interest:
        return ["Graphic Designer", "UX/UI Designer", "Animator"]
    elif "computer" in interest or "code" in interest or "technology" in interest:
        return ["Software Developer", "AI Engineer", "Cybersecurity Analyst"]
    elif "people" in interest or "help" in interest or "empathy" in interest:
        return ["Psychologist", "Social Worker", "Human Resources Manager"]
    elif "writing" in interest or "story" in interest:
        return ["Content Writer", "Journalist", "Screenwriter"]
    elif "business" in interest or "management" in interest:
        return ["Business Analyst", "Marketing Manager", "Entrepreneur"]
    elif "nature" in interest or "animals" in interest:
        return ["Biologist", "Veterinarian", "Environmental Scientist"]
    else:
        return ["Career Counselor", "Life Coach", "Explore internships or volunteering"]

# 🧠 GPT-4-based explanation
def explain_careers(user_input, careers):
    prompt = f"""
You are an intelligent and empathetic AI career counselor.

A student said: "{user_input}"

You have suggested these careers: {', '.join(careers)}.

Now explain:
1. Why these careers match their interests
2. What strengths or passions they tap into
3. What type of person would thrive in each of them

Be concise, motivating, and student-friendly.
"""

    response = client.chat.completions.create(
        model="gpt-4",  # Or use "gpt-3.5-turbo" if GPT-4 is not available
        messages=[
            {"role": "system", "content": "You are a professional AI career counselor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# 🖥️ Terminal Chat Loop
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("🎓 Welcome to the GPT-4 AI Career Counselor")
    print("🧠 Share your interests or personality. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("👋 Goodbye! Wishing you a bright future ahead!")
            break

        matched_careers = suggest_careers(user_input)
        print(f"\n📌 Suggested Careers: {', '.join(matched_careers)}")

        try:
            explanation = explain_careers(user_input, matched_careers)
            print(f"\n🤖 GPT-4 Advice:\n{explanation}\n")
        except Exception as e:
            print("⚠️ Error from GPT:", e)

if __name__ == "__main__":
    main()
