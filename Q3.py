# qUESTION 3
class Student:
    def __init__(self, name):
        self.name = name
        self.clubs = []  

    def join_club(self, club):
        if club not in self.clubs:
            self.clubs.append(club)
            club.add_member(self)  
    def list_clubs(self):
        return [club.name for club in self.clubs]


class Club:
    def __init__(self, name):
        self.name = name
        self.members = []  

    def add_member(self, student):
        if student not in self.members:
            self.members.append(student)

    def list_members(self):
        return [student.name for student in self.members]



if __name__ == "__main__":
    
    alice = Student("suudi")
    bob = Student("elvis")
    
    
    chess_club = Club("Chess Club")
    science_club = Club("Science Club")

    alice.join_club(chess_club)
    bob.join_club(chess_club)
    alice.join_club(science_club)

   
    print(f"Members of {chess_club.name}: {chess_club.list_members()}")

    
    print(f"Clubs suudi is a member of: {alice.list_clubs()}")

    
    print(f"Clubs elvis is a member of: {bob.list_clubs()}")