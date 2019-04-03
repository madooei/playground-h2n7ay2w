from isPalindrome import isPalindrome

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")
    send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
    send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
    send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
    send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
    send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
    send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
    send_msg("My personal Yoda, you are. 🙏", "_)_/LI")

def fail():
    print("TECHIO> success false")
    
def tests():
  try:
    assert isPalindrome("")
  except AssertionError as e:
    fail()
    send_msg("Oops! 🐞", e)
    send_msg("Hint 💡", "What is the smallest palindrome? 🤔")   
    
  try:
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
    success()
  
  except AssertionError as e:
    fail()
    send_msg("Oops! 🐞", e)
    send_msg("Hint 💡", "If the first and the last character of the input are not the same then ...? 🤔")
        
if __name__ == "__main__":
    tests()
