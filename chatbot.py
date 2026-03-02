import streamlit as st
import random
import time
from datetime import datetime

# Page config
st.set_page_config(
    page_title="🤖 Nayana's AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 Nayana's AI Chatbot")
st.markdown("---")
st.markdown("<center>✨ Created by Nayana | Python Developer ✨</center>", unsafe_allow_html=True)
st.markdown("---")

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello Nayana! 👋 I'm your personal AI assistant. I know you love Python, coding, and your favorite color is black! How can I help you today?"}
    ]

# Game states
if "number_game" not in st.session_state:
    st.session_state.number_game = None
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

# Responses
responses = {
    "hello": "Hi Nayana! Great to see you! 👋",
    "hi": "Hello Nayana! How's your coding going today?",
    "how are you": "I'm doing great! Ready to help you!",
    "who are you": "I'm Nayana's personal AI assistant!",
    "about me": "You're Nayana! You love Python, black color, coding, dream to be Developer, and like Oats!",
    "python": "Python is your favorite! 🐍",
    "coding": "Coding is your passion! Keep building! 💻",
    "developer": "Your dream to become Developer is amazing! 🚀",
    "oats": "Oats are healthy and delicious! 🥣",
    "black": "Black is an elegant color! ⚫",
    "time": f"Current time is: {datetime.now().strftime('%I:%M %p')}",
    "date": f"Today's date is: {datetime.now().strftime('%B %d, %Y')}",
    "joke": random.choice([
        "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did Nayana become a programmer? Because she loves coding more than Oats! 😄",
    ]),
    "fact": random.choice([
        "Python was named after Monty Python, not the snake!",
        "The first computer bug was an actual moth!",
    ]),
    "motivate": random.choice([
        "You're doing great Nayana! Keep coding! 💪",
        "Every expert was once a beginner! 🌟",
    ]),
    "compliment": random.choice([
        "You're an amazing Python programmer Nayana! 🌟",
        "Your coding skills are impressive! 🔥",
    ]),
    "games": "Try: 'guess number', 'quiz', 'riddle'",
    "guess number": "I'm thinking of a number between 1-10. What's your guess?",
    "quiz": "Python Quiz: What is 2**3? (A:6, B:8, C:9, D:10)",
    "riddle": "What has keys but can't open locks? (Answer: piano)",
    "story": "Once upon a time, Nayana built an amazing chatbot! 📚",
    "fortune": "You will become a great Python developer! 🔮",
    "bye": "Goodbye Nayana! Keep coding! 👋",
    "thanks": "You're welcome! 😊",
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Number game
    if st.session_state.number_game is not None:
        try:
            guess = int(user_input)
            if guess == st.session_state.number_game:
                st.session_state.number_game = None
                return "🎉 Correct! Play again with 'guess number'"
            elif guess < st.session_state.number_game:
                return "Too low! Try higher"
            else:
                return "Too high! Try lower"
        except:
            return "Please type a number!"
    
    # Quiz
    if "quiz" in str(st.session_state.messages[-3:]) and user_input in ["b", "8"]:
        st.session_state.quiz_score += 1
        return "✅ Correct! 2**3 = 8! +1 point!"
    
    # Check responses
    for key in responses:
        if key in user_input:
            if key == "guess number":
                st.session_state.number_game = random.randint(1, 10)
            return responses[key]
    
    return "That's interesting! Tell me more!"

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here Nayana..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar
with st.sidebar:
    st.header("👩‍💻 Nayana's Space")
    st.markdown("---")
    
    st.markdown("### 🌟 About Nayana:")
    st.markdown("**Name:** Nayana")
    st.markdown("**Favorite:** Python 🐍")
    st.markdown("**Color:** Black ⚫")
    st.markdown("**Hobby:** Coding 💻")
    st.markdown("**Dream:** Developer 🚀")
    st.markdown("**Food:** Oats 🥣")
    
    st.markdown("---")
    
    st.markdown("### 🎮 Games:")
    st.markdown("- 🎲 guess number")
    st.markdown("- 📝 quiz")
    st.markdown("- 🤔 riddle")
    st.markdown("- 📖 story")
    st.markdown("- 🔮 fortune")
    
    st.markdown("---")
    
    # Stats
    msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
    st.markdown(f"### 📊 Stats")
    st.markdown(f"💬 Messages: {msg_count}")
    if st.session_state.quiz_score > 0:
        st.markdown(f"📝 Quiz Score: {st.session_state.quiz_score}")
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat cleared! Ready to help you again Nayana! 👋"}
        ]
        st.session_state.number_game = None
        st.rerun()

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ by Nayana | Python Developer in the making 🚀</center>", unsafe_allow_html=True)