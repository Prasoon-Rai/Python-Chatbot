import wolframalpha

# Heart of AI -
client = wolframalpha.Client('G37W7T-5VTVX57G6L')

def main_chat(query):
    if "sup" in query:
        print("Me good !")

while True:
    query = str(input('Question : '))
    res = client.query(query)
    output = next(res.results).text
    print(output)

    main_chat(output)
