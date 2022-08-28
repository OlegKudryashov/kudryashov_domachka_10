class Candidate:
    def __init__(self, pk, name, picture, skills, position):
        self.pk = pk
        self.name = name
        self.picture = picture
        self.skills = skills
        self.position = position

    def __repr__(self):
        return f'{self.name} \n {self.position} \n {self.skills}'
