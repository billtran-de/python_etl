import psycopg2


# load transformed data into postgres
def load_data_artist_postgres(artists):
    # connect to postgres
    conn = psycopg2.connect(host='localhost',
                            database='python_pipeline',
                            user='postgres',
                            password='postgres',
                            port=5432)
    cur = conn.cursor()

    # insert data to database
    query = "INSERT INTO artist (artist_id, artist_name, artist_view_url) VALUES (%s,%s,%s)"
    for artist in artists:
        cur.execute(query, (artist[0], artist[1], artist[2]))
    conn.commit()

    # test whether data has been inserted
    cur.execute("SELECT * FROM artist")
    print(cur.fetchall())


def load_data_collection_postgres(collections):
    # connect to postgres
    conn = psycopg2.connect(host='localhost',
                            database='python_pipeline',
                            user='postgres',
                            password='postgres',
                            port=5432)
    cur = conn.cursor()

    query = "INSERT INTO collection (collection_id, artist_id, collection_name, collection_view_url, collection_price," \
            " currency) VALUES (%s,%s,%s,%s,%s,%s)"

    # insert data to database
    for collection in collections:
        cur.execute(query, (collection[0], collection[1], collection[2], collection[3], collection[4], collection[5]))
    conn.commit()

    # test whether data has been inserted
    cur.execute("SELECT * FROM collection")
    print(cur.fetchall())


def load_data_track_postgres(tracks):
    # connect to postgres
    conn = psycopg2.connect(host='localhost',
                            database='python_pipeline',
                            user='postgres',
                            password='postgres',
                            port=5432)
    cur = conn.cursor()

    query = "INSERT INTO track (track_id, collection_id, track_name, track_view_url, track_price," \
            "release_date, track_count, track_number, track_time_millis) " \
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    # insert data to database
    for track in tracks:
        cur.execute(query, (track[0], track[1], track[2], track[3], track[4], track[5], track[6], track[7],
                            track[8]))
    conn.commit()

    # test whether data has been inserted
    cur.execute("SELECT * FROM track")
    print(cur.fetchall())


# test function
if __name__ == '__main__':
    load_data_artist_postgres(artists=None)
