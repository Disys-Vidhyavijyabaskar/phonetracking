class googlephonetracking():

    def __init__(self,s,p,e,m):

        self.__playsound=s
        self.__setpassword=p
        self.__linkwithelectronics=e
        self.__addmessage=m

    def display(self):

        self.__password="enter code" or "password" or "fingerprint"
        print("swipe to enter password")

        self.__sound=" play a sound"
        print("sound track")

        self.__message=" add a lockscreen message"
        print("hi i am xxx, call 9782125221")

        self.__electronics="link with tablet" or "smart band" or "GPS"
        print("your phone is not with you")

    def safety(self):

        self.setpassword="set a swipe lock" or "facelock" or "fingerprint" or"pattern"
        print("reconfirm password")


    def link(self):

        self.link="link with google accounts"
        print("link with gmail")

customer=googlephonetracking("playsound","set passwords","link with electronics","add a message")
customer.display()
customer.safety()
customer.link()

if ("password doesn't match"):
    raise TypeError("passwords doesn't match")

elif print("password saved successfully"):

    if ("passwords don't match"):
        raise TypeError("re-enter password")

    if("password wrong>3 times"):
        print("try after sometime")
        
