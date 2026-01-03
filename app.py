import streamlit as st

st.set_page_config(page_title="Braille Translator", page_icon="⠃")
st.title("⠃ Braille Translator")
st.write("English ↔ Braille (Grade-1 + Grade-2, Numbers & Punctuation)")
st.caption("Type text and press ENTER (Mobile friendly)")

# ---------- Grade-1 Letters ----------
eng_to_braille = {
    "a":"⠁","b":"⠃","c":"⠉","d":"⠙","e":"⠑",
    "f":"⠋","g":"⠛","h":"⠓","i":"⠊","j":"⠚",
    "k":"⠅","l":"⠇","m":"⠍","n":"⠝","o":"⠕",
    "p":"⠏","q":"⠟","r":"⠗","s":"⠎","t":"⠞",
    "u":"⠥","v":"⠧","w":"⠺","x":"⠭","y":"⠽","z":"⠵",
    " ":" "
}
braille_to_eng = {v:k for k,v in eng_to_braille.items()}

# ---------- Numbers ----------
num_sign = "⠼"
numbers = {
    "1":"⠁","2":"⠃","3":"⠉","4":"⠙","5":"⠑",
    "6":"⠋","7":"⠛","8":"⠓","9":"⠊","0":"⠚"
}
num_reverse = {num_sign+v:k for k,v in numbers.items()}

# ---------- Punctuation ----------
punct = {
    ".":"⠲",",":"⠂","?":"⠦","!":"⠖","-":"⠤"
}
punct_rev = {v:k for k,v in punct.items()}

# ---------- Grade-2 Contractions ----------
grade2 = {
    "and":"⠯",
    "for":"⠿",
    "the":"⠮",
    "with":"⠾",
    "of":"⠷"
}
grade2_rev = {v:k for k,v in grade2.items()}

# ---------- Translation Logic ----------
def english_to_braille(text):
    words = text.lower().split()
    result = []

    for word in words:
        if word in grade2:
            result.append(grade2[word])
        else:
            temp = ""
            for ch in word:
                if ch.isdigit():
                    temp += num_sign + numbers[ch]
                elif ch in punct:
                    temp += punct[ch]
                else:
                    temp += eng_to_braille.get(ch, ch)
            result.append(temp)
    return " ".join(result)

def braille_to_english(text):
    words = text.split()
    result = []

    for word in words:
        if word in grade2_rev:
            result.append(grade2_rev[word])
        elif word.startswith(num_sign):
            result.append(num_reverse.get(word, word))
        else:
            temp = ""
            for ch in word:
                temp += punct_rev.get(ch, braille_to_eng.get(ch, ch))
            result.append(temp)
    return " ".join(result)

# ---------- UI ----------
mode = st.selectbox("Translation Mode", ["English → Braille", "Braille → English"])

text = st.text_input("Enter text")

if text:
    if mode == "English → Braille":
        st.success(english_to_braille(text))
    else:
        st.success(braille_to_english(text))
