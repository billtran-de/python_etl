CREATE TABLE artist (
	artist_id INT PRIMARY KEY,
	artist_name VARCHAR (50),
	artist_view_url VARCHAR (1000)
);

CREATE TABLE collection (
	collection_id INT PRIMARY KEY,
	artist_id INT,
	collection_name VARCHAR (50),
	collection_view_url VARCHAR (1000),
	collection_price FLOAT,
	disc_count INT,
	disc_number INT,
	currency VARCHAR (10),
	FOREIGN KEY (artist_id) REFERENCES artist (artist_id)
);

CREATE TABLE track (
	track_id INT PRIMARY KEY,
	collection_id INT,
	track_name VARCHAR (50),
	track_view_url VARCHAR (1000),
	track_price FLOAT,
	release_date TIMESTAMP,
	track_count INT,
	track_number INT,
	track_time_millis INT,
	is_streamable BOOL,
	FOREIGN KEY (collection_id) REFERENCES collection (collection_id)
);

