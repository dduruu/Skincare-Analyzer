from groq import Groq

# Enter your API key
GROQ_API_KEY = ""
client = Groq(api_key=GROQ_API_KEY)

def analyze_ingredients(ingredients: str):
    system_prompt = "You are a professional Dermatologist and Biochemist. You'll be decoding the ingredients. Analyze skincare ingredients strictly and thoroughly."
    user_prompt = f"""Analyze these ingredients honestly: {ingredients}.
Provide a concise and professional report including each item on a new line:
⚡ Safety Score (0-10)
🚩 Red Flags
💚 Key Ingredients
⚠️ Concerns
✨ Benefits
🌸 Summary
Keep it brief and clear, 5-7 sentences max.
Make sure each section starts on a new line."""

    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.4
    )

    report = completion.choices[0].message.content

    for emoji in ["⚡", "🚩", "💚", "⚠️", "✨","🌸"]:
        report = report.replace(emoji, f"\n{emoji}")

    print(report)
    print("\n========================================\n")

if __name__ == "__main__":
    print("✨🧴 Skincare Ingredient Analysis 🫧✨\n")
    ingredients = input("Paste the ingredient list here:\n")
    analyze_ingredients(ingredients)