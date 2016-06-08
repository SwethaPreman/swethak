def main():
    s=input("day")
    if((s=="monday") or (s=="tuesday") or (s=="wednesday") or (s=="thursday") or (s=="friday")):
          print("\ntrue")
    elif((s=="saturday") or (s=="sunday")):
        print("\nfalse")
    else:
        print("\nInvalid")
main()
