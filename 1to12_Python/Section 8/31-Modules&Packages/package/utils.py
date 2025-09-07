def get_input(prompt:str, type_of_num:str):
    inp = input(prompt)
    match type_of_num:
        case 'int':
            return int(inp)
        case 'float':
            return float(inp)
        case _:
            return inp