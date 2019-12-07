if __name__ == "__main__":
    
    def valid_password(password):
        password_string = str(password)

        def sequential_numbers(password_string):

            previous_letter = ''
            sequential_letter_count = 1
            current_sequential_letter_count = 1
            for letter in password_string:
                if previous_letter == letter:
                    current_sequential_letter_count += 1
                else:
                    if sequential_letter_count != 2:
                        sequential_letter_count = current_sequential_letter_count
                    current_sequential_letter_count = 1
                previous_letter = letter
            
            return sequential_letter_count == 2 or current_sequential_letter_count == 2
        
        def ever_increasing(password_string):
            previous_letter = '0'
            for letter in password_string:
                if int(previous_letter) > int(letter):
                    return False
                previous_letter = letter
            return True
        
        return sequential_numbers(password_string) and ever_increasing(password_string)
    
    print(valid_password(112233))
    print(valid_password(123444))
    print(valid_password(111122))
    valid_passwords = 0
    for number in range(197487, 673251):
        if valid_password(number):
            valid_passwords += 1
    
    print(valid_passwords)