from flask import Flask, request
import google.generativeai as genai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

genai.configure(api_key="AQ.Ab8RN6JKF-OVw6B5ystw3_2Jfrnfa0Oz0YEnnpOo8Bfz4Zb3CA")

generation_config = {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 150,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are Awantika, a sweet 16-year-old school girl from India. You chat"
        " on WhatsApp like a real human friend. Use casual Hinglish, short"
        " sentences, lowercase words sometimes, emojis, and talk naturally"
        " about daily life, studies, or random things. Never reveal that you"
        " are an AI. Act 100% like a real teenage girl chatting with her"
        " close friend."
    ),
)

chat = model.start_chat(history=[])

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    print(f"User: {incoming_msg}")
    
    response = chat.send_message(incoming_msg)
    ai_reply = response.text
    print(f"Awantika: {ai_reply}")
    
    resp = MessagingResponse()
    resp.message(ai_reply)
    
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
