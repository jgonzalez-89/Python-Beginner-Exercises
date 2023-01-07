def sing():

    song = ""
    for i in range(12):
        if i < 4:
            song += "let it be, "
        elif i == 4:
            song += "whisper words of wisdom, "
        elif i < 10:
            song += "let it be, "
        elif i == 10:
            song += "there will be an answer, "
        elif i > 10:
            song += "let it be"
    return song

print(sing())