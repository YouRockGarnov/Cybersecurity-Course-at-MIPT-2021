with open("source", "rb") as inp:
    data = inp.read()
    data = data.replace(b'\x75\x11', b'\x90\x90')

    with open("cracked", "wb") as out:
        out.write(data)
