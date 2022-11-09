from google.cloud import storage

bucket_name = "multi_vid"
source_blob_name = "Double1.mp4"
destination_file_name = "D:\\Desktop\\multi_cam_person_id\\"


def download_blob(bucket_name, source_blob_name, destination_file_name):

    bucket_name = "multi_vid"
    source_blob_name = "Double1.mp4"
    destination_file_name = "D:\\Desktop\\multi_cam_person_id\\"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(blob)


download_blob(bucket_name, source_blob_name, destination_file_name)
