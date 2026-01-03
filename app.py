import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Braille Translator", page_icon="⠃")
st.title("⠃ Braille Translator")
st.write("English ↔ Braille (Grade-1, Grade-2, Numbers & Punctuation)")

# ---------------- LETTERS ----------------
english_to_braille = {
    "a":"⠁","b":"⠃","c":"⠉","d":"⠙","e":"⠑",
    "f":"⠋","g":"⠛","h":"⠓","i":"⠊","j":"⠚",
    "k":"⠅","l":"⠇","m":"⠍","n":"⠝","o":"⠕",
    "p":"⠏","q":"⠟","r":"⠗","s":"⠎","t":"⠞",
    "u":"⠥","v":"⠧","w":"⠺","x":"⠭","y":"⠽","z":"⠵",
    " ":" "
}

braille_to_english = {v: k for k, v in english_to_braille.items()}

# ---------------- NUMBERS ----------------
number_sign = "⠼"
numbers = {
    "1":"⠁","2":"⠃","3":"⠉","4":"⠙","5":"⠑",
    "6":"⠋","7":"⠛","8":"⠓","9":"⠊","0":"⠚"
}
numbers_reverse = {number_sign + v: k for k, v in numbers.items()}

# ---------------- PUNCTUATION ----------------
punctuation = {
    ".":"⠲", ",":"⠂", "?":"⠦", "!":"⠖",
    ":":"⠒", ";":"⠆", "-":"⠤"
}
punctuation_reverse = {v: k for k, v in punctuation.items()}

# ---------------- GRADE-2 WORDS ----------------
grade2_words = {
    "and":"⠯",
    "for":"⠿",
    "the":"⠮",
    "with":"⠾",
    "of":"⠷"
}
grade2_reverse = {v: k for k, v in grade2_words.items()}

# ---------------- FUNCTIONS ----------------
def english_to_braille_grade1(text):
    output = ""
    for ch in text.lower():
        if ch.isdigit():
            output += number_sign + numbers[ch]
        elif ch in punctuation:
            output += punctuation[ch]
        else:
            output += english_to_braille.get(ch, ch)
    return output

def english_to_braille_grade2(text):
    words = text.lower().split()
    result = []

    for w in words:
        if w in grade2_words:
            result.append(grade2_words[w])
        else:
            temp = ""
            for ch in w:
                if ch.isdigit():
                    temp += number_sign + numbers[ch]
                elif ch in punctuation:
                    temp += punctuation[ch]
                else:
                    temp += english_to_braille.get(ch, ch)
            result.append(temp)
    return " ".join(result)

def braille_to_english_text(text):
    words = text.split()
    result = []

    for w in words:
        if w in grade2_reverse:
            result.append(grade2_reverse[w])
        elif w.startswith(number_sign):
            result.append(numbers_reverse.get(w, w))
        else:
            temp = ""
            for ch in w:
                if ch in punctuation_reverse:
                    temp += punctuation_reverse[ch]
                else:
                    temp += braille_to_english.get(ch, ch)
            result.append(temp)
    return " ".join(result)

# ---------------- UI ----------------
mode = st.selectbox(
    "Translation Mode",
    ["English → Braille", "Braille → English"]
)

grade = st.radio(
    "Braille Grade",
    ["Grade-1 (Letters)", "Grade-2 (Contractions)"]
)

text = st.text_area("Enter text:")

if text:
    if mode == "English → Braille":
        if grade == "Grade-1 (Letters)":
            result = english_to_braille_grade1(text)
        else:
            result = english_to_braille_grade2(text)

        st.subheader("Braille Output")
        st.success(result)

    else:
        result = braille_to_english_text(text)
        st.subheader("English Output")
        st.success(result)
