ciphertext = "wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}"

for shift in range(26):
    output = ""
    
    for char in ciphertext:
        if char.islower():
            base = ord('a')
            output += chr((ord(char) - base - shift) % 26 + base)
        elif char.isupper():
            base = ord('A')
            output += chr((ord(char) - base - shift) % 26 + base)
        else:
            output += char
          
    print(f"Shift {shift:02d}: {output}")
