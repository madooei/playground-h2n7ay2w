from count_paths import count_paths

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

def success():
    print("TECHIO> success true")

def fail():
    print("TECHIO> success false")
    
def tests():
  try:
    count = count_paths(1, 1)
    assert count == 1, "Running count_path(1,1)... Expected 1, got {}".format(count)
    count = count_paths(3, 1)
    assert count == 1, "Running count_path(3,1)... Expected 1, got {}".format(count)
    count = count_paths(1, 4)
    assert count == 1, "Running count_path(1,4)... Expected 1, got {}".format(count)
    count = count_paths(3, 4)
    assert count == 10, "Running count_path(3,4)... Expected 10, got {}".format(count)
    count = count_paths(3, 3)
    assert count == 6, "Running count_path(3,3)... Expected 6, got {}".format(count)
    count = count_paths(7, 8)
    assert count == 1716, "Running count_path(7,8)... Expected 1716, got {}".format(count)
    success()
  
  except AssertionError as e:
    fail()
    send_msg("Oops! 🐞", e)
        
if __name__ == "__main__":
    tests()
