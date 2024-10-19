import streamlit as st
import pty
import os


def run_app():
    # Create a pseudoterminal and attach it to the command
    def spawn_and_read():
        def read(fd):
            while True:
                output = os.read(fd, 1024).decode()
                if output:
                    st.session_state.console_output += output

        pty.spawn(['./sshx'])

    spawn_and_read()

# Streamlit UI
st.title("Console Output")

if "console_output" not in st.session_state:
    st.session_state.console_output = ""

# Button to start the application
if st.button("Start App"):
    run_app()

# Display console output
st.text_area("Console", value=st.session_state.console_output, height=400, max_chars=None)
