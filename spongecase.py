try:
    import pyperclip
except ImportError:
    pass

message = input('eNtEr yOuR MeSsAgE: ')

spongecaseMessage = ''

for i in range(len(message)):
    if i % 2 == 0:
        spongecaseMessage += message[i].lower()
    else:
        spongecaseMessage += message[i].upper()

try:
    pyperclip.copy(spongecaseMessage)
    print(spongecaseMessage)
    print('cOpIeD To cLiPbOaRd')
except:
    print(spongecaseMessage)
