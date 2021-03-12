import TROLLCODE

while True:
    text = input(' TROLLCODE >')
    result, error = basic.run(text)

    if error: print(error.as_string())
    else: print(result)

    