import pytest

@pytest.fixture
def nation_instance():
    from pw4py import Nation
    return Nation(6)

def test_cityids(nation_instance):
    """Tests if API returns 'cityids' correctly"""

    assert nation_instance.cityids == [10618, 131681]

def test_cityprojecttimerturns(nation_instance):
    """Tests if API returns 'cityprojecttimerturns': 0"""

    assert nation_instance.cityprojecttimer == 0
    assert nation_instance.cityprojecttimerturns == 0

def test_nation_API_success(nation_instance):
    """Tests if API returns 'success': True"""

    assert nation_instance.success == True
    assert nation_instance.get('success')

def test_nationid(nation_instance):
    """Tests if nation ID is correct"""

    assert nation_instance.nationid == 6

def test_nation_name(nation_instance):
    """Tests if nation name is correct"""

    assert nation_instance.name == "Mountania"
    assert str(nation_instance) == "Mountania"

def test_prename(nation_instance):
    """Tests if nation prename is correct"""

    assert nation_instance.prename == "The Dominion of"

def test_continent(nation_instance):
    """Tests if continent is correct"""

    assert nation_instance.continent == "North America"

def test_socialpolicy(nation_instance):
    """Tests if social policy is correct"""

    assert nation_instance.socialpolicy == "moderate"

def test_color(nation_instance):
    """Tests if color is correct"""

    assert nation_instance.color == "aqua" or nation_instance.color == "beige"
    assert nation_instance.colour == "aqua" or nation_instance.colour == "beige"

def test_minutessinceactive(nation_instance):
    """Tests if minutessinceactive is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.minutessinceactive, int)

def test_uniqueid(nation_instance):
    """Tests if unique ID is of correc type"""

    assert isinstance(nation_instance.uniqueid, str)

def test_government(nation_instance):
    """Tests if government type is correct"""

    assert nation_instance.government == "People's Republic"

def test_domesticpolicy(nation_instance):
    """Tests if domestic policy is correct"""

    assert nation_instance.domesticpolicy == "Urbanization"
    assert nation_instance.domestic_policy == "Urbanization"

def test_warpolicy(nation_instance):
    """Tests if war policy is correct"""

    assert nation_instance.warpolicy == "Turtle"
    assert nation_instance.war_policy == "Turtle"

def test_founded(nation_instance):
    """Tests if  is correct"""

    from datetime import datetime

    assert nation_instance.founded == datetime(2014, 8, 5, 0, 10, 59)
    assert nation_instance.founded_str == "2014-08-05 00:10:59"


def test_daysold(nation_instance):
    """Tests if daysold is of correct type"""

    assert isinstance(nation_instance.daysold, int)

def test_alliance(nation_instance):
    """Tests if alliance is correct"""

    assert nation_instance.alliance == None

def test_allianceposition(nation_instance):
    """Tests if alliance position is correct"""

    assert nation_instance.allianceposition == 0
    assert nation_instance.allianceposition_str == None

def test_allianceid(nation_instance):
    """Tests if alliance ID is correct"""

    assert nation_instance.allianceid == None

def test_flagurl(nation_instance):
    """Tests if flag URL is correct"""

    assert nation_instance.flagurl == "https://politicsandwar.com/uploads/125eff51f3476cd5f24debb891968eeb58bef89a566.png"

def test_leadername(nation_instance):
    """Tests if leader name is correct"""

    assert nation_instance.leader == "Alex"
    assert nation_instance.leadername == "Alex"

def test_title(nation_instance):
    """Tests if title is correct"""

    assert nation_instance.title == "Head Administrator"

def test_ecopolicy(nation_instance):
    """Tests if eco policy is correct"""

    assert nation_instance.ecopolicy == "moderate"

def test_approvalrating(nation_instance):
    """Tests if approval rating is correct"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.approvalrating, float)

def test_nationrank(nation_instance):
    """Tests if nation rank is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.nationrank, int)

def test_nationrankstrings(nation_instance):
    """Tests if nation rank is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.nationrank_str, str)
    assert isinstance(nation_instance.nationrankstrings, str)

def test_nrtotal(nation_instance):
    """Tests if nrtotal is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.nrtotal, int)

def test_cities(nation_instance):
    """Tests if cities is correct"""

    assert nation_instance.cities == 2

def test_latitude(nation_instance):
    """Tests if latitude is correct"""

    assert nation_instance.latitude == 48.82

def test_longitude(nation_instance):
    """Tests if longitude is correct"""

    assert nation_instance.longitude == -122.65

def test_score(nation_instance):
    """Tests if score is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.score, float)

def test_population(nation_instance):
    """Tests if population is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.population, int)

def test_gdp(nation_instance):
    """Tests if gdp is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.gdp, float)

def test_totalinfrastructure(nation_instance):
    """Tests if total infrastructure is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.totalinfrastructure, float)

def test_landarea(nation_instance):
    """Tests if land area is of correct type"""

    # Impossible to test for correct value
    assert isinstance(nation_instance.landarea, float)

def test_soldier_stats(nation_instance):
    """Tests if soldier stats are of correct type"""

    assert isinstance(nation_instance.soldiers, int)
    assert isinstance(nation_instance.soldiercasualties, int)
    assert isinstance(nation_instance.soldierskilled, int)

def test_tank_stats(nation_instance):
    """Tests if tanks stats are of correct type"""

    assert isinstance(nation_instance.tanks, int)
    assert isinstance(nation_instance.tankcasualties, int)
    assert isinstance(nation_instance.tankskilled, int)

def test_aircraft_stats(nation_instance):
    """Tests if aircraft stats are of correct type"""

    assert isinstance(nation_instance.aircraft, int)
    assert isinstance(nation_instance.aircraftcasualties, int)
    assert isinstance(nation_instance.aircraftkilled, int)

def test_ship_stats(nation_instance):
    """Tests if ship stats are of correct type"""

    assert isinstance(nation_instance.ships, int)
    assert isinstance(nation_instance.shipcasualties, int)
    assert isinstance(nation_instance.shipskilled, int)

def test_missile_stats(nation_instance):
    """Tests if missile stats are of correct type"""

    assert isinstance(nation_instance.missiles, int)
    assert isinstance(nation_instance.missilelaunched, int)
    assert isinstance(nation_instance.missileseaten, int)

def test_nuke_stats(nation_instance):
    """Tests if nuke stats are of correct type"""

    assert isinstance(nation_instance.nukes, int)
    assert isinstance(nation_instance.nukeslaunched, int)
    assert isinstance(nation_instance.nukeseaten, int)

def test_infra_war_stats(nation_instance):
    """Tests if infra war stats are of correct type"""

    assert isinstance(nation_instance.infdesttot, float)
    assert isinstance(nation_instance.totalinfradestroyed, float)

    assert isinstance(nation_instance.infraLost, float)
    assert isinstance(nation_instance.infralost, float)

def test_projects(nation_instance):
    """Tests if projects are correct"""

    assert nation_instance.ironworks == 0
    assert nation_instance.IW == 0
    assert nation_instance.bauxiteworks == 0
    assert nation_instance.BW == 0
    assert nation_instance.armsstockpile == 0
    assert nation_instance.AS == 0
    assert nation_instance.emgasreserve == 0
    assert nation_instance.EGR == 0
    assert nation_instance.massirrigation == 0
    assert nation_instance.MI == 0
    assert nation_instance.inttradecenter == 0
    assert nation_instance.ITC == 0
    assert nation_instance.missilelpad == 1
    assert nation_instance.MLP == 1
    assert nation_instance.nuclearresfac == 1
    assert nation_instance.NRF == 1
    assert nation_instance.irondome == 0
    assert nation_instance.ID == 0
    assert nation_instance.vitaldefsys == 0
    assert nation_instance.VDS == 0
    assert nation_instance.intagncy == 1
    assert nation_instance.IA == 1
    assert nation_instance.uraniumenrich == 1
    assert nation_instance.UEP == 1
    assert nation_instance.propbureau == 0
    assert nation_instance.PB == 0
    assert nation_instance.cenciveng == 0
    assert nation_instance.CCE == 0

def test_vmode(nation_instance):
    """Tests if vmode is False"""

    assert nation_instance.vmode == False

def test_offensivewars(nation_instance):
    """Tests if offensivewars is of correct type"""

    assert isinstance(nation_instance.offensivewars, int)

def test_defensivewars(nation_instance):
    """Tests if defensivewars is of correct type"""

    assert isinstance(nation_instance.defensivewars, int)

def test_offensivewar_ids(nation_instance):
    """Tests if offensivewar_ids is of correct type"""

    assert isinstance(nation_instance.offensivewar_ids, list)
    assert all(isinstance(x, int) for x in nation_instance.offensivewar_ids)

def test_defensivewar_ids(nation_instance):
    """Tests if defensivewar_ids is of correct type"""

    assert isinstance(nation_instance.defensivewar_ids, list)
    assert all(isinstance(x, int) for x in nation_instance.defensivewar_ids)

def test_beige_turns_left(nation_instance):
    """Tests if beige_turns_left is of correct type"""

    assert isinstance(nation_instance.beigeturnsleft, int)
    assert isinstance(nation_instance.beige_turns_left, int)

def test_radiation_index(nation_instance):
    """Tests if radiation_index is of correct type"""

    assert isinstance(nation_instance.radiationindex, float)
    assert isinstance(nation_instance.radiation_index, float)

def test_season(nation_instance):
    """Tests if season is of correct type"""

    assert isinstance(nation_instance.season, str)

