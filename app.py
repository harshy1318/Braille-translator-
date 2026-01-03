import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Braille Translator", page_icon="⠃")
st.title("⠃ Braille Translator")
st.write("English ↔ Braille (Grade-1 + Grade-2, Numbers & Punctuation)")
st.caption("Type and press Enter (NO Ctrl, NO Button)")

# ---------------- LETTERS ----------------
eng_to_braille = {
    "a":"⠁","b":"⠃","c":"⠉","d":"⠙","e":"⠑",
    "f":"⠋","g":"⠛","h":"⠓","i":"⠊","j":"⠚",
    "k":"⠅","l":"⠇","m":"⠍","n":"⠝","o":"⠕",
    "p":"⠏","q":"⠟","r":"⠗","s":"⠎","t":"⠞",
    "u":"⠥","v":"⠧","w":"⠺","x":"⠭","y":"⠽","z":"⠵",
    " ":" "
}
braille_to_eng = {v: k for k, v in eng_to_braille.items()}

# ---------------- NUMBERS ----------------
num_sign = "⠼"
numbers = {
    "1":"⠁","2":"⠃","3":"⠉","4":"⠙","5":"⠑",
    "6":"⠋","7":"⠛","8":"⠓","9":"⠊","0":"⠚"
}
num_reverse = {num_sign + v: k for k, v in numbers.items()}

# ---------------- PUNCTUATION ----------------
punct = {
    ".":"⠲", ",":"⠂", "?":"⠦", "!":"⠖",
    ":":"⠒", ";":"⠆", "-":"⠤"
}
punct_reverse = {v: k for k, v in punct.items()}

# ---------------- GRADE-2 ----------------
grade2 = {
    "and":"⠯",
    "for":"⠿",
    "the":"⠮",
    "with":"⠾",
    "of":"⠷"
}
grade2_rev = {v: k for k, v in grade2.items()}

# ---------------- FUNCTIONS ----------------
def english_to_braille(text):
    words = text.lower().split()
    output = []

    for word in words:
        if word in grade2:          # Grade-2 first
            output.append(grade2[word])
        else:
            temp = ""
            for ch in word:
                if ch.isdigit():
                    temp += num_sign + numbers[ch]
                elif ch in punct:
                    temp += punct[ch]
                else:
                    temp += eng_to_braille.get(ch, ch)
            output.append(temp)

    return " ".join(output)

def braille_to_english(text):
    words = text.split()
    output = []

    for word in words:
        if word in grade2_rev:
            output.append(grade2_rev[word])
        elif word.startswith(num_sign):
            output.append(num_reverse.get(word, word))
        else:
            temp = ""
            for ch in word:
                if ch in punct_reverse:
                    temp += punct_reverse[ch]
                else:
                    temp += braille_to_eng.get(ch, ch)
            output.append(temp)

    return " ".join(output)

# ---------------- UI ----------------
mode = st.selectbox("Translation Mode", ["English → Braille", "Braille → English"])

text = st.text_input("Enter text")

if text:
    if mode == "English → Braille":
        st.success(english_to_braille(text))
    else:
        st.success(braille_to_english(text))
