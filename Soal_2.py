def funPalindrome(subject):
    subject = subject.lower()
    kebalikanpalindrome = 'Yes' if subject == subject [::-1] else 'No'
    return f'{kebalikanpalindrome}\nJika Dibalik: {subject[::-1]}'

masukankata = input('Masukan Kata: ')
print(funPalindrome(masukankata))

