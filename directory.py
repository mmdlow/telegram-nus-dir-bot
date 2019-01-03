acad = {
'CORS': 'http://www.cors.nus.edu.sg/',
'EduRec': 'https://myisis.nus.edu.sg/psp/cs90prd/?cmd=login',
'IVLE': 'https://ivle.nus.edu.sg/default.aspx',
'LumiNus': 'https://luminus.nus.edu.sg/',
'NUS Libraries': 'https://libportal.nus.edu.sg/frontend/index',
'Nusmods': 'https://nusmods.com/'
}

faci = {
'Parking': 'https://uci.nus.edu.sg/oca/transport-logistics-carpark/parking-information-for-visitors/',
'Bookings': 
{
	'Kent Ridge': 'https://aces.nus.edu.sg/fbs/HomeServlet',
	'UTown': 'https://utownfbs.nus.edu.sg/utown/apptop.aspx',
	'Sports Facilities': 'https://reboks.nus.edu.sg/nus_public_web/public/facilities'
}
}

facu = {}
resd = {}
misc = {}

# OUTERMOST LAYER
# Contains all 5 main categories
link_dict = {
'Academic': acad,
'Facilities': faci,
'Faculties': facu,
'Residences': resd,
'Miscellaneous': misc
}