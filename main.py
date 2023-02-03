letters = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
encoder = {i: a for i, a in enumerate(letters.split(" "))}
decoder = {a: i for i, a in enumerate(reversed(letters.split(" ")))}

input_text = "GSVUOZTRHHZBDVZIVXIZAB"
decode_text = ""
for letter in input_text.lower():
    decode_text = decode_text + encoder[decoder[letter]]

print(decode_text)