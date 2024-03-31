def reverse_string(input_str):
    reversed_str = ""
    for char in input_str[::-1]:
        reversed_str += char
    return reversed_str

# Test the function
input_str = input("Enter a String : ")
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)
