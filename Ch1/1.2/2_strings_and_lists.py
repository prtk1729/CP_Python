

if __name__ == "__main__":

    # NOTE: string is immutable
    # Sc: But How to modify a string
        # 1. First get each char of a str to list
        # 2. Then, modify
        # 3. Then, convert list to string


    name = "PrateekPani"

    # using `name`, make another string s.t
    # name2 is "PrateekQani" NOTE: Qani
    name2 = list(name) # 1st listify string i.e each char a le
    # modify list element
    name2[7] = 'Q'
    name2 = ''.join(name2)
    print(name, name2)
    print()

    # Summary: string-copy => listOfChars => Modify => join-method