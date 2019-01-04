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

# Needs updating to include all related sites, e.g. mysoc
# Needs to expand to include all departments
facu = {
'Architecture': 'http://www.arch.nus.edu.sg/',
'Arts & Social Sciences': 'http://www.fas.nus.edu.sg/',
'Business & Accountancy': 'http://bba.nus.edu/',
'Computing': 'https://www.comp.nus.edu.sg/',
'Dentistry': 'http://www.dentistry.nus.edu.sg/',
'Duke-NUS': 'https://www.duke-nus.edu.sg/',
'Engineering': 'https://www.eng.nus.edu.sg/',
'Industrial Design': 'http://did.nus.edu.sg/',
'Law': 'http://law.nus.edu.sg/',
'Medicine': 'http://nusmedicine.nus.edu.sg/',
'Music': 'https://www.ystmusic.nus.edu.sg/',
'Nursing': 'http://medicine.nus.edu.sg/nursing/',
'Project & Facilities Management': 'http://www.bdg.nus.edu.sg/undergraduate/PFM-introduction.html',
'Public Health': 'https://www.sph.nus.edu.sg/',
'Public Policy': 'https://lkyspp.nus.edu.sg/',
'Real Estate': 'http://www.rst.nus.edu.sg/index.html',
'Science':
{
	'Chemistry': 'http://www.chemistry.nus.edu.sg/',
	'Computational Biology': 'http://www.science.nus.edu.sg/undergraduate-studies/ugprog/primary-majors/174-undergraduate/ugprog/554-computational-biology',
	'Data Science': 'https://www.stat.nus.edu.sg/index.php/prospective-students/undergraduate-programme/data-science-and-analytics',
	'Environmental Science': 'http://www.envstudies.nus.edu.sg/',
	'Food Science': 'http://www.fst.nus.edu.sg/',
	'Life Sciences': 'http://www.lifesciences.nus.edu.sg/',
	'Mathematics': 'http://ww1.math.nus.edu.sg/default.aspx',
	'Pharmacy': 'http://pharmacy.nus.edu.sg/',
	'Physics': 'http://www.physics.nus.edu.sg/',
	'Quantitative Finance': 'http://www.nus.edu.sg/nusbulletin/faculty-of-science/undergraduate-education/degree-requirements/bachelor-of-sciencebachelor-of-science-hons-programme-requirements-b-sc-b-sc-hons/quantitative-finance/',
	'Statistics': 'https://www.stat.nus.edu.sg/index.php/current-students/undergraduate-programme/programme-structure'
},
'University Scholars Programme': 'http://www.usp.nus.edu.sg/'
}

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

misc = {
'AIMS': 'https://inetapps.nus.edu.sg/osh/portal/eServices/ehs360_aims.html',
'NUS email': 'https://exchange.nus.edu.sg/',
'NUSync': 'https://orgsync.com/login/national-university-of-singapore',
'NUS Whispers': 'https://www.nuswhispers.com/home/'
}

# OUTERMOST LAYER
# Contains all 5 main categories
link_dict = {
'Academic': acad,
'Facilities': faci,
'Faculties': facu,
'Residences': resd,
'Miscellaneous': misc
}