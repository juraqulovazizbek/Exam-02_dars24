find_pattern = lambda items, pat, t: list(filter(
    lambda n: (t=="starts" and n.lower().startswith(pat.lower())) or
              (t=="ends" and n.lower().endswith(pat.lower())) or
              (t=="contains" and pat.lower() in n.lower()),
    items
))
print(find_pattern(["Ali", "Alisher", "Vali"], "a", "starts"))
