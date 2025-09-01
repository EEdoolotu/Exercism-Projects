my_list = [5, 10, 15, 20, 25]

def bin_search(list):
    num = int(input("Enter a number "))
    if num in list:
        return True
    else: 
        return False

result = bin_search(my_list)
print(result)