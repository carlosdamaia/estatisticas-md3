class Jogador:
    def __init__(self, id, nick, total_kills, total_assists, total_deaths, total_stars, med_hs, total_score, total_matches, winrate):
        self._id = id
        self._nick = nick
        self._total_kills = total_kills
        self._total_assists = total_assists
        self._total_deaths = total_deaths
        self._total_stars = total_stars
        self._med_hs = med_hs
        self._total_score = total_score
        self._total_matches = total_matches
        self._winrate = winrate

    #getter id
    def get_id_jogador(self):
        return self._id

    # Getter para nick
    def get_nick(self):
        return self._nick

    # Setter para nick
    def set_nick(self, novo_nick):
        self._nick = novo_nick

    # Getter para total_kills
    def get_total_kills(self):
        return self._total_kills

    # Setter para total_kills
    def set_total_kills(self, novo_total_kills):
        self._total_kills = novo_total_kills

    # Getter para total_assists
    def get_total_assists(self):
        return self._total_assists

    # Setter para total_assists
    def set_total_assists(self, novo_total_assists):
        self._total_assists = novo_total_assists

    # Getter para total_deaths
    def get_total_deaths(self):
        return self._total_deaths

    # Setter para total_deaths
    def set_total_deaths(self, novo_total_deaths):
        self._total_deaths = novo_total_deaths

    # Getter para total_stars
    def get_total_stars(self):
        return self._total_stars

    # Setter para total_stars
    def set_total_stars(self, novo_total_stars):
        self._total_stars = novo_total_stars

    # Getter para med_hs
    def get_med_hs(self):
        return self._med_hs

    # Setter para med_hs
    def set_med_hs(self, novo_med_hs):
        self._med_hs = novo_med_hs

    # Getter para total_score
    def get_total_score(self):
        return self._total_score

    # Setter para total_score
    def set_total_score(self, novo_total_score):
        self._total_score = novo_total_score

    # Getter para total_matches
    def get_total_matches(self):
        return self._total_matches

    # Setter para total_matches
    def set_total_matches(self, novo_total_matches):
        self._total_matches = novo_total_matches

    # Getter para winrate
    def get_winrate(self):
        return self._winrate

    # Setter para winrate
    def set_winrate(self, novo_winrate):
        self._winrate = novo_winrate