## Add all required imports here ##
import streamlit as st
from llama_cpp import Llama
import datetime
import random
import string
from time import sleep
import tiktoken

import subprocess

if __name__ == '__main__':
    #subprocess.run("llamafile-0.8.12.exe -m model/Lite-Mistral-150M-v2-Instruct-Q8_0.gguf -c 2048 --nobrowser --host 0.0.0.0")
    #subprocess.run('start cmd.exe /k .\llamafile-0.8.12.exe -m .\model\Lite-Mistral-150M-v2-Instruct-Q8_0.gguf -c 2048 --host 0.0.0.0 --nobrowser',shell=True)
    subprocess.run("streamlit run stapp.py")