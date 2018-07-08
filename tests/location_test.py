# coding=utf-8

import unittest
from ladybug.location import Location


class LocationTestCase(unittest.TestCase):
    """Test for (ladybug/location.py)"""

    # preparing to test.
    def setUp(self):
        """set up."""
        pass

    def tearDown(self):
        """Nothing to tear down as nothing gets written to file."""
        pass

    def test_default_values(self):
        """Test if the command correctly creates a location."""
        loc = Location()
        assert loc.city == '-'
        assert loc.country == '-'
        assert loc.latitude == 0
        assert loc.longitude == 0
        assert loc.time_zone == 0
        assert loc.station_id is None
        assert loc.source is None

    def test_from__init__(self):
        """Test if the command correctly creates location based on individual values"""
        # This is totally a real place! It's in Wales, check it out!
        city = 'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch'
        country = 'United Kingdom'
        latitude = 53.2225252
        longitude = -4.2211707
        time_zone = 1
        elevation = 12
        station_id = 'SomeInventedStation'
        source = 'SomeNoneExistentSource'

        loc = Location(city=city, country=country, latitude=latitude,
                       longitude=longitude, time_zone=time_zone,
                       elevation=elevation, station_id=station_id, source=source)

        assert loc.city == city
        assert loc.country == country
        assert loc.latitude == latitude
        assert loc.longitude == longitude
        assert loc.time_zone == time_zone
        assert loc.elevation == elevation
        assert loc.station_id == station_id
        assert loc.source == source
        assert loc.meridian == -15

    def test_from_individual_values(self):
        """Test if the command correctly creates location based on individual values"""
        loc = Location()

        new_latitude = 31.4234953
        new_longitude = 72.9492158
        new_time_zone = 5
        new_elevation = 20

        loc.latitude = new_latitude
        loc.longitude = new_longitude
        loc.time_zone = new_time_zone
        loc.elevation = new_elevation

        assert loc.latitude == new_latitude
        assert loc.longitude == new_longitude
        assert loc.time_zone == new_time_zone
        assert loc.elevation == new_elevation

    def test_from_location(self):
        """Test the from_location() class method"""
        city = 'Tehran'
        country = 'Iran'
        latitude = 36
        longitude = 34
        time_zone = 3.5
        elevation = 54

        loc = Location(city=city, country=country, latitude=latitude,
                       longitude=longitude, time_zone=time_zone,
                       elevation=elevation)

        loc_from_loc = Location.from_location(loc)

        assert loc_from_loc.city == city
        assert loc_from_loc.country == country
        assert loc_from_loc.latitude == latitude
        assert loc_from_loc.longitude == longitude
        assert loc_from_loc.time_zone == time_zone
        assert loc_from_loc.elevation == elevation

    def test_json_methods(self):
        """Test JSON serialization functions"""
        city = 'Tehran'
        country = 'Iran'
        latitude = 36
        longitude = 34
        time_zone = 3.5
        elevation = 54

        loc = Location(city=city, country=country, latitude=latitude,
                       longitude=longitude, time_zone=time_zone,
                       elevation=elevation)

        assert loc.to_json() == {"city": city, "country": country, "latitude": latitude,
                                 "longitude": longitude, "time_zone": time_zone,
                                 "elevation": elevation}

        loc_from_json = Location.from_json(loc.to_json())

        assert loc_from_json.city == city
        assert loc_from_json.latitude == latitude
        assert loc_from_json.longitude == longitude
        assert loc_from_json.time_zone == time_zone
        assert loc_from_json.elevation == elevation
        assert loc_from_json.country == country


if __name__ == "__main__":
    unittest.main()
