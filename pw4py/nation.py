# SPDX-License-Identifier: MIT
#
# nation.py - Implements the Nation API
#
# Copyright (c) 2018-2019 Joe Dai.

# Libraries
from datetime import datetime

class Nation(object):
    """Nation API wrapper"""

    def __init__(self, id):
        # Local
        from . import session
        from . import API_PATH
        from . import API_KEY

        path = f'{API_PATH}/nation/id={id}&key={API_KEY}'
        r = session.get(path)

        _raw_JSON = r.json()
        self.raw_JSON = r.json()

        self.cityids = list(map(int, _raw_JSON['cityids']))

        self.cityprojecttimer = int(_raw_JSON['cityprojecttimerturns'])
        self.cityprojecttimerturns = int(_raw_JSON['cityprojecttimerturns'])

        self.success = bool(_raw_JSON['success'])

        self.nationid = int(_raw_JSON['nationid'])

        self.name = str(_raw_JSON['name'])

        self.prename = str(_raw_JSON['prename'])

        self.continent = str(_raw_JSON['continent'])

        self.socialpolicy = str(_raw_JSON['socialpolicy'])

        self.color = str(_raw_JSON['color'])
        self.colour = str(_raw_JSON['color'])

        self.minutessinceactive = int(_raw_JSON['minutessinceactive'])

        self.uniqueid = str(_raw_JSON['uniqueid'])

        self.government = str(_raw_JSON['government'])

        self.domesticpolicy = str(_raw_JSON['domestic_policy'])
        self.domestic_policy = str(_raw_JSON['domestic_policy'])

        self.warpolicy = str(_raw_JSON['war_policy'])
        self.war_policy = str(_raw_JSON['war_policy'])

        self.founded = datetime.strptime(_raw_JSON['founded'], '%Y-%m-%d %H:%M:%S')
        self.founded_str = str(_raw_JSON['founded'])

        self.daysold = int(_raw_JSON['daysold'])

        if str(_raw_JSON['alliance']) == "None":
            self.alliance = None
        else:
            self.alliance = str(_raw_JSON['alliance'])

        self.allianceposition = int(_raw_JSON['allianceposition'])
        self.allianceposition_str = {5: 'leader', 4: 'heir', 3: 'officer', 2: 'member', 1: 'applicant', 0: None}[int(_raw_JSON['allianceposition'])]

        if int(_raw_JSON['allianceid']) == 0:
            self.allianceid = None
        else:
            self.allianceid = int(_raw_JSON['allianceid'])

        self.flagurl = str(_raw_JSON['flagurl'])

        self.leader = str(_raw_JSON['leadername'])
        self.leadername = str(_raw_JSON['leadername'])

        self.title = str(_raw_JSON['title'])

        self.ecopolicy = str(_raw_JSON['ecopolicy'])

        self.approvalrating = float(_raw_JSON['approvalrating'])

        self.nationrank = int(_raw_JSON['nationrank'])

        self.nationrank_str = str(_raw_JSON['nationrankstrings'])
        self.nationrankstrings = str(_raw_JSON['nationrankstrings'])

        self.nrtotal = int(_raw_JSON['nrtotal'])

        self.cities = int(_raw_JSON['cities'])

        self.latitude = float(_raw_JSON['latitude'])

        self.longitude = float(_raw_JSON['longitude'])

        self.score = float(_raw_JSON['score'])

        self.population = int(_raw_JSON['population'])

        self.gdp = float(_raw_JSON['gdp'])
        self.gdp_str = '${:,.2f}'.format(float(_raw_JSON['gdp']))

        self.totalinfrastructure = float(_raw_JSON['totalinfrastructure'])

        self.landarea = float(_raw_JSON['landarea'])

        # --- Military ---

        self.soldiers = int(_raw_JSON['soldiers'])
        self.soldiercasualties = int(_raw_JSON['soldiercasualties'])
        self.soldierskilled = int(_raw_JSON['soldierskilled'])

        self.tanks = int(_raw_JSON['tanks'])
        self.tankcasualties = int(_raw_JSON['tankcasualties'])
        self.tankskilled = int(_raw_JSON['tankskilled'])

        self.aircraft = int(_raw_JSON['aircraft'])
        self.aircraftcasualties = int(_raw_JSON['aircraftcasualties'])
        self.aircraftkilled = int(_raw_JSON['aircraftkilled'])

        self.ships = int(_raw_JSON['ships'])
        self.shipcasualties = int(_raw_JSON['shipcasualties'])
        self.shipskilled = int(_raw_JSON['shipskilled'])

        self.missiles = int(_raw_JSON['missiles'])
        self.missilelaunched = int(_raw_JSON['missilelaunched'])
        self.missileseaten = int(_raw_JSON['missileseaten'])

        self.nukes = int(_raw_JSON['nukes'])
        self.nukeslaunched = int(_raw_JSON['nukeslaunched'])
        self.nukeseaten = int(_raw_JSON['nukeseaten'])

        # --- War stats ---

        self.totalinfradestroyed = float(_raw_JSON['infdesttot'])
        self.infdesttot = float(_raw_JSON['infdesttot'])

        self.infralost = float(_raw_JSON['infraLost'])
        self.infraLost = float(_raw_JSON['infraLost'])

        self.moneylooted = float(_raw_JSON['moneyLooted'])
        self.moneyLooted = float(_raw_JSON['moneyLooted'])

        # --- Projects ---

        self.IW = bool(int(_raw_JSON['ironworks']))
        self.ironworks = bool(int(_raw_JSON['ironworks']))

        self.BW = bool(int(_raw_JSON['bauxiteworks']))
        self.bauxiteworks = bool(int(_raw_JSON['bauxiteworks']))

        self.AS = bool(int(_raw_JSON['armsstockpile']))
        self.armsstockpile = bool(int(_raw_JSON['armsstockpile']))

        self.EGR = bool(int(_raw_JSON['emgasreserve']))
        self.emgasreserve = bool(int(_raw_JSON['emgasreserve']))

        self.MI = bool(int(_raw_JSON['massirrigation']))
        self.massirrigation = bool(int(_raw_JSON['massirrigation']))

        self.ITC = bool(int(_raw_JSON['inttradecenter']))
        self.inttradecenter = bool(int(_raw_JSON['inttradecenter']))

        self.MLP = bool(int(_raw_JSON['missilelpad']))
        self.missilelpad = bool(int(_raw_JSON['missilelpad']))

        self.NRF = bool(int(_raw_JSON['nuclearresfac']))
        self.nuclearresfac = bool(int(_raw_JSON['nuclearresfac']))

        self.ID = bool(int(_raw_JSON['irondome']))
        self.irondome = bool(int(_raw_JSON['irondome']))

        self.VDS = bool(int(_raw_JSON['vitaldefsys']))
        self.vitaldefsys = bool(int(_raw_JSON['vitaldefsys']))

        self.IA = bool(int(_raw_JSON['intagncy']))
        self.intagncy = bool(int(_raw_JSON['intagncy']))

        self.UEP = bool(int(_raw_JSON['uraniumenrich']))
        self.uraniumenrich = bool(int(_raw_JSON['uraniumenrich']))

        self.PB = bool(int(_raw_JSON['propbureau']))
        self.propbureau = bool(int(_raw_JSON['propbureau']))

        self.CCE = bool(int(_raw_JSON['cenciveng']))
        self.cenciveng = bool(int(_raw_JSON['cenciveng']))

        # ---

        self.vmode = bool(int(_raw_JSON['vmode']))

        self.offensivewars = int(_raw_JSON['offensivewars'])

        self.defensivewars = int(_raw_JSON['defensivewars'])

        self.offensivewar_ids = list(map(int, _raw_JSON['offensivewar_ids']))

        self.defensivewar_ids = list(map(int, _raw_JSON['defensivewar_ids']))

        self.beigeturnsleft = int(_raw_JSON['beige_turns_left'])
        self.beige_turns_left = int(_raw_JSON['beige_turns_left'])

        self.radiationindex = float(_raw_JSON['radiation_index'])
        self.radiation_index = float(_raw_JSON['radiation_index'])

        self.season = str(_raw_JSON['season'])

    def get(self, field):
        """
        Get an attribute

        Arguments:
            field {str} -- the attribute to get

        Returns:
            Union[int, str, float, bool, None] -- attribute contents
        """

        return getattr(self, field)

    def __str__(self):
        """
        Get name of alliance

        Returns:
            str -- name of alliance
        """

        return self.raw_JSON['name']
