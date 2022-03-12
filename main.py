from extract import extract_data_from_api
from transform import transform_data_for_artist, transform_data_for_collection, transform_data_for_track
from load import load_data_artist_postgres, load_data_collection_postgres, load_data_track_postgres

# ETL from API to Postgres (artist table, collection table, track table)
if __name__ == '__main__':
    # get data from API
    data = extract_data_from_api()

    # transform artist data
    artists = transform_data_for_artist(data)

    # load artist data to Postgres
    load_data_artist_postgres(artists)

    # transform collection data
    collections = transform_data_for_collection(data)

    # load collection data to Postgres
    load_data_collection_postgres(collections)

    # transform track data
    tracks = transform_data_for_track(data)

    # load track data to Postgres
    load_data_track_postgres(tracks)
