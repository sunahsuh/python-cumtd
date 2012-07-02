"""
Non-exhaustive tests for the CUMTD API Python helper library. Currently only tests baseline positive cases and does not test for specific output.
"""

from cumtd import CumtdApi
from datetime import datetime

KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

mtd = CumtdApi(KEY, debug=True)

now = datetime.now()

print "Testing GetCalendarDatesByDate"
services = mtd.get_calendar_dates_by_date(now.strftime('%Y-%m-%d'))
print services

print "Testing GetCalendarDatesByService"
print mtd.get_calendar_dates_by_service(services['calendar_dates'][0]['service_id'])

print "Testing GetDeparturesByStop"
print mtd.get_departures_by_stop('GRNWRT')

print "Testing GetRoute"
print mtd.get_route('GREEN')

print "Testing GetRoutes"
print mtd.get_routes()

print "Testing GetShape"
print mtd.get_shape('5E')

print "Testing GetShapeBetweenStops"
print mtd.get_shape_between_stops('GRNNEIL:6', 'IU:1', '5E')

print "Testing GetStop"
print mtd.get_stop(['GRNNEIL', 'IU'])

print "Testing GetStops"
print mtd.get_stops()

print "Testing GetStopsByLatLon"
print mtd.get_stops_by_lat_lon('40.110999', '-88.245728')

print "Testing GetStopsBySearch"
print mtd.get_stops_by_search('state and william')

print "Testing GetStopTimesByTrip"
print mtd.get_stop_times_by_trip('1GN513__GN1')

print "Testing GetStopTimesByStop"
print mtd.get_stop_times_by_stop('GRNNEIL')

print "Testing GetPlannedTripsByLatLon"
print mtd.get_planned_trips_by_lat_lon('40.110999', '-88.245728', '40.107783', '-88.23163')

print "Testing GetPlannedTripsByStops"
print mtd.get_planned_trips_by_stops('GRNNEIL', 'IU')

print "Testing GetTrip"
print mtd.get_trip('1GN513__GN1')

print "Testing GetTripsByBlock"
print mtd.get_trips_by_block('GN1')

print "Testing GetTripsByRoute"
print mtd.get_trips_by_route('GREEN')

print "Testing GetLastFeedUpdate"
print mtd.get_last_feed_update()


