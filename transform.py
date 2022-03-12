# transform artist data from api to insert to database
def transform_data_for_artist(data):
    # create a list of tuples
    # each tuple is a row to insert into database
    temp_artists = []
    for i in range(len(data)):
        each_artist = [data[i]['artistId'], data[i]['artistName'], data[i]['artistViewUrl']]
        each_artist = tuple(each_artist)
        temp_artists.append(each_artist)

    artists = [artist for artist in set(tuple(i) for i in temp_artists)]

    # remove duplicate key of artist data
    artists.remove((136975, 'The Beatles & Billy Preston', 'https://music.apple.com/us/artist/the-beatles/136975?uo=4'))

    return artists


# transform collection data from api to insert to database
def transform_data_for_collection(data):
    # create a list of tuples
    # each tuple is a row to insert into database
    temp_collection = []
    for i in range(len(data)):
        each_collection = [data[i]['collectionId'], data[i]['artistId'], data[i]['collectionName'],
                           data[i]['collectionViewUrl'], data[i]['collectionPrice'], data[i]['currency']]
        each_collection = tuple(each_collection)
        temp_collection.append(each_collection)
    collections = [collection for collection in set(tuple(i) for i in temp_collection)]

    # remove duplicate key of collection data
    duplicated_key = set()
    final_collections = []
    for collection_id, artist_id, collection_name, collection_view_url, collection_price, currency in collections:
        if not collection_id in duplicated_key:
            duplicated_key.add(collection_id)
            final_collections.append((collection_id, artist_id, collection_name, collection_view_url, collection_price, currency))
    return final_collections


# transform track data from api to insert to database
def transform_data_for_track(data):
    # create a list of tuples
    # each tuple is a row to insert into database
    temp_track = []
    for i in range(len(data)):
        if data[i]['wrapperType'] == "track":
            each_track = [data[i]['trackId'], data[i]['collectionId'], data[i]['trackName'],
                          data[i]['trackViewUrl'], data[i]['trackPrice'], data[i]['releaseDate'], data[i]['trackCount'],
                          data[i]['trackNumber'], data[i]['trackTimeMillis']]
            each_track = tuple(each_track)
            temp_track.append(each_track)
    tracks = [track for track in set(tuple(i) for i in temp_track)]

    # remove duplicate key of track data
    duplicated_key = set()
    final_tracks = []
    for track_id, collection_id, track_name, track_view_url, track_price, release_date, track_count,\
            track_number, track_time_millis in tracks:
        if not track_id in duplicated_key:
            duplicated_key.add(track_id)
            final_tracks.append((track_id, collection_id, track_name, track_view_url, track_price, release_date, track_count,\
            track_number, track_time_millis))
    return final_tracks


# test function
if __name__ == '__main__':
    print(transform_data_for_track())
