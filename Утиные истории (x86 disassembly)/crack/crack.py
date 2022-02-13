with open("source", "rb") as inp:
    data = inp.read()
    data = data.replace(b'\x75\x11', b'\x74\x11')

    with open("cracked", "wb") as out:
        out.write(data)
