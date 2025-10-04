def format_name(full_name: str) -> str:
    fish = full_name.split(" ")
    ism, fam, och = fish
    return f"{ism} {fam} {och}"


print(format_name("Aliyev Vali G'aniyevich")) 
