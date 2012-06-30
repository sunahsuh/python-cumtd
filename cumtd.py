import requests

# Constants
BASE_URL = 'http://developer.cumtd.com/api/'
API_VERSION = 'v2.1'

"""
Python library implementation of the Champaign-Urbana Mass Transit
District's REST API. Adheres very closely to the (excellent) documentation
available here: http://developer.cumtd.com/

Functions return a python dictionary of the parsed JSON result.
"""
class CumtdApi:
    key = None
    # TODO: Add XML support if there's a demand
    data_format = 'json' # default to json
    base_url = BASE_URL
    api_version = API_VERSION

    def __init__(self, key):
        self.key = key
        self.url = self.base_url + self.api_version + '/' + self.data_format + '/'

    # TODO: Add changeset support

    # Calendar Dates
    def get_calendar_dates_by_date(self, date):
        # TODO: Take in date of type datetime and format the string
        return self._make_mtd_request('GetCalendarDatesByDate', locals())

    def get_calendar_dates_by_service(self, service_id):
        return self._make_mtd_request('GetCalendarDatesByService', locals())

    # Departures
    def get_departures_by_stop(self, stop_id, route_id = None, pt = 30,
            count = None):
        return self._make_mtd_request('GetDeparturesByStop', locals())
    
    # Routes
    def get_route(self, route_id):
        if (type(route_id) is list):
            route_id = ''.join(route_id, ';')
        return self._make_mtd_request('GetRoute', locals())

    def get_routes(self):
        return self._make_mtd_request('GetRoutes', locals())

    # Shapes
    def get_shape(self, shape_id):
        return self._make_mtd_request('GetShape', locals())

    def get_shape_between_stops(self, begin_stop_id, end_stop_id, shape_id):
        return self._make_mtd_request('GetShapeBetweenStops', locals())

    # Stops
    def get_stop(self, stop_id):
        if (type(stop_id) is list):
            stop_id = ''.join(stop_id, ';')
        return self._make_mtd_request('GetStop', locals())

    def get_stops(self):
        return self._make_mtd_request('GetStops', locals())

    def get_stops_by_lat_lon(self, lat, lon, count=None):
        return self._make_mtd_request('GetStopsByLatLon', locals())

    def get_stops_by_search(self, query, count = None):
        return self._make_mtd_request('GetStopsBySearch', locals())

    # Stop Times
    def get_stop_times_by_trip(self, trip_id):
        return self._make_mtd_request('GetStopTimesByTrip', locals())

    def get_stop_times_by_stop(self, stop_id, route_id = None, date = None):
        if (type(route_id) is list):
            route_id = ''.join(stop_id, ';')
        return self._make_mtd_request('GetStopTimesByStop', locals())

    # Trip Planner
    def get_planned_trips_by_lat_lon(self, origin_lat, origin_lon,
            destination_lat, destination_lon, date = None, time = None,
            max_walk = None, minimize = None, arrive_depart = None):
        return self._make_mtd_request('GetPlannedTripsByLatLon', locals())

    def get_planned_trips_by_stop(self, origin_stop_id, destination_stop_id,
            date = None, time = None, max_walk = None, minimize = None,
            arrive_depart = None):
        return self._make_mtd_request('GetPlannedTripsByStop', locals())

    # Trips
    def get_trip(self, trip_id):
        return self._make_mtd_request('GetTrip', locals())

    def get_trips_by_block(self, block_id):
        return self._make_mtd_request('GetTripsByBlock', locals())

    def get_trips_by_route(self, route_id):
        return self._make_mtd_request('GetTripsByRoute', locals())
    
    # Metadata
    def get_last_feed_update(self):
        return self._make_mtd_request('GetLastFeedUpdate', locals())

    # Private functions
    def _get_mtd_param_dict(self):
        return {'key': self.key}

    def _make_mtd_request(self, api_function, function_args):
        params = self._get_mtd_param_dict()
        for k, v in function_args.items():
            if (v != None and k != 'self'):
                params[k] = v
        r = requests.get(self.url + api_function, params=params)
        # raise an error if the http response code was not ok
        r.raise_for_status()
        return r.json

