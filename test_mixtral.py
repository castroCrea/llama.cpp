from llama_cpp import Llama

# Instanciate the model
mixtral_llama_model = Llama(model_path="./models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf")

def generate_text_from_prompt(user_prompt,
                             max_tokens = 100,
                             temperature = 0.3,
                             top_p = 0.1,
                             echo = True,
                             stop = ["Q", "\n"]):

   # Define the parameters
   model_output = mixtral_llama_model(
       user_prompt,
       max_tokens=max_tokens,
       temperature=temperature,
       top_p=top_p,
       echo=echo,
       stop=stop,
   )


   return model_output

my_prompt = "Q: What do you think about the inclusion policies in Tech companies?"


model_response = generate_text_from_prompt(my_prompt)


print('=========')
print(model_response)
print('=========')
print(model_response["choices"][0]["text"].strip())
print('=========')
