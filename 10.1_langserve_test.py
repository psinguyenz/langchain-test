from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/chain/c/N4XyA")
res = chain.invoke({"language": "Vietnamese", "text": "Generative AI is a bigger opportunity than Internet"})

# act as a client using the langserve, either use this or the web interface in http://localhost:8000/chain/playground/
print(res)