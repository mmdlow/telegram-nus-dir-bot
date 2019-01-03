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

resd = {
'Air Conditioning Management': 'https://nus-utown.evs.com.sg/',
'Dining Management': 'https://aces.nus.edu.sg/Prjhml/',
'Hostel Management': 'https://uhms.nus.edu.sg/',
'Module Registration': 'https://myaces.nus.edu.sg/prjmps/MasterServletStudent?actionParam=studentlogin',
'Halls and Residences':
{
	'Eusoff Hall': 'http://nusync.orgsync.com/org/eusoffhall',
	'Kent Ridge Hall': 'http://nusync.orgsync.com/org/kentridgehall/',
	'King Edward VII Hall': 'http://www.kevii.nus.edu.sg/',
	'Raffles Hall': 'http://raffles.nus.edu.sg/',
	'Sheares Hall': 'http://nusync.orgsync.com/org/sheareshall'
	'Temasek Hall': 'http://www.temasek.nus.edu.sg/'
	'PGP House': 'http://www.nus.edu.sg/pgphouse/',
	'Cinammon College': 'http://www.usp.nus.edu.sg/life-at-usp/usp-housing-and-support/cinnamon-college-usp',
	'Tembusu College': 'https://tembusu.nus.edu.sg/',
	'College Of Alice & Peter Tan': 'http://capt.nus.edu.sg/',
	'Residential College 4': 'http://rc4.nus.edu.sg/',
	'Prince Georges Park Residences': 'https://uci.nus.edu.sg/ohs/future-residents/undergraduates/prince-georges-park-residences/',
	'UTown Residence': 'https://uci.nus.edu.sg/ohs/future-residents/graduates/utown/'
}
}

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