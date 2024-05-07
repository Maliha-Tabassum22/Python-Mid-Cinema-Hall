class Hall:
    def __init__(self, row, col, hallNo):
        self.__seats = {}
        self.__show_list = []
        self.__row = row
        self.__col = col
        self.__hallNo = hallNo
        self.__seat = [[0 for i in range(col)] for j in range(row)]

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = [
            [0 for _ in range(self.__col)] for _ in range(self.__row)]

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.__seats:
            show_seats = self.__seats[show_id]
            for row, col in seats_to_book:
                if 0 <= row < self.__row and 0 <= col < self.__col:  
                    if show_seats[row][col] == 0:  
                        show_seats[row][col] = 1
                    else:
                        print("Seat Is Already Booked!")
                else:
                    print("Invalid Seat!")
        else:
            print("Show Not Found!")

    def view_show_list(self):
        for show in self.__show_list:
            print(show)

    def view_available_seats(self, show_id):
        if show_id in [show[0] for show in self.__show_list]: 
            show_seats = self.__seats[show_id]
            for row in show_seats:
                print(" ".join(map(str, row)))
        else:
            print("Show Not Found!")

    def get_show_ids(self):  
        return [show[0] for show in self.__show_list]

    def get_hallNo(self):
        return self.__hallNo


class StarCinema(Hall):  
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    def hall_by_no(self, hallNo):
        for hall in self.hall_list:
            if hall.get_hallNo() == hallNo:
                return hall
        return None


hallA = Hall(row=5, col=5, hallNo=1)
hallB = Hall(row=5, col=5, hallNo=2)

hallA.entry_show(id='101', movie_name='Superman', time='8:00 PM')
hallA.entry_show(id='102', movie_name='Spiderman', time='11:00 PM')

hallB.entry_show(id='103', movie_name='Batman', time='2:00 PM')
hallB.entry_show(id='104', movie_name='Parman', time='6:00 PM')

cinema = StarCinema()
cinema.entry_hall(hallA)
cinema.entry_hall(hallB)





while True:
    print("Menu : ")
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")

    opt = input("Enter Your Choice : ")

    if opt == '1':
        for hall in cinema.hall_list:
            print(f"Hall No : {hall.get_hallNo()}")
            hall.view_show_list()
        print()

    elif opt == '2':
        show_id = input("Enter Show ID : ").strip()  
        hall = None
        for h in cinema.hall_list:
            if h.get_show_ids() and show_id in h.get_show_ids():
                hall = h
                break
        if hall:
            hall.view_available_seats(show_id)
        else:
            print("Show Not Found!")

    elif opt == '3':
        show_id = input("Enter Show ID : ").strip()  
        cnt = int(input("Enter The Number Of Seats To Book : "))
        booking_seat = []

        for _ in range(cnt):
            seat_input = input(f"Enter Seat {_ + 1} (e.g., 1-2) : ")
            seat = tuple(map(int, seat_input.split('-')))
            booking_seat.append(seat)
        
        hall = None
        for h in cinema.hall_list:
            if h.get_show_ids() and show_id in h.get_show_ids():
                hall = h
                break
        if hall:
            hall.book_seats(show_id, booking_seat)
            print("Booking Successfully!!!")
        else:
            print("Show Not Found!")

    elif opt == '4':
        break

    else:
        print("Please Choose A Valid Option.")
