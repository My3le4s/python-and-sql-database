data = {'color': 'red',
        'fruit': 'apple',
        'pet': 'dog',
        'car': 'van'
        }

iterator = iter(data)

while True:
    try:
        key = next(iterator)
        value = data[key]
        print(f'{key}: {value}')
    except StopIteration:
        break


keys = list(data.keys())
i = 0
while i < len(keys):
    key = keys[i]
    value = data[key]
print(key, +':', +value)
i += 1
