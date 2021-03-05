class Atm(object):
    atmnum1 = input('Enter ATM number:- ')
    pinnum1 = input('Enter your pin number:- ')
    def __init__(self, atmnum, pinnum):
        self.atmnum = atmnum
        self.pinnum = pinnum
    def Cashwithdrawl(self):
        input('Enter amount to enter:- ')
    def BalanceEnquiry(self):
        print('You have 300000 amount in your account')
ATM = Atm('atmnum1', 'pinnum1')
print(ATM.BalanceEnquiry())