class JogadorTotalStats:
    def __init__(self, id, nick, total_kills, total_assists, total_deaths, total_stars, total_hs, total_score, total_matches, winrate):
        self._id = id
        self._nick = nick
        self._total_kills = total_kills
        self._total_assists = total_assists
        self._total_deaths = total_deaths
        self._total_stars = total_stars
        self._total_hs = total_hs
        self._total_score = total_score
        self._total_matches = total_matches
        self._winrate = winrate

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def nick(self):
        return self._nick

    @property
    def total_kills(self):
        return self._total_kills

    @property
    def total_assists(self):
        return self._total_assists

    @property
    def total_deaths(self):
        return self._total_deaths

    @property
    def total_stars(self):
        return self._total_stars

    @property
    def total_hs(self):
        return self._total_hs

    @property
    def total_score(self):
        return self._total_score

    @property
    def total_matches(self):
        return self._total_matches

    @property
    def winrate(self):
        return self._winrate

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

    @nick.setter
    def nick(self, value):
        self._nick = value

    @total_kills.setter
    def total_kills(self, value):
        self._total_kills = value

    @total_assists.setter
    def total_assists(self, value):
        self._total_assists = value

    @total_deaths.setter
    def total_deaths(self, value):
        self._total_deaths = value

    @total_stars.setter
    def total_stars(self, value):
        self._total_stars = value

    @total_hs.setter
    def total_hs(self, value):
        self._total_hs = value

    @total_score.setter
    def total_score(self, value):
        self._total_score = value

    @total_matches.setter
    def total_matches(self, value):
        self._total_matches = value

    @winrate.setter
    def winrate(self, value):
        self._winrate = value

class JogadorStats:
    def __init__(self, id, kills, assists, deaths, stars, hs, score, kda, time, jogador_total_stats_id, partida_id, partida_md3_id):
        self._id = id
        self._kills = kills
        self._assists = assists
        self._deaths = deaths
        self._stars = stars
        self._hs = hs
        self._score = score
        self._kda = kda
        self._time = time
        self._jogador_total_stats_id = jogador_total_stats_id
        self._partida_id = partida_id
        self._partida_md3_id = partida_md3_id

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def kills(self):
        return self._kills

    @property
    def assists(self):
        return self._assists

    @property
    def deaths(self):
        return self._deaths

    @property
    def stars(self):
        return self._stars

    @property
    def hs(self):
        return self._hs

    @property
    def score(self):
        return self._score

    @property
    def kda(self):
        return self._kda

    @property
    def time(self):
        return self._time

    @property
    def jogador_total_stats_id(self):
        return self._jogador_total_stats_id

    @property
    def partida_id(self):
        return self._partida_id

    @property
    def partida_md3_id(self):
        return self._partida_md3_id

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

    @kills.setter
    def kills(self, value):
        self._kills = value

    @assists.setter
    def assists(self, value):
        self._assists = value

    @deaths.setter
    def deaths(self, value):
        self._deaths = value

    @stars.setter
    def stars(self, value):
        self._stars = value

    @hs.setter
    def hs(self, value):
        self._hs = value

    @score.setter
    def score(self, value):
        self._score = value

    @kda.setter
    def kda(self, value):
        self._kda = value

    @time.setter
    def time(self, value):
        self._time = value

    @jogador_total_stats_id.setter
    def jogador_total_stats_id(self, value):
        self._jogador_total_stats_id = value

    @partida_id.setter
    def partida_id(self, value):
        self._partida_id = value

    @partida_md3_id.setter
    def partida_md3_id(self, value):
        self._partida_md3_id = value

class Partida:
    def __init__(self, id, jogo, mapa, rounds, vencedor_partida, md3_id):
        self._id = id
        self._jogo = jogo
        self._mapa = mapa
        self._rounds = rounds
        self._vencedor_partida = vencedor_partida
        self._md3_id = md3_id

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def jogo(self):
        return self._jogo

    @property
    def mapa(self):
        return self._mapa

    @property
    def rounds(self):
        return self._rounds

    @property
    def vencedor_partida(self):
        return self._vencedor_partida

    @property
    def md3_id(self):
        return self._md3_id

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

    @jogo.setter
    def jogo(self, value):
        self._jogo = value

    @mapa.setter
    def mapa(self, value):
        self._mapa = value

    @rounds.setter
    def rounds(self, value):
        self._rounds = value

    @vencedor_partida.setter
    def vencedor_partida(self, value):
        self._vencedor_partida = value

    @md3_id.setter
    def md3_id(self, value):
        self._md3_id = value

class MD3:
    def __init__(self, id, data, vencedor):
        self._id = id
        self._data = data
        self._vencedor = vencedor

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    @property
    def vencedor(self):
        return self._vencedor

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

    @data.setter
    def data(self, value):
        self._data = value

    @vencedor.setter
    def vencedor(self, value):
        self._vencedor = value