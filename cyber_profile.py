from colorama import Fore, Style, init

init()

print(Fore.GREEN + """
      CCCCC  OOOOO  OOOOO  K   KK  IIIII  EEEEE      BBBB
      C      O   O  O   O  K  K      I    E          B   B
      C      O   O  O   O  K K       I    EEEE  ---  BBBB
      C      O   O  O   O  K  K      I    E          B   B
      CCCCC  OOOOO  OOOOO  K   KK  IIIII  EEEEE      BBBB
      """)

print(Fore.RED + "=" * 80)
print("                CYBER PROFILE GENERATOR")
print("=" * 80)

name = input(Fore.CYAN + "\nPlease Enter your Codename: ")
age = input("Your Age: ")
goal = input("Cyber Goal: ")
country = input("Country: ")


print(Fore.GREEN + "\nGenerating Profile...\n")

print(Fore.YELLOW + "=" * 80)
print(Fore.BLUE + "Codename: ", name)
print(Fore.LIGHTRED_EX + "Age: ", age)
print(Fore.LIGHTMAGENTA_EX + "Mission: ", goal)
print(Fore.LIGHTGREEN_EX + "Country: ", country)
print(Fore.YELLOW + "=" * 80)

print(Fore.GREEN + "\nACCESS GRANTED")
print(Style.RESET_ALL)