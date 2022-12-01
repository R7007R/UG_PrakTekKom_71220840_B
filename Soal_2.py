def funPalindrome(s):
    s = s.lower()
    kebalikanpalindrome = 'Yes' if s == s [::-1] else 'No'
    return f'{kebalikanpalindrome}\nJika Dibalik: {s[::-1]}'

masukankata = input('Masukan Kata: ')
print(funPalindrome(masukankata))

