from isPalindrome import isPalindrome

def run():
  assert isPalindrome("ali")==False, "ali is not palindrome"
  assert isPalindrome("bob"), "bob is palindrom"
  assert isPalindrome("hannah"), "hannah is palindrome"
  assert isPalindrome("ada"), "ada is plaindrome"
  assert isPalindrome("anna"), "anna is palindrome"
  assert isPalindrome("nitin"), "nitin is palindrome"
  assert isPalindrome("otto"), "otto is palindrome"
  assert isPalindrome("madam"), "madam is palindrome"
  assert isPalindrome("racecar"), "racecar is palindrome"
  assert isPalindrome("xerox")==False, "xerox is not palindrome"


if __name__ == "__main__":
    run()
