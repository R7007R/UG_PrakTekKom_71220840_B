def add(np, nd):
    return f'{np} + {nd} = {np + nd}'

def substract(np, nd):
    return f'{np} - {nd} = {np + nd}'

def multiply(np, nd):
    return f'{np} * {nd} = {np * nd}'

def divide(np, nd):
    return f'{np} / {nd} = {np / nd}'

calculator = {
    'Add':add,
    'Substract':substract,
    'Multiply':multiply,
    'Divide':divide
}

print('select operation.')
for pilihan,option in enumerate(calculator,start=1):
    print(f'{pilihan}. {option}')

choice = list(calculator)[int(input('\nEnter choice(1/2/3/4): '))-1]

pil1 = float(input('\nEnter first number: '))
pil2 = float(input('enter second number: '))
print(calculator[choice](pil1,pil2))