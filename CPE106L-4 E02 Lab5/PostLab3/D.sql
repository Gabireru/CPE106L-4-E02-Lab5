CREATE TABLE GUIDE (
    GUIDE_NUM TEXT PRIMARY KEY,
    LAST_NAME TEXT,
    FIRST_NAME TEXT,
    ADDRESS TEXT,
    CITY TEXT,
    STATE TEXT,
    POSTAL_CODE TEXT,
    PHONE_NUM TEXT,
    HIRE_DATE TEXT
);

CREATE TABLE CUSTOMER (
    CUSTOMER_NUM TEXT PRIMARY KEY,
    LAST_NAME TEXT NOT NULL,
    FIRST_NAME TEXT,
    ADDRESS TEXT,
    CITY TEXT,
    STATE TEXT,
    POSTAL_CODE TEXT,
    PHONE TEXT
);

CREATE TABLE RESERVATION (
    RESERVATION_ID TEXT PRIMARY KEY,
    TRIP_ID INTEGER,
    TRIP_DATE TEXT,
    NUM_PERSONS INTEGER,
    TRIP_PRICE REAL,
    OTHER_FEES REAL,
    CUSTOMER_NUM TEXT
);

CREATE TABLE TRIP (
    TRIP_ID INTEGER PRIMARY KEY,
    TRIP_NAME TEXT,
    START_LOCATION TEXT,
    STATE TEXT,
    DISTANCE INTEGER,
    MAX_GRP_SIZE INTEGER,
    TYPE TEXT,
    SEASON TEXT
);

CREATE TABLE TRIP_GUIDES (
    TRIP_ID INTEGER,
    GUIDE_NUM TEXT,
    PRIMARY KEY (TRIP_ID, GUIDE_NUM)
);

INSERT INTO GUIDE VALUES
('AM01', 'Abrams', 'Miles', '54 Quest Ave.', 'Williamsburg', 'MA', '01096', '617-555-6032', '2012-06-03'),
('BR01', 'Boyers', 'Rita', '140 Oakton Rd.', 'Jaffrey', 'NH', '03452', '603-555-2134', '2012-03-04'),
('DH01', 'Devon', 'Harley', '25 Old Ranch Rd.', 'Sunderland', 'MA', '01375', '781-555-7767', '2012-01-08'),
('GZ01', 'Gregory', 'Zach', '7 Moose Head Rd.', 'Dummer', 'NH', '03588', '603-555-8765', '2012-11-04'),
('KS01', 'Kiley', 'Susan', '943 Oakton Rd.', 'Jaffrey', 'NH', '03452', '603-555-1230', '2013-04-08'),
('KS02', 'Kelly', 'Sam', '9 Congaree Ave.', 'Fraconia', 'NH', '03580', '603-555-0003', '2013-06-10'),
('MR01', 'Marston', 'Ray', '24 Shenandoah Rd.', 'Springfield', 'MA', '01101', '781-555-2323', '2015-09-14'),
('RH01', 'Rowan', 'Hal', '12 Heather Rd.', 'Mount Desert', 'ME', '04660', '207-555-9009', '2014-06-02'),
('SL01', 'Stevens', 'Lori', '15 Riverton Rd.', 'Coventry', 'VT', '05825', '802-555-3339', '2014-09-05'),
('UG01', 'Unser', 'Glory', '342 Pineview St.', 'Danbury', 'CT', '06810', '203-555-8534', '2015-02-02');

INSERT INTO CUSTOMER VALUES
('101', 'Northfold', 'Liam', '9 Old Mill Rd.', 'Londonderry', 'NH', '03053', '603-555-7563'),
('102', 'Ocean', 'Arnold', '2332 South St. Apt 3', 'Springfield', 'MA', '01101', '413-555-3212'),
('103', 'Kasuma', 'Sujata', '132 Main St. #1', 'East Hartford', 'CT', '06108', '860-555-0703');

INSERT INTO RESERVATION VALUES
('1600001', 40, '2016-03-26', 2, 55.00, 0.00, '101'),
('1600002', 21, '2016-06-08', 2, 95.00, 0.00, '101'),
('1600003', 28, '2016-09-12', 1, 35.00, 0.00, '103');

INSERT INTO TRIP VALUES
(1, 'Arethusa Falls', 'Harts Location', 'NH', 5, 10, 'Hiking', 'Summer'),
(2, 'Mt Ascutney - North Peak', 'Weathersfield', 'VT', 5, 6, 'Hiking', 'Late Spring'),
(3, 'Mt Ascutney - West Peak', 'Weathersfield', 'VT', 6, 10, 'Hiking', 'Early Fall');

INSERT INTO TRIP_GUIDES VALUES
(1, 'GZ01'),
(1, 'RH01'),
(2, 'AM01'),
(2, 'SL01'),
(3, 'SL01');
