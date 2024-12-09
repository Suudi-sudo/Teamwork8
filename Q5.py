class Member:  
    def __init__(self, name):  
        self.name = name  

    def __repr__(self):  
        return self.name  


class Team:  
    def __init__(self, name):  
        self.name = name  
        self.team_members = set()  # Use a set to prevent duplicates  

    def add_member(self, member):  
        if member in self.team_members:  
            print(f"{member.name} is already a member of team {self.name}.")  
        else:  
            self.team_members.add(member)  
            print(f"Added {member.name} to team {self.name}.")  

    def __repr__(self):  
        return self.name  


class Project:  
    def __init__(self, name):  
        self.name = name  
        self.teams = []  

    def assign_team(self, team):  
        if team not in self.teams:  
            self.teams.append(team)  
            print(f"Assigned team {team.name} to project {self.name}.")  
        else:  
            print(f"Team {team.name} is already assigned to project {self.name}.")  

    def display_members(self):  
        unique_members = set()  # To keep track of unique members  
        for team in self.teams:  
            unique_members.update(team.team_members)  
        print(f"Members in project {self.name}: {', '.join(str(member) for member in unique_members)}")  

    def total_unique_members(self):  
        unique_members = set()  # To keep track of unique members  
        for team in self.teams:  
            unique_members.update(team.team_members)  
        return len(unique_members)  




# Creating  members  
maxwell = Member("maxwell")  
peter = Member("iris")  
iris = Member("peter")  

  
team_a = Team("Team A")  
team_b = Team("Team B")  


team_a.add_member(iris)  
team_a.add_member(peter)  
team_b.add_member(peter)  

team_b.add_member(iris)  

  
team_a.add_member(maxwell)  
 

project_1 = Project("Project 1")  
project_2 = Project("Project 2")  


project_1.assign_team(team_a)  
project_2.assign_team(team_b)  


project_1.display_members()  
 
project_2.display_members()  


total_unique = project_1.total_unique_members() + project_2.total_unique_members()  
print(f"Total unique members across all projects: {total_unique}")