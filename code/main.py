from datetime import date

class Hotel:

    def __init__(self) :
        self.rooms = {}
        self.available_rooms ={'single':[101,102,103], 'double':[201,202,203],'luxury':[301,302,303],'suite':[401,402,403]}
        self.roomprice={1:6000,2:8000,3:12000,4:16000}

    def check_in(self, name, address, phone):
        roomtype = int(input('Room types:\n1.single \n2.double\n3.Luxury\n4.Suite\nSelect a room type'))
        if roomtype==1:
            if self.available_rooms['single']:
             roomno=self.available_rooms['single'].pop(0)
            else:
              print('Sorry, all single rooms are full')
            return
        elif roomtype==2:
            if self.available_rooms['double']:
             roomno=self.available_rooms['double'].pop(0)
            else:
               print('Sorry, all double rooms are full')
               return
        elif roomtype==3:
            if self.available_rooms['luxury']:
                roomno=self.available_rooms['luxury'].pop(0)
            else:
              print('Sorry, all luxury rooms are full')
              return
        elif roomtype==4:
             if self.available_rooms['suite']:
                 roomno=self.available_rooms['suite'].pop(0)
             else:
                   print('Sorry, all Suite rooms are full')
                   return
        else:
            print("Please enter a valid room type")
        d,m,y=map(int,input('enter the date, month and year in which you have checked in').split())
        check_in = date(y,m,d)
        self.rooms[roomno] =  {
            'name': name,
            'address': address,
            'phone':phone,
            'check_in_date': check_in,
            'room_type': roomtype,
            'roomservice':0
        }
        print (f"Checked in {name},{address} to room: {roomno} on {check_in}")



    def room_service(self,roomno):
        if roomno in self.rooms:
            print("******Room service menu******")
            print("1Ordering food and beverages: Rs 100  2.Plumber: Rs 70 3:Electrician: Rs 50 4.Massage: Rs 40  5.Special Requests: Rs 250 6.Exit")
            while 1:
                c=int(input("Select your choice"))
                if c==1:
                    q=int(input("Enter the quantity"))
                    self.rooms[roomno]['roomservice']+=100*q
                elif c==2:
                     q=int(input("Enter the quantity"))
                     self.rooms[roomno]['roomservice']+=70*q
                elif c==3:
                     q=int(input("Enter the quantity"))
                     self.rooms[roomno]['roomservice']+=50*q
                elif c==4:
                     q=int(input("Enter the quantity"))
                     self.rooms[roomno]['roomservice']+=40*q
                elif c==5:
                     q=int(input("Enter the quantity"))
                     self.rooms[roomno]['roomservice']+=250*q
                elif c==6:
                    break;
                else:
                    print("Invalid Number")
            print("Room service Rs:",self.rooms[roomno]['roomservice'],"\n")
        else:
            print('Invalid room number')
                                

    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at the moment")
        else:
            print("Occupied rooms: ")
            print("------------------------")
            print('Room no Name Phone')
            print("------------------------")
            for  roomnumber,details in self.rooms.items():
                print(roomnumber,'\t',details['name'],'\t',details['phone'])

    def check_out(self, roomnumber):
        if roomnumber in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[roomnumber]['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype = self.rooms[roomnumber]['room_type']
            if roomtype==1:
                self.available_rooms['single'].append(roomnumber)
            elif roomtype==2:
                self.available_rooms['double'].append(roomnumber)
            elif roomtype==3:
                self.available_rooms['luxury'].append(roomnumber)
            elif roomtype==4:
                self.available_rooms['suite'].append(roomnumber)
            print('-------------------')
            print('Pintu Dhaba Bill')
            print(f"Name{self.rooms[roomnumber]['name']}\nAddress:{self.rooms[roomnumber]['address']}")
            print(f"Phone:{self.rooms[roomnumber]['phone']}")
            print(f'Room Number:{roomnumber}')
            print(f"Check in date:{check_in_date.strftime('%d %B %Y')}")
            print(f'Check out date:{check_out_date.strftime("%d %B %Y")}')
            print(f'No.of Days :{duration}\tPrice per day:Rs {self.roomprice[roomtype]}')
            roombill=self.roomprice[roomtype]*duration
            roomservice=self.rooms[roomnumber]['roomservice']
            print('Room bill: Rs',roombill)
            print('Room service: Rs', roomservice)
            print('Total bill',roombill + roomservice)
            del self.rooms[roomnumber]
        else:
            print(f"Room[roomnumber] is vacant")

    def start_app(self):
        while True:
            print("---------------------------")
            print("Welcome to Pintu's Dhaaba")
            print("1: Check In")
            print("2: Ask for room service")
            print("3: Check which rooms are taken")
            print("4: Check Out")
            print("5: Exit")
            choice = input("Enter your Choice(1-5)")
            if choice == '1':
                name =input("Namaste! Please enter your name")
                address =input("Please enter your address")
                phone = int(input("Enter your contact number"))
                self.check_in(name, address, phone)
            elif choice == '2':
                roomno = input("Please enter your  number. Service will be sent over shortly.")
                self.room_service(roomno)
            elif choice == '3':
                self.display_occupied()
            elif choice == '4':
                 roomnumber = int(input("Please enter your room number"))
            elif choice == '5':
                break
            else:
                print("You have entered a wrong number. Please try to enter your choice again")

h = Hotel()
h.start_app()
