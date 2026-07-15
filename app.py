import streamlit as st

st.title("💬 MyTemanNgobrol")

# Inisialisasi history chat jika belum ada
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Halo! Ada yang bisa saya bantu hari ini?"}]

# Tampilkan history chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input user
if prompt := st.chat_input("Apa yang ingin kamu bicarakan?"):
    # Simpan dan tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Placeholder untuk respon AI
    # Di sini nanti kita panggil fungsi AI lu (misal: panggil_ai(prompt))
    respon_ai = f"Ini respon simulasi untuk: {prompt}"
    
    # Simpan dan tampilkan respon AI
    st.session_state.messages.append({"role": "assistant", "content": respon_ai})
    st.chat_message("assistant").write(respon_ai)