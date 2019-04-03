from isPalindrome import isPalindrome

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def tests():
  try:
    assert exp(2, 3)==2**3
    assert exp(1, 5)==1
    assert exp(9, 0)==1
    assert exp(2, 2)==2**2
    assert exp(5, 6)==5**6
    success()
    send_msg("Kudos 🌟", "Nice work 😀")
  
  except AssertionError as e:
    fail()
    send_msg("Oops! 🐞", e)
        
if __name__ == "__main__":
    tests()
