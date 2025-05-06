import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="AIzaSyDtfUgEuU0H_MVBa8A1Wwn42P8LsdJ0_qk")

# Configuration for the generation behavior
generation_config = {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Start a new chat session
chat = model.start_chat(history=[])

# ✅ Take user input for the prompt
user_prompt = input("Enter the email type or prompt: ")

# ✅ Send the user prompt to Gemini
response = chat.send_message(user_prompt)

# ✅ Print the AI-generated response
print("\nGenerated Email:\n")
print(response.text)
