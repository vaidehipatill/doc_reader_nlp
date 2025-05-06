# Main Streamlit UI page

import streamlit as st
from pdf_processor import pdf_to_text, split_text
from vector_store import build_index, query_index
from chatbot import chat_with_gpt

st.set_page_config(page_title="Document Insight Assistant", layout="wide")
st.markdown("<h1 style='color: #2E4053;'>Document Reader</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #566573;'>An academic tool to extract insights and answer questions from your documents.</p>", unsafe_allow_html=True)

uploaded_files = st.sidebar.file_uploader("Upload your PDF documents", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    filenames = []
    total_pages = 0

    for file in uploaded_files:
        text = pdf_to_text(file)
        all_text += text
        filenames.append(file.name)

    st.sidebar.success("Documents processed successfully!")
    st.sidebar.markdown("#### Uploaded Files:")
    for name in filenames:
        st.sidebar.write(f"- {name}")

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Total Documents:** {len(filenames)}")
    st.sidebar.markdown(f"**Total Characters:** {len(all_text):,}")

    with st.expander("🔎 Preview Extracted Text"):
        st.text_area("Extracted Text", all_text[:2000] + "...", height=200)

    chunks = split_text(all_text)
    index, _ = build_index(chunks)

    st.markdown("### Ask a Question")
    st.markdown("<p style='color: #566573;'>Type your question below to query the documents.</p>", unsafe_allow_html=True)

    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    query = st.text_input("Your Question")

    if query:
        retrieved_chunks = query_index(index, chunks, query)
        context = " ".join(retrieved_chunks)
        answer = chat_with_gpt(context, query)

        st.session_state.chat_history.append({"user": query, "bot": answer})

    # Show chat history
    for chat in st.session_state.chat_history[::-1]:
        st.markdown(f"<div style='background-color: #2E4053; padding: 10px; border-radius: 5px;'><strong>Q:</strong> {chat['user']}<br><strong>A:</strong> {chat['bot']}</div><br>", unsafe_allow_html=True)

    if st.session_state.chat_history:
        if st.download_button("Download Q&A History", 
                              data="\n\n".join([f"Q: {c['user']}\nA: {c['bot']}" for c in st.session_state.chat_history]), 
                              file_name="chat_history.txt"):
            st.success("Chat history downloaded!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #95A5A6;'>Project developed by Vaidehi Patil | NLP Course Project | 2025</p>", unsafe_allow_html=True)
