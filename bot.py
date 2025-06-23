def generate_konten(trigger):
    if trigger == "#kocak":
        return "Video absurd lagi ngocok tawa 😆"
    elif trigger == "#edukasi":
        return "Konten edukasi dibungkus lucu"
    else:
        return "Trigger tidak dikenali"

# Contoh pakai
print(generate_konten("#kocak"))
