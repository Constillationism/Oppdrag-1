alder = int(input('Hvor gammel er du'))
if alder <13:
    print('Du er et barn')
elif alder >13 and alder <19:
    print('Du er en ungdom')
elif alder >19 and alder <59:
    print('Du er en voksen')
elif alder >60:
    print('Du er gammel')