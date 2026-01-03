import streamlit as st

st.set_page_config(page_title="Braille Translator", page_icon="⠃")
st.title("⠃ Braille Translator")
st.write("English ↔ Braille (Auto Grade-1 + Grade-2)")
st.caption("Just type text and press Enter (mobile friendly)")

# ---------- Dictionaries ----------
letters = {
    "a":"⠁","b":"⠃","c":"⠉","d":"⠙","e":"⠑",
    "f":"⠋","g":"⠛","h":"⠓","i":"⠊","j":"⠚",
    "k":"⠅","l":"⠇","m":"⠍","n":"⠝","o":"⠕",
    "p":"⠏","q":"⠟","r":"⠗","s":"⠎","t":"⠞",
    "u":"⠥","v":"⠧","w":"⠺","x":"⠭","y":"⠽","z":"⠵",
    " ":" "
}
reverse_letters = {v:k for k,v in letters.items()}

contractions = {
    "and":"⠯","for":"⠿","the":"⠮","with":"⠾","of":"⠷"
}
reverse_contractions = {v:k for k,v in contractions.items()}

# ---------- Logic ----------
def eng_to_braille(text):
    words = text.lower().split()
    out = []
    for w in words:
        if w in contractions:
            out.append(contractions[w])
        else:
            out.append("".join(letters.get(c, c) for c in w))
    return " ".join(out)

def braille_to_eng(text):
    words = text.split()
    out = []
    for w in words:
        if w in reverse_contractions:
            out.append(reverse_contractions[w])
        else:
            out.append("".join(reverse_letters.get(c, c) for c in w))
    return " ".join(out)

# ---------- UI ----------
mode = st.selectbox("Translation Mode", ["English → Braille", "Braille → English"])
text = st.text_input("Enter text")

if text:
    if mode == "English → Braille":
        st.success(eng_to_braille(text))
    else:
        st.success(braille_to_eng(text))
