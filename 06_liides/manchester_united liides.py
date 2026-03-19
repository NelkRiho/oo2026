from abc import ABC, abstractmethod

#  LIIDES 1: Footballer  (kõik mängijad peavad täitma)
class Footballer(ABC):

    @abstractmethod
    def get_player_info(self) -> str:
        pass

    @abstractmethod
    def get_position(self) -> str:
        pass

    @abstractmethod
    def play(self):
        pass

#  LIIDES 2: Leader  (ainult kaptenile)
class Leader(ABC):

    @abstractmethod
    def motivate_team(self):
        pass

    @abstractmethod
    def get_captaincy_badge(self) -> str:
        pass

#  KLASS: Player, kasutab Footballer
class Player(Footballer):

    def __init__(self, name: str, number: int, position: str):
        self.name     = name
        self.number   = number
        self.position = position

    def get_player_info(self) -> str:
        return f"#{self.number} {self.name}"

    def get_position(self) -> str:
        return self.position

    def play(self):
        print(f"{self.get_player_info()} ({self.position}) mängib ja kontrollib palli.")

#  KLASS: Captain, kasutab Player'i + Leader
class Captain(Player, Leader):

    def __init__(self, name: str, number: int, position: str, captain_since: str):
        super().__init__(name, number, position)
        self.captain_since = captain_since

    # Footballer.play() ülekirjutamine
    def play(self):
        print(f"{self.get_player_info()} (C) [{self.position}] juhib mängu ja annab käsklusi.")

    # Leader meetodid
    def motivate_team(self):
        print(f"  C {self.name}: \"Tulge, poisid! Manchester United ei anna alla!\"")

    def get_captaincy_badge(self) -> str:
        return f"{self.name} on kapten (C) alates {self.captain_since}. aastast."

#  KLASS: GoalKeeper, pärib Player'i, lisab oma meetodi
class GoalKeeper(Player):

    def __init__(self, name: str, number: int, clean_sheets: int):
        super().__init__(name, number, "Väravavaht")
        self.clean_sheets = clean_sheets

    # Footballer.play() ülekirjutamine
    def play(self):
        print(f"{self.get_player_info()} [Väravavaht] hoiab väravat. "
              f"Puhaste mängude arv: {self.clean_sheets}.")

 # GoalKeeper meetod
    def make_save(self):
        self.clean_sheets += 1
        print(f"   {self.name} tõrjub löögi! Puhaste mängude arv nüüd: {self.clean_sheets}.")

#  NÄITPROGRAMM
if __name__ == "__main__":

    print("Manchester United Koosseis \n")

    # Objektide loomine
    keeper  = GoalKeeper("Senne Lammens",    31, 8)
    captain = Captain("Bruno Fernandes",    8, "Ründav poolkaitsja", "2020")
    player1 = Player("Benjamin Sesko",    30, "Ründaja")
    player2 = Player("Kobbie Mainoo",      37, "Poolkaitsja")

    # 1. Mängijad (footballers)
    print("Mängijad väljakul")
    squad: list[Footballer] = [keeper, captain, player1, player2]

    for f in squad:
        f.play()   # iga klass käitub omamoodi!

    # 2. Leader liides – ainult kapten
    print("\n Kapteni erivõimed (Leader)")
    print(captain.get_captaincy_badge())
    captain.motivate_team()

    # 3. GoalKeeper
    print("\nVäravavaht teeb tõrje!")
    keeper.make_save()

# tüübikontroll – kes on mis tüüpi mängija?
    print("\n Tüübikontroll")
    for f in squad:
        if isinstance(f, Captain):
            print(f"{f.get_player_info()} → ON kapten  (Leader + Footballer)")
        elif isinstance(f, GoalKeeper):
            print(f"{f.get_player_info()} → ON väravavaht (GoalKeeper + Footballer)")
        else:
            print(f"{f.get_player_info()} → tavaline väljakumängija (Footballer)")

    print("\nLõpp")
