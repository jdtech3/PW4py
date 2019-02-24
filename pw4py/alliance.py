# SPDX-License-Identifier: MIT
#
# alliance.py - Implements the Alliance API
#
# Copyright (c) 2018-2019 Joe Dai.

class Alliance(object):
    def __init__(self, id):
        # Local
        from . import session
        from . import API_PATH

        path = f'{API_PATH}/alliance/id={id}'
        r = session.get(path)

        _raw_JSON = r.json()
        self.raw_JSON = r.json()

        self.leaderids = list(map(int, _raw_JSON['leaderids']))

        self.success = bool(_raw_JSON['success'])

        self.allianceid = int(_raw_JSON['allianceid'])

        self.name = str(_raw_JSON['name'])

        self.acronym = str(_raw_JSON['acronym'])

        self.score = float(_raw_JSON['score'])

        self.color = str(_raw_JSON['color'])
        self.colour = str(_raw_JSON['color'])

        self.members = int(_raw_JSON['members'])

        self.member_id_list = list(map(int, _raw_JSON['member_id_list']))

        self.vmodemembers = int(_raw_JSON['vmodemembers'])
        self.vmode_members = int(_raw_JSON['vmodemembers'])

        self.accepting_members = bool(_raw_JSON['accepting members'])   # wtf why a space there

        self.applicants = int(_raw_JSON['applicants'])

        self.flagurl = str(_raw_JSON['flagurl'])

        self.forumurl = str(_raw_JSON['forumurl'])

        self.irc = str(_raw_JSON['irc'])
        self.discord = str(_raw_JSON['irc'])

        self.gdp = float(_raw_JSON['gdp'])
        self.gdp_str = '${:,.2f}'.format(float(_raw_JSON['gdp']))

        self.cities = int(_raw_JSON['cities'])

        # --- Military ---

        self.soldiers = int(_raw_JSON['soldiers'])

        self.tanks = int(_raw_JSON['tanks'])

        self.aircraft = int(_raw_JSON['aircraft'])

        self.ships = int(_raw_JSON['ships'])

        self.missiles = int(_raw_JSON['missiles'])

        self.nukes = int(_raw_JSON['nukes'])

        # --- ---

        self.treasures = int(_raw_JSON['treasures'])

    def get(self, field):
        return getattr(self, field)

    def __str__(self):
        return self.raw_JSON['name']
