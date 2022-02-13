with open("antideb", "rb") as inp:
    data = inp.read()
    data = data.replace(b'\x75\x14', b'\x74\x14')

    with open("antideb_patched", "wb") as out:
        out.write(data)
