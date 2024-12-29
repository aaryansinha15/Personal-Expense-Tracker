def validate_file(input_value):
    try:
        value= float(input_value)
        if value<0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid value!! Please enter a positive value. ")
        return None
    