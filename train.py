with open('data/input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("length of dataset in characters: ", len(text))
print(text[:1000])

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(f'Vocabulary size is: {vocab_size}')

stoi = {ch: i for i, ch in enumerate(text)}
print(stoi)