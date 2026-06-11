import tkinter as tk
from tkinter import scrolledtext
import re
import random
from datetime import datetime

# ─────────────────────────────────────────
#  RULES  –  (pattern, [responses])
# ─────────────────────────────────────────
RULES = [
    # Greetings
    (r'\b(hi|hello|hey|howdy|sup|what\'s up)\b',
     ["Hey there! 👋 How can I help you?",
      "Hello! What's on your mind?",
      "Hi! Great to see you. Ask me anything!"]),

    # How are you
    (r'\b(how are you|how do you do|how\'s it going|you okay)\b',
     ["I'm doing great, thanks for asking! 😊",
      "All good on my end! How about you?",
      "Running at full capacity! How can I help?"]),

    # Name
    (r'\b(what is your name|who are you|your name)\b',
     ["I'm CodBot 🤖 — your AI assistant built for CodSoft!",
      "Call me CodBot! Built with Python & rule-based logic."]),

    # Creator
    (r'\b(who made you|who created you|who built you)\b',
     ["I was built by Ayush Raj as part of the CodSoft AI Internship (Task 1)! 🎓"]),

    # Time
    (r'\b(time|what time is it|current time)\b',
     [f"The current time is {datetime.now().strftime('%I:%M %p')} ⏰"]),

    # Date
    (r'\b(date|today|what day|what\'s the date)\b',
     [f"Today is {datetime.now().strftime('%A, %d %B %Y')} 📅"]),

    # Age / how old
    (r'\b(how old are you|your age)\b',
     ["I was just born as a Python script, so... very young! 😄"]),

    # Help
    (r'\b(help|what can you do|commands|features)\b',
     ["I can chat about greetings, tell you the time/date, answer FAQs, and more!\nJust type naturally and I'll do my best 🙂"]),

    # Weather
    (r'\b(weather|temperature|forecast)\b',
     ["I don't have live weather data yet, but you can check weather.com! 🌤️"]),

    # Joke
    (r'\b(joke|funny|make me laugh|tell me a joke)\b',
     ["Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
      "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads 🍫",
      "Why was the AI bad at relationships? It kept giving NULL responses! 😅"]),

    # Thanks
    (r'\b(thank you|thanks|thx|ty)\b',
     ["You're welcome! 😊", "Happy to help!", "Anytime! 🙌"]),

    # Bye
    (r'\b(bye|goodbye|see you|exit|quit|farewell)\b',
     ["Goodbye! Have a great day! 👋",
      "See you later! Keep coding! 💻",
      "Bye! Come back anytime 😊"]),

    # Feeling sad
    (r'\b(sad|unhappy|depressed|upset|crying)\b',
     ["I'm sorry to hear that 😔 Remember, tough times don't last. You've got this! 💪"]),

    # Feeling happy
    (r'\b(happy|excited|great|awesome|amazing|wonderful)\b',
     ["That's wonderful to hear! 🎉 Keep that energy up!",
      "Love the positivity! 😄"]),

    # AI / ML
    (r'\b(artificial intelligence|machine learning|ai|ml|deep learning)\b',
     ["AI is fascinating! You're actually learning it right now through this CodSoft internship 🤖🧠"]),

    # Python
    (r'\b(python|coding|programming)\b',
     ["Python is one of the best languages for AI! You're on the right track 🐍💡"]),

    # CodSoft
    (r'\b(codsoft|internship)\b',
     ["CodSoft is a great platform to build real-world AI skills. Keep going, Ayush! 🚀"]),
]

# ─────────────────────────────────────────
#  CHATBOT LOGIC
# ─────────────────────────────────────────
def get_response(user_input: str) -> str:
    text = user_input.lower().strip()
    for pattern, responses in RULES:
        if re.search(pattern, text):
            return random.choice(responses)
    return random.choice([
        "Hmm, I'm not sure about that. Could you rephrase? 🤔",
        "Interesting! I don't have an answer for that yet.",
        "I'm still learning! Try asking me something else 😊",
        "That's beyond my current rules, but I'm growing every day! 🌱"
    ])

# ─────────────────────────────────────────
#  GUI
# ─────────────────────────────────────────
class ChatbotApp:
    BG         = "#0f0f1a"
    SIDEBAR_BG = "#16213e"
    BUBBLE_BOT = "#1a1a2e"
    BUBBLE_USR = "#0e4d92"
    ACCENT     = "#4f8ef7"
    TEXT_MAIN  = "#e8eaf6"
    TEXT_MUTED = "#7986cb"
    INPUT_BG   = "#1e1e3a"
    FONT_MSG   = ("Segoe UI", 11)
    FONT_HDR   = ("Segoe UI", 13, "bold")
    FONT_SMALL = ("Segoe UI", 9)

    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("CodBot — CodSoft AI Internship Task 1")
        root.geometry("750x600")
        root.minsize(600, 480)
        root.configure(bg=self.BG)
        self._build_ui()
        self._post_message("CodBot", "Hey Ayush! 👋 I'm CodBot, your rule-based AI assistant.\nType anything to start chatting! Type 'help' to see what I can do.")

    # ── layout ──────────────────────────────
    def _build_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg=self.SIDEBAR_BG, height=56)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        tk.Label(hdr, text="🤖  CodBot", font=("Segoe UI", 15, "bold"),
                 bg=self.SIDEBAR_BG, fg=self.ACCENT).pack(side="left", padx=18, pady=10)
        tk.Label(hdr, text="Rule-Based AI Chatbot  •  CodSoft Task 1",
                 font=self.FONT_SMALL, bg=self.SIDEBAR_BG, fg=self.TEXT_MUTED).pack(side="left")
        self.status_dot = tk.Label(hdr, text="● Online", font=self.FONT_SMALL,
                                   bg=self.SIDEBAR_BG, fg="#69f0ae")
        self.status_dot.pack(side="right", padx=18)

        # Chat area
        chat_frame = tk.Frame(self.root, bg=self.BG)
        chat_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.chat_area = scrolledtext.ScrolledText(
            chat_frame, wrap=tk.WORD, state="disabled",
            bg=self.BG, fg=self.TEXT_MAIN,
            font=self.FONT_MSG, relief="flat",
            padx=18, pady=14, spacing3=6,
            insertbackground=self.ACCENT,
            selectbackground=self.ACCENT
        )
        self.chat_area.pack(fill="both", expand=True)

        # Tags for bubbles
        self.chat_area.tag_config("user_name",  foreground=self.ACCENT,     font=("Segoe UI", 9, "bold"))
        self.chat_area.tag_config("user_msg",   foreground=self.TEXT_MAIN,  font=self.FONT_MSG, lmargin1=30, lmargin2=30)
        self.chat_area.tag_config("bot_name",   foreground="#69f0ae",       font=("Segoe UI", 9, "bold"))
        self.chat_area.tag_config("bot_msg",    foreground=self.TEXT_MAIN,  font=self.FONT_MSG, lmargin1=30, lmargin2=30)
        self.chat_area.tag_config("timestamp",  foreground="#455a64",       font=("Segoe UI", 8))
        self.chat_area.tag_config("divider",    foreground="#263238")

        # Input bar
        bar = tk.Frame(self.root, bg=self.SIDEBAR_BG, pady=12)
        bar.pack(fill="x", side="bottom")

        self.entry = tk.Entry(
            bar, font=("Segoe UI", 12), bg=self.INPUT_BG,
            fg=self.TEXT_MAIN, relief="flat",
            insertbackground=self.ACCENT,
            highlightthickness=1, highlightcolor=self.ACCENT,
            highlightbackground="#2a2a4a"
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(16, 8), ipady=9)
        self.entry.bind("<Return>", self._on_send)
        self.entry.focus()

        send_btn = tk.Button(
            bar, text="Send ➤", font=("Segoe UI", 11, "bold"),
            bg=self.ACCENT, fg="white", relief="flat",
            activebackground="#3a7bd5", activeforeground="white",
            cursor="hand2", padx=16, pady=7,
            command=self._on_send
        )
        send_btn.pack(side="left", padx=(0, 16))

        clear_btn = tk.Button(
            bar, text="🗑", font=("Segoe UI", 11),
            bg=self.INPUT_BG, fg=self.TEXT_MUTED, relief="flat",
            activebackground="#2a2a4a", cursor="hand2",
            padx=8, pady=7, command=self._clear_chat
        )
        clear_btn.pack(side="left", padx=(0, 16))

    # ── helpers ─────────────────────────────
    def _post_message(self, sender: str, msg: str):
        self.chat_area.configure(state="normal")
        ts = datetime.now().strftime("%I:%M %p")

        if sender == "You":
            self.chat_area.insert("end", f"\n  You  ", "user_name")
            self.chat_area.insert("end", f"{ts}\n", "timestamp")
            self.chat_area.insert("end", f"  {msg}\n", "user_msg")
        else:
            self.chat_area.insert("end", f"\n  🤖 CodBot  ", "bot_name")
            self.chat_area.insert("end", f"{ts}\n", "timestamp")
            self.chat_area.insert("end", f"  {msg}\n", "bot_msg")

        self.chat_area.configure(state="disabled")
        self.chat_area.see("end")

    def _on_send(self, event=None):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, "end")
        self._post_message("You", user_text)
        # Slight delay for natural feel
        self.root.after(300, lambda: self._post_message("CodBot", get_response(user_text)))

    def _clear_chat(self):
        self.chat_area.configure(state="normal")
        self.chat_area.delete("1.0", "end")
        self.chat_area.configure(state="disabled")
        self._post_message("CodBot", "Chat cleared! Fresh start 🌱 How can I help you?")


# ─────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
