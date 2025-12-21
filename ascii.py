from colorama import Fore, Style, init
import os
import time

init(autoreset=True)


banner = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * *****        ***                     ***  ***   ****  ****  *   * *****  ***  *****  ***  ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *        * ***                   *   *   *       *     * *   * *     *         * *   * *   * ",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *         * * *       *****       *   *   *       *   **  ***** ****  ****      *  ***  ***** ",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *          * * *              ***  *   *   *   ***       *     *     * *   *     * *   *     * ",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****        ***  *****        ***   ***  ***** ***** ****      * ****   ***      *  ***      * "
]


small = [
    "      *               *        * *          *            *   *       *                      *                       *                                       ",
    "  *** *      ****     *  ****  *  * ****    *     *          ****    *                ***   **** ****  *            *                           *  *        ",
    " **** ****  *      ****  *  * ****  **** *  ****         *   *   *   *   ** ** ***** *   *  *  * *  *  ****  ****  ***  *  *  *   * *   *  * *  *  *  ****  ",
    "*   * *   * *      *  *  * *   *     * *    *  *  *   *  *   ****    *   * * * *   * *   *  **** ****  *     *****  *   *  *   * *  * * *   *    *     *    ",
    " ***  ****   ****  ****  ***   *    ****    *  *  *   ****   *   *   *   *   * *   *  ***   *       *  *     ****   **  ****    *   *   *  * *  *     ****  "
]


def ascii_index(ch):
    c = ord(ch)
    if ch.isupper():
        return (c - 65) * 6
    if ch == ' ':
        return 26 * 6
    if ch == '@':
        return 27 * 6
    if ch == '_':
        return 28 * 6
    if ch == '-':
        return 29 * 6
    if ch == '.':
        return 30 * 6
    if ch.isdigit():
        return (c - 17) * 6
    return None

def ascii_index_small(ch):
    if ch.islower():
        return (ord(ch) - 97) * 6
    return None


def show_ascii(text, color=Fore.CYAN):
    idx = [ascii_index(ch) for ch in text if ascii_index(ch) is not None]
    for row in banner:
        print(color + "".join(row[p:p+6] for p in idx))

def show_ascii_small(text, color=Fore.CYAN):
    idx = [ascii_index_small(ch) for ch in text if ascii_index_small(ch) is not None]
    for row in small:
        print(color + "".join(row[p:p+6] for p in idx))


def module_one_char():
    os.system("cls")
    print(Fore.YELLOW + "\n SINGLE CHARACTER ASCII (A-Z)\n")
    key = input("Enter uppercase letter: ")
    if len(key) != 1 or not key.isupper():
        print(Fore.RED + "Enter ONE uppercase letter!")
        return
    show_ascii(key, Fore.GREEN)

def module_word():
    os.system("cls")
    print(Fore.YELLOW + "\n WORD ASCII (A-Z, max 15)\n")
    txt = input("Enter uppercase word: ")
    if not txt.isupper() or len(txt) > 15:
        print(Fore.RED + "Only uppercase A-Z allowed!")
        return
    show_ascii(txt, Fore.MAGENTA)

def module_range():
    os.system("cls")
    print(Fore.YELLOW + "\n RANGE A-Z (Example: A-D)\n")
    rng = input("Enter A-D: ")

    if len(rng) != 3 or rng[1] != "-" or not rng[0].isupper() or not rng[2].isupper():
        print(Fore.RED + "Format must be A-D only.")
        return

    start, end = rng[0], rng[2]
    if ord(start) > ord(end):
        print(Fore.RED + "Start must be smaller.")
        return

    output = "".join(chr(c) for c in range(ord(start), ord(end) + 1))
    show_ascii(output, Fore.BLUE)

def module_num():
    os.system("cls")
    print(Fore.YELLOW + "\n ONLY NUMBERS (0-9)\n")
    txt = input("Enter digits: ")
    if not txt.isdigit():
        print(Fore.RED + "Numbers only!")
        return
    show_ascii(txt, Fore.RED)

def module_name_tag():
    os.system("cls")
    print(Fore.YELLOW + "\n NAME TAG (A-Z only)\n")
    txt = input("Enter name (max 12 chars): ").upper()

    if len(txt) == 0 or len(txt) > 12 or not all(ch.isalpha() or ch == " " for ch in txt):
        print(Fore.RED + "Invalid input.")
        return

    width = len(txt) * 6
    border = "*" * width

    print(Fore.WHITE + border)
    show_ascii(txt, Fore.CYAN)
    print(Fore.WHITE + border)

def module_reverse_text():
    os.system("cls")
    print(Fore.YELLOW + "\n REVERSE TEXT (A-Z only)\n")
    txt = input("Enter text: ").upper()

    print("\nOriginal:\n")
    show_ascii(txt)
    print("\nReversed:\n")
    show_ascii(txt[::-1])


def module_one_char_small():
    os.system("cls")
    print(Fore.YELLOW + "\n SMALL CHARACTER ASCII (a-z)\n")
    key = input("Enter lowercase letter: ")
    if len(key) != 1 or not key.islower():
        print(Fore.RED + "Enter ONE lowercase letter!")
        return
    show_ascii_small(key, Fore.GREEN)

def module_word_small():
    os.system("cls")
    print(Fore.YELLOW + "\n SMALL WORD ASCII (a-z, max 15)\n")
    txt = input("Enter lowercase word: ")
    if not txt.islower() or len(txt) > 15:
        print(Fore.RED + "Only lowercase a-z allowed!")
        return
    show_ascii_small(txt, Fore.MAGENTA)


def main_menu():
    while True:
        os.system("cls")
        print(Fore.CYAN + "\n--------------------------")
        print(Fore.YELLOW+"      ASCII ART MAKER")
        print(Fore.CYAN + "--------------------------\n")

        print("1. Single Character (A-Z)")
        print("2. Word (A-Z)")
        print("3. Alphabet Range (A-D)")
        print("4. Only Numbers")
        print("5. Name Tag")
        print("6. Reverse Text")
        # print("--- lowercase (a-z) ---")
        print("7. Small Single Character (a-z)")
        print("8. Small Word (a-z)")
        print("9. Exit\n")

        choice = input("Enter choice: ")

        if choice == "1": module_one_char()
        elif choice == "2": module_word()
        elif choice == "3": module_range()
        elif choice == "4": module_num()
        elif choice == "5": module_name_tag()
        elif choice == "6": module_reverse_text()
        elif choice == "7": module_one_char_small()
        elif choice == "8": module_word_small()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice!")

        input("\nPress Enter to continue...")

main_menu()
