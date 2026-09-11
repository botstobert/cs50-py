def convert(s):
    s = s.replace(":)" , "🙂")
    s = s.replace(":(" , "🙁")

    return s


def main():
    text = input()
    print(convert(text))

if __name__ == "__main__":
    main()
