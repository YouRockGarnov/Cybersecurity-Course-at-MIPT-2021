with open("source", "rb") as inp:
    data = inp.read()
    data = data.replace(b'\xe0\xd7', b'\xe0\xc7')

    with open("cracked", "wb") as out:
        out.write(data)
