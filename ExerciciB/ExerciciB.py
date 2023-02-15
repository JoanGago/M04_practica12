import json

# Creem la funcio que mostra i guarda un arxiu extern JSON
def exercicijsonB():
    datas = """
    {
    "book": [
            {
                "title": "Harry Potter",
                "cover": "dura",
                "year": 2007,
                "pages": 223
            },
            {
                "title": "La pedrada",
                "cover": "tova",
                "year": 2011,
                "pages": 654
            },
            {
                "title": "El camí",
                "cover": "tova",
                "year": 1909,
                "pages": 789
            },
            {
                "title": "El gegant Pere",
                "cover": "dura",
                "year": 1978,
                "pages": 121
            }
        ]
    }
"""
    with open("jsonB", 'w') as file:
        json.dump(datas, file)

# Creem la funció que llegeix el codi i el passa per pantalla
def llegirjson():

    with open("jsonB", 'r') as file:
        result = json.load(file)
        print(result)




