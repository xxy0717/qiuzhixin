import openai
import streamlit as st

# Initialize the OpenAI API key
openai.api_key = "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"

def generate_cover_letter(model, prompt, length, tone):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=length,
        n=1,
        stop=None,
        temperature=tone,
    )

    message = completions.choices[0].text
    return message

def main():
    st.title("Cover Letter Generator")

    model = "text-davinci-002"
    length = st.slider("Length of the cover letter (in tokens)", 50, 500, 200)
    tone = st.slider("Tone of the cover letter", 0.0, 1.0, 0.5)

    name = st.text_input("Your name")
    position = st.text_input("Position you're applying for")
    company = st.text_input("Company name")

    if st.button("Generate cover letter"):
        prompt = (f"Dear hiring manager,\n\n"
                  f"My name is {name} and I am writing to apply for the position of {position} at {company}.\n\n"
                  f"I am excited about this opportunity because ")
        cover_letter = generate_cover_letter(model, prompt, length, tone)
        st.write("\n\n")
        st.write("# Generated Cover Letter\n")
        st.write(cover_letter)

        if st.button("Download cover letter"):
            with open("cover_letter.txt", "w") as file:
                file.write(cover_letter)
                st.success("Cover letter downloaded!")

if __name__ == '__main__':
    main()
