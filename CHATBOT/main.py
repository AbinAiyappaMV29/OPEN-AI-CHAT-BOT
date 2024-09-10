import openai
#enter your api key below (api key is free for new accounts for some limited search or you can purchase in open_ai)
Api_Key = open("Api_Key",'r').read()
openai.api_key = Api_Key

chat_log = []

while True:
    user_input = input()
    if user_input.lower() == "quit":
        break
    else:
        chat_log.append({"role": "users", "content": user_input})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=chat_log
        )
        asssitant_responce = responce['choices'][0]['message']['content']
        print("ChatGPT:", assistant_responce.strip("\n".strip()))
        chat_log.append({"role": "assistant", "content": assistatn_responce.strip("\n").strip()})