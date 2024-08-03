# Gemma2-2b-it-chatbot
Repo of the code from the Medium article about running Gemma2 2b locally

> works with Python 3.11+

### Packages and dependencies
create a virtual environment
```
python -m venv venv
```

Install with pip
```
pip install streamlit==1.36.0 llama-cpp-python==0.2.85 tiktoken
```


### Doownload the model file in the model subdirectory
```
Quantization: gemma-2-2b-it-Q5_K_M.gguf

wget https://huggingface.co/bartowski/gemma-2-2b-it-GGUF/resolve/main/gemma-2-2b-it-Q5_K_M.gguf -OutFile model/gemma-2-2b-it-Q5_K_M.gguf

```


### Model Card
```
NCTX = 8196
CHAT TEMPLATE YES
SYSTEM MESSAGE NOT SUPPORTED
```

Available chat formats from metadata: chat_template.default
```
Using gguf chat template: {{ bos_token }}{% if messages[0]['role'] == 'system' %}{{ raise_exception('System role not supported') }}{% endif %}{% for message in messages %}{% if (message['role'] == 'user') != (loop.index0 % 2 == 0) %}{{ raise_exception('Conversation roles must alternate user/assistant/user/assistant/...') }}{% endif %}{% if (message['role'] == 'assistant') %}{% set role = 'model' %}{% else %}{% set role = message['role'] %}{% endif %}{{ '<start_of_turn>' + role + '
' + message['content'] | trim + '<end_of_turn>
' }}{% endfor %}{% if add_generation_prompt %}{{'<start_of_turn>model
'}}{% endif %}
Using chat eos_token: <eos>
Using chat bos_token: <bos>
```

#### Prompt format
```
<bos><start_of_turn>user
{prompt}<end_of_turn>
<start_of_turn>model
<end_of_turn>
<start_of_turn>model
```

### Create a BAT file
point the path to your project path (iin my case is `C:\Users\FabioMatricardi\Documents\DEV\PortableLLMS\Gemma2-2b`)
```
C:
cd C:\Users\FabioMatricardi\Documents\DEV\PortableLLMS\Gemma2-2b
call .\venv\Scripts\activate.bat
streamlit run .\stapp.py

PAUSE

```

Run the `.bat` file or with the venv activated run
```
streamlit run .\stapp.py
```

