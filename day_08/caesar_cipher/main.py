import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            shifted_position = (alphabet.index(char) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            break
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            pass
        else:
            break

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    while True:
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == "no" or restart == "yes":
            break
    if restart == "no":
        should_continue = False
        print("Goodbye")
