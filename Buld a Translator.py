def translate(phrase):
    translation=""
    for latter in phrase:
        if latter in "AEIOUaeiou":
            translation=translation+"g"
        else:translation=translation+latter
    return translation

print(translate(input("Enter a phrase")))



