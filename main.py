import wolframalpha

# Heart of AI -
client = wolframalpha.Client('G37W7T-5VTVX57G6L')

while True:
    query = str(input('Question : '))
    res = client.query(query)
    output = next(res.results).text
    print(output)
